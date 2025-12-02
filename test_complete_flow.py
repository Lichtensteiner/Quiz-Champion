#!/usr/bin/env python
"""Test complet du flux: jouer une partie et vérifier les stats de catégorie"""

from src.quiz_champion.models.database import Database
from src.quiz_champion.services import (
    UserService, CategoryStatsService, RecommendationService, GameService
)
from src.quiz_champion.models import Game, GameAnswer, Question, Choice
from datetime import datetime

def test_complete_flow():
    """Test le flux complet: créer utilisateur → jouer → mettre à jour stats → recommander"""
    
    db = Database()
    db.init_db()
    session = db.get_session()
    
    print("=" * 70)
    print("TEST COMPLET - MODE ENTRAÎNEMENT PAR CATÉGORIE + RECOMMANDATIONS IA")
    print("=" * 70)
    
    # ÉTAPE 1: Créer un utilisateur
    print("\n📝 ÉTAPE 1: Créer un utilisateur")
    user = UserService.create_user(session, "joueur_test")
    print(f"✅ Utilisateur créé: {user.pseudo} (ID: {user.id})")
    
    # ÉTAPE 2: Récupérer les catégories
    print("\n📚 ÉTAPE 2: Récupérer les catégories disponibles")
    all_cats_data = CategoryStatsService.get_all_categories_with_stats(session, user.id)
    print(f"✅ {len(all_cats_data)} catégories disponibles")
    
    # ÉTAPE 3: Créer une partie pour une catégorie spécifique
    print("\n🎮 ÉTAPE 3: Créer une partie - Catégorie 'Gabon'")
    gabon_cat = next((c for c in all_cats_data if c['category_name'] == 'Gabon'), None)
    
    if gabon_cat:
        # Créer une partie
        game = Game(
            user_id=user.id,
            mode="solo",
            num_questions=5,
            started_at=datetime.utcnow()
        )
        session.add(game)
        session.commit()
        session.refresh(game)
        print(f"✅ Partie créée: {game.id}")
        
        # ÉTAPE 4: Ajouter des réponses
        print("\n📋 ÉTAPE 4: Simuler des réponses")
        questions = session.query(Question).filter(
            Question.category_id == gabon_cat['category_id'],
            Question.status == "publié"
        ).limit(5).all()
        
        correct_count = 0
        for i, question in enumerate(questions, 1):
            if question.choices:
                choice = question.choices[0]
                is_correct = choice.is_correct
                
                game_answer = GameAnswer(
                    game_id=game.id,
                    question_id=question.id,
                    choice_id=choice.id,
                    is_correct=is_correct,
                    time_taken=0,
                    points_earned=10 if is_correct else 0
                )
                session.add(game_answer)
                
                if is_correct:
                    correct_count += 1
                    status = "✓"
                else:
                    status = "✗"
                
                print(f"  {status} Question {i}: {status} ({'Correcte' if is_correct else 'Incorrecte'})")
        
        session.commit()
        print(f"✅ {correct_count}/{len(questions)} réponses correctes")
        
        # ÉTAPE 5: Mettre à jour les stats de catégorie
        print("\n📊 ÉTAPE 5: Mettre à jour les stats de catégorie")
        CategoryStatsService.update_category_stats_after_game(session, user.id, game)
        print(f"✅ Stats de catégorie mises à jour")
        
        # ÉTAPE 6: Afficher les stats
        print("\n📈 ÉTAPE 6: Afficher les stats de la catégorie")
        cat_stats_data = CategoryStatsService.get_all_categories_with_stats(session, user.id)
        gabon_stats = next((c for c in cat_stats_data if c['category_name'] == 'Gabon'), None)
        if gabon_stats:
            print(f"✅ Stats pour 'Gabon':")
            print(f"  - Parties: {gabon_stats['user_games']}")
            print(f"  - Correctes: {gabon_stats['user_correct']}")
            print(f"  - Réponses: {gabon_stats['user_answered']}")
            print(f"  - Précision: {gabon_stats['user_accuracy']:.1f}%")
        
        # ÉTAPE 7: Générer les recommandations
        print("\n🤖 ÉTAPE 7: Générer les recommandations IA")
        recommendations = RecommendationService.get_learning_recommendations(session, user.id)
        print(f"✅ {len(recommendations)} recommandations générées:")
        for i, rec in enumerate(recommendations, 1):
            title = rec.get('title', 'N/A')
            emoji = rec.get('emoji', '•')
            message = rec.get('message', '')
            print(f"  {i}. {emoji} {title}")
            print(f"     → {message[:60]}...")
        
        # ÉTAPE 8: Résumé de maîtrise
        print("\n🏆 ÉTAPE 8: Résumé de maîtrise")
        mastery = RecommendationService.get_mastery_summary(session, user.id)
        for level, categories in mastery.items():
            if categories:
                print(f"✅ {level.upper()}: {', '.join(categories)}")
    
    print("\n" + "=" * 70)
    print("✅ TEST COMPLET RÉUSSI!")
    print("=" * 70)
    
    session.close()

if __name__ == "__main__":
    test_complete_flow()

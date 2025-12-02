#!/usr/bin/env python
"""Test d'intégration des nouvelles fonctionnalités de catégories"""

from src.quiz_champion.models.database import Database
from src.quiz_champion.services import (
    CategoryStatsService, RecommendationService, UserService, QuestionService
)
from src.quiz_champion.models import Category, Question, User

def test_category_stats_integration():
    """Test l'intégration complète du système de catégories"""
    
    # Initialiser la base de données
    db = Database()
    db.init_db()
    session = db.get_session()
    
    print("=" * 60)
    print("TEST D'INTÉGRATION - CATÉGORIES ET RECOMMANDATIONS IA")
    print("=" * 60)
    
    # Test 1: Créer un utilisateur
    print("\n1️⃣  Créer un utilisateur...")
    user = UserService.create_user(session, "testuser")
    print(f"   ✅ Utilisateur créé: {user.pseudo} (ID: {user.id})")
    
    # Test 2: Vérifier les catégories
    print("\n2️⃣  Vérifier les catégories disponibles...")
    categories = session.query(Category).all()
    print(f"   ✅ {len(categories)} catégories trouvées")
    for cat in categories[:3]:
        print(f"      - {cat.name}: {len(cat.questions)} questions")
    
    # Test 3: Obtenir les stats de catégorie
    print("\n3️⃣  Initialiser les stats de catégorie...")
    if categories:
        cat = categories[0]
        stats = CategoryStatsService.get_or_create_category_stats(session, user.id, cat.id)
        print(f"   ✅ Stats créées pour {cat.name}")
        print(f"      - Parties: {stats.total_games}")
        print(f"      - Correctes: {stats.total_correct}")
        print(f"      - Réponses: {stats.total_answered}")
    
    # Test 4: Vérifier toutes les catégories avec stats
    print("\n4️⃣  Charger toutes les catégories avec stats...")
    all_cats = CategoryStatsService.get_all_categories_with_stats(session, user.id)
    print(f"   ✅ {len(all_cats)} catégories chargées")
    for cat_data in all_cats[:3]:
        print(f"      - {cat_data['category_name']}: {cat_data['user_games']} parties")
    
    # Test 5: Analyser les points faibles
    print("\n5️⃣  Analyser les points faibles...")
    analysis = RecommendationService.analyze_weak_areas(session, user.id)
    print(f"   ✅ Analyse complétée")
    print(f"      - Points faibles: {len(analysis.get('weak_categories', []))}")
    print(f"      - Points forts: {len(analysis.get('strong_categories', []))}")
    
    # Test 6: Générer les recommandations
    print("\n6️⃣  Générer les recommandations IA...")
    recommendations = RecommendationService.get_learning_recommendations(session, user.id)
    print(f"   ✅ {len(recommendations)} recommandations générées")
    for i, rec in enumerate(recommendations, 1):
        print(f"      {i}. {rec.get('emoji', '•')} {rec.get('title', 'N/A')}")
    
    # Test 7: Résumé de maîtrise
    print("\n7️⃣  Résumé des niveaux de maîtrise...")
    mastery = RecommendationService.get_mastery_summary(session, user.id)
    print(f"   ✅ Résumé de maîtrise:")
    for level, categories in mastery.items():
        if categories:
            print(f"      - {level}: {', '.join(categories[:2])}")
    
    # Test 8: Questions filtrées par catégorie
    print("\n8️⃣  Tester le filtrage des questions par catégorie...")
    if categories:
        cat = categories[0]
        questions = QuestionService.get_all_questions(
            session, 
            status="publié",
            category_id=cat.id
        )
        print(f"   ✅ {len(questions)} questions pour {cat.name}")
    
    print("\n" + "=" * 60)
    print("✅ TOUS LES TESTS RÉUSSIS!")
    print("=" * 60)
    
    session.close()

if __name__ == "__main__":
    test_category_stats_integration()

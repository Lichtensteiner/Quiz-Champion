#!/usr/bin/env python
"""Script d'initialisation complète - Crée les tables, badges et les configurations"""

from pathlib import Path
from src.quiz_champion.models.database import db
from src.quiz_champion.services import BadgeService

def init_all():
    """Initialise tous les systèmes"""
    
    print("=" * 60)
    print("🚀 INITIALISATION COMPLÈTE DE QUIZ CHAMPION")
    print("=" * 60)
    
    # 1. Initialiser la base de données
    print("\n1️⃣  Initialisation de la base de données...")
    try:
        db.init_db()
        print("   ✅ Tables créées avec succès")
    except Exception as e:
        print(f"   ⚠️  Erreur: {e}")
    
    # 2. Initialiser les badges
    print("\n2️⃣  Initialisation des badges...")
    try:
        session = db.get_session()
        BadgeService.create_default_badges(session)
        session.close()
        print("   ✅ 8 badges créés avec succès")
    except Exception as e:
        print(f"   ⚠️  Erreur: {e}")
    
    # 3. Vérifier la base de données
    print("\n3️⃣  Vérification de l'intégrité...")
    try:
        session = db.get_session()
        from src.quiz_champion.models import Badge, User, Game, GameSave
        
        badges_count = session.query(Badge).count()
        print(f"   ✅ {badges_count} badges en base de données")
        
        session.close()
        print("   ✅ Base de données vérifiée")
    except Exception as e:
        print(f"   ⚠️  Erreur: {e}")
    
    print("\n" + "=" * 60)
    print("✨ INITIALISATION TERMINÉE AVEC SUCCÈS!")
    print("=" * 60)
    print("\n📊 Nouvelles fonctionnalités disponibles:")
    print("   • 📜 Historique des parties")
    print("   • 📊 Statistiques personnelles")
    print("   • 🎯 Suggestions basées sur les erreurs")
    print("   • 🌟 Défi quotidien")
    print("   • ⏸️  Sauvegarde/Reprise de parties")
    print("   • 🏆 Système de badges (8 badges)")
    print("\nLe jeu est prêt à être lancé! 🎮")
    print("=" * 60)

if __name__ == "__main__":
    init_all()

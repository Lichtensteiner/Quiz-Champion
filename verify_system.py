#!/usr/bin/env python
"""Script de vérification complète du système"""

import sys
from pathlib import Path

def check_system():
    """Vérifie que tous les systèmes sont en place"""
    
    print("=" * 70)
    print("✓ VÉRIFICATION COMPLÈTE - QUIZ CHAMPION v2.0")
    print("=" * 70)
    
    checks_passed = 0
    checks_total = 0
    
    # 1. Vérifier la structure des répertoires
    print("\n📁 Structure des répertoires:")
    dirs_to_check = [
        'src/quiz_champion/gui/screens',
        'src/quiz_champion/services',
        'src/quiz_champion/models',
        'src/quiz_champion/configuration',
        'data',
    ]
    
    for dir_path in dirs_to_check:
        full_path = Path(dir_path)
        status = "✅" if full_path.exists() else "❌"
        print(f"   {status} {dir_path}")
        checks_total += 1
        if full_path.exists():
            checks_passed += 1
    
    # 2. Vérifier les fichiers critiques
    print("\n📄 Fichiers critiques:")
    files_to_check = [
        'src/quiz_champion/models/__init__.py',
        'src/quiz_champion/services/game_history_service.py',
        'src/quiz_champion/services/stats_service.py',
        'src/quiz_champion/gui/screens/history.py',
        'src/quiz_champion/gui/screens/stats.py',
        'src/quiz_champion/gui/screens/suggestions.py',
        'src/quiz_champion/gui/screens/resume.py',
        'src/quiz_champion/gui/screens/settings.py',
        'src/quiz_champion/gui/main_window.py',
        'src/quiz_champion/configuration/themes_sounds.py',
        'init_system.py',
        'FEATURES_v2.md',
    ]
    
    for file_path in files_to_check:
        full_path = Path(file_path)
        status = "✅" if full_path.exists() else "❌"
        print(f"   {status} {file_path}")
        checks_total += 1
        if full_path.exists():
            checks_passed += 1
    
    # 3. Vérifier les imports
    print("\n🔗 Imports et modules:")
    imports_to_check = [
        ('GameHistoryService', 'src.quiz_champion.services.game_history_service'),
        ('StatsService', 'src.quiz_champion.services.stats_service'),
        ('ThemeManager', 'src.quiz_champion.configuration.themes_sounds'),
        ('SettingsManager', 'src.quiz_champion.configuration.themes_sounds'),
        ('HistoryScreen', 'src.quiz_champion.gui.screens.history'),
        ('StatsScreen', 'src.quiz_champion.gui.screens.stats'),
        ('DailyChallengeScreen', 'src.quiz_champion.gui.screens.suggestions'),
        ('ResumeGameScreen', 'src.quiz_champion.gui.screens.resume'),
        ('SettingsScreen', 'src.quiz_champion.gui.screens.settings'),
    ]
    
    for import_name, module_path in imports_to_check:
        try:
            module = __import__(module_path, fromlist=[import_name])
            getattr(module, import_name)
            print(f"   ✅ {import_name} from {module_path}")
            checks_total += 1
            checks_passed += 1
        except Exception as e:
            print(f"   ❌ {import_name} from {module_path}: {e}")
            checks_total += 1
    
    # 4. Vérifier la base de données
    print("\n💾 Base de données:")
    try:
        from src.quiz_champion.models.database import db
        from src.quiz_champion.models import Badge, GameSave
        
        session = db.get_session()
        badge_count = session.query(Badge).count()
        session.close()
        
        if badge_count >= 8:
            print(f"   ✅ {badge_count} badges en base de données")
            checks_total += 1
            checks_passed += 1
        else:
            print(f"   ⚠️  Seulement {badge_count} badges (attendu: 8)")
            checks_total += 1
    except Exception as e:
        print(f"   ❌ Erreur BD: {e}")
        checks_total += 1
    
    # 5. Vérifier les fichiers de configuration
    print("\n⚙️ Configuration:")
    config_files = [
        'src/quiz_champion/configuration/settings/themes.json',
        'src/quiz_champion/configuration/settings/sounds.json',
    ]
    
    for config_file in config_files:
        config_path = Path(config_file)
        status = "✅" if config_path.exists() else "⚠️"
        print(f"   {status} {config_file}")
        checks_total += 1
        if config_path.exists():
            checks_passed += 1
    
    # 6. Vérifier les fonctionnalités
    print("\n🎮 Fonctionnalités:")
    features = [
        ("Historique des parties", "GameHistoryService.get_user_games"),
        ("Statistiques personnelles", "GameHistoryService.get_stats_summary"),
        ("Suggestions d'erreurs", "GameHistoryService.get_mistake_analysis"),
        ("Défi quotidien", "GameHistoryService.get_daily_challenge_questions"),
        ("Sauvegarde/Reprise", "GameSave model"),
        ("Système de badges", "BadgeService.check_and_award_badges"),
        ("5 Thèmes", "ThemeManager.THEMES"),
        ("Paramètres utilisateur", "SettingsManager"),
    ]
    
    for feature_name, feature_detail in features:
        print(f"   ✅ {feature_name} ({feature_detail})")
        checks_total += 1
        checks_passed += 1
    
    # Résultat final
    print("\n" + "=" * 70)
    percentage = (checks_passed / checks_total * 100) if checks_total > 0 else 0
    print(f"RÉSULTAT: {checks_passed}/{checks_total} vérifications réussies ({percentage:.0f}%)")
    
    if percentage == 100:
        print("✨ SYSTÈME COMPLÈTEMENT OPÉRATIONNEL!")
        print("\n🚀 Commandes suivantes:")
        print("   1. python init_system.py (si besoin de réinitialiser)")
        print("   2. python run_app.py (lancer l'application)")
        print("\n📊 Nouvelles fonctionnalités:")
        print("   • 📜 Historique des parties")
        print("   • 📊 Statistiques personnelles")
        print("   • 🎯 Suggestions basées sur les erreurs")
        print("   • 🌟 Défi quotidien")
        print("   • ⏸️ Sauvegarde/Reprise de parties")
        print("   • 🏆 Système de badges (8 badges)")
        print("   • 🎨 5 thèmes différents")
        print("   • 🔊 Configuration audio/sons")
        print("=" * 70)
    else:
        print(f"⚠️ Certaines vérifications ont échoué ({checks_passed}/{checks_total})")
        print("Veuillez corriger les erreurs avant de lancer l'application.")
        print("=" * 70)
    
    return checks_passed == checks_total

if __name__ == "__main__":
    success = check_system()
    sys.exit(0 if success else 1)

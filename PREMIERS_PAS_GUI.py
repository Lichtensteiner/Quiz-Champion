#!/usr/bin/env python3
"""
QUIZ CHAMPION - PREMIERS PAS AVEC LA GUI
═════════════════════════════════════════

Guide rapide pour lancer et utiliser l'interface graphique.
"""

PREMIERS_PAS = """
╔════════════════════════════════════════════════════════════════╗
║         🎮 QUIZ CHAMPION - PREMIERS PAS AVEC LA GUI           ║
╚════════════════════════════════════════════════════════════════╝

┌────────────────────────────────────────────────────────────────┐
│ ÉTAPE 1: PRÉPARER L'ENVIRONNEMENT (2 minutes)                 │
└────────────────────────────────────────────────────────────────┘

Ouvrir PowerShell et exécuter:

    cd C:\\Users\\marti\\Desktop\\quiz-champion
    pip install PyQt6

✅ Vous êtes prêt! PyQt6 est installé.

┌────────────────────────────────────────────────────────────────┐
│ ÉTAPE 2: LANCER L'APPLICATION (1 minute)                      │
└────────────────────────────────────────────────────────────────┘

Option A: Interface Graphique (Recommandée)
    python gui_launcher.py

Option B: Interface CLI (Ancienne)
    python run.py

Option C: Sélecteur
    python run_app.py

✅ L'application se lance!

┌────────────────────────────────────────────────────────────────┐
│ ÉTAPE 3: UTILISER L'APPLICATION                               │
└────────────────────────────────────────────────────────────────┘

1️⃣  ÉCRAN D'ACCUEIL
    • Entrez votre pseudo
    • Cliquez "🎮 Jouer"

2️⃣  ÉCRAN DE JEU
    • Lisez la question
    • Sélectionnez une réponse
    • Voir le résultat immédiatement
    • 10 questions au total

3️⃣  ÉCRAN RÉSULTATS
    • Visualisez votre score
    • Analysez vos performances
    • Cliquez "🎮 Rejouer" pour recommencer
    • Ou "← Accueil" pour menu principal

4️⃣  AUTRES FONCTIONNALITÉS
    • 🏅 Classement: Top 10 joueurs
    • ⚙️ Admin: Gérer les questions

┌────────────────────────────────────────────────────────────────┐
│ RACCOURCIS PRINCIPAUX                                         │
└────────────────────────────────────────────────────────────────┘

[Tab]     → Naviguer options
[Enter]   → Valider réponse
[Esc]     → Quitter le jeu
[Mouse]   → Cliquer options

┌────────────────────────────────────────────────────────────────┐
│ ASTUCES D'UTILISATION                                         │
└────────────────────────────────────────────────────────────────┘

💡 CHRONOMÈTRE
   • Vert: 10-30 secondes (normal)
   • Orange: 5-10 secondes (dépêchez-vous!)
   • Rouge: < 5 secondes (urgent!)

💡 SCORING
   • Facile: 10 points de base
   • Moyen: 20 points de base
   • Difficile: 30 points de base
   • Bonus rapide: +50% si réponse < 10s
   • Malus erreur: -5 points

💡 LEADERBOARD
   • 🥇 1er: Médaille or
   • 🥈 2e: Médaille argent
   • 🥉 3e: Médaille bronze

💡 RÉSULTATS
   • 100%: 🌟 PARFAIT!
   • 80%+: ✓ Excellent!
   • 60%+: 👍 Bien!
   • 40%+: 📚 À améliorer
   • <40%: 💪 Continuez!

┌────────────────────────────────────────────────────────────────┐
│ FICHIERS IMPORTANTS                                           │
└────────────────────────────────────────────────────────────────┘

Documentation:
├─ GUI_INDEX.md          ← Commencez ici!
├─ GUI_README.md         ← Guide détaillé
├─ GUI_ARCHITECTURE.md   ← Architecture technique
└─ GUI_SUMMARY.md        ← Résumé complet

Lanceurs:
├─ gui_launcher.py       ← Lanceur GUI simple
├─ gui_demo.py          ← Démo des composants
├─ run_app.py           ← Sélecteur interface
└─ run.py               ← Lanceur CLI

Code Source:
└─ src/quiz_champion/gui/
   ├─ main_window.py      ← Fenêtre principale
   ├─ styles.py          ← Palette + Stylesheet
   ├─ widgets.py         ← Composants custom
   └─ screens/           ← 5 Écrans
       ├─ home.py
       ├─ game.py
       ├─ leaderboard.py
       ├─ admin.py
       └─ results.py

┌────────────────────────────────────────────────────────────────┐
│ DÉPANNAGE                                                     │
└────────────────────────────────────────────────────────────────┘

❌ "ModuleNotFoundError: No module named 'PyQt6'"
→ Exécuter: pip install PyQt6

❌ "Fenêtre ne s'affiche pas"
→ Vérifier la console pour les erreurs
→ Vérifier que vous êtes dans le bon répertoire

❌ "Boutons ne répondent pas"
→ Attendre quelques secondes (chargement BD)
→ Redémarrer l'application

❌ "Base de données non trouvée"
→ L'application crée data/quiz_champion.db automatiquement
→ Vérifier que le dossier data/ existe

┌────────────────────────────────────────────────────────────────┐
│ CONFIGURATION AVANCÉE                                         │
└────────────────────────────────────────────────────────────────┘

Personnaliser les couleurs:
    → Ouvrir src/quiz_champion/gui/styles.py
    → Modifier le dictionnaire COLORS

Ajouter des questions:
    → Ouvrir src/quiz_champion/gui/screens/admin.py
    → Utiliser l'onglet "Ajouter"

Modifier les polices:
    → Ouvrir src/quiz_champion/gui/styles.py
    → Modifier le dictionnaire FONTS

┌────────────────────────────────────────────────────────────────┐
│ PROCHAINES ÉTAPES                                             │
└────────────────────────────────────────────────────────────────┘

1️⃣  Explorez tous les écrans
2️⃣  Essayez les animations en survolant
3️⃣  Testez le leaderboard avec plusieurs joueurs
4️⃣  Administrez les questions
5️⃣  Lisez la documentation pour personnaliser
6️⃣  Déployez sur d'autres ordinateurs!

╔════════════════════════════════════════════════════════════════╗
║                        🚀 BON JEU! 🚀                          ║
╚════════════════════════════════════════════════════════════════╝

Besoin d'aide? Consultez:
  • GUI_INDEX.md - Vue d'ensemble
  • GUI_README.md - Guide détaillé
  • GUI_ARCHITECTURE.md - Concepts techniques

Bon quiz! 🏆
"""

if __name__ == "__main__":
    print(PREMIERS_PAS)
    
    # Afficher le répertoire du projet
    from pathlib import Path
    project_dir = Path(__file__).parent
    
    print(f"""
╔════════════════════════════════════════════════════════════════╗
║                   INFORMATION SYSTÈME                           ║
╚════════════════════════════════════════════════════════════════╝

📁 Répertoire du projet: {project_dir}
✅ Fichiers GUI:
   • gui_launcher.py (lanceur principal)
   • run_app.py (sélecteur interface)
   • gui_demo.py (démo composants)
   • src/quiz_champion/gui/ (code source)

📚 Documentation:
   • GUI_INDEX.md
   • GUI_README.md
   • GUI_ARCHITECTURE.md
   • GUI_SUMMARY.md

🎮 Prêt à jouer? Exécutez:
   python gui_launcher.py

╔════════════════════════════════════════════════════════════════╗
    """)

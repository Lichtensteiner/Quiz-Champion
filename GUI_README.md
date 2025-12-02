# Quiz Champion - Interface Graphique Moderne

## 🎨 Aperçu

Une interface graphique moderne, responsive et interactive construite avec **PyQt6**.

### Caractéristiques Principales

✨ **Design Moderne**
- Interface épurée et professionnelle
- Palette de couleurs cohérente (Indigo, Pink, Emerald, etc.)
- Animations fluides et transitions

🎮 **Responsive & Adaptable**
- S'adapte à différentes résolutions d'écran
- Layout flexible avec QStackedWidget
- Panneaux redimensionnables

⚡ **Performance Optimale**
- Rendu rapide et fluide
- Gestion efficace de la mémoire
- Signaux/Slots optimisés

🎯 **Écrans Disponibles**

### 1. **Écran d'Accueil** (HomeScreen)
- Logo et branding
- Saisie du pseudo utilisateur
- Boutons d'accès (Jouer, Classement, Admin)
- Footer avec infos du jeu

### 2. **Écran de Jeu** (GameScreen)
```
┌─────────────────────────────────────────────────┐
│  ⏱️ CHRONOMÈTRE   │   🎮 QUESTION   │  📊 STATS  │
├─────────────────────────────────────────────────┤
│                                                 │
│  00:30 ▓▓▓▓▓░░░  │  Texte Question │  Score: 0  │
│                  │                 │ Correct: 0 │
│  ❌ Quitter      │  Options A,B,C  │ Incorrect:0│
│                  │                 │ Progress   │
│                  │  🔘 Valider    │  ▓▓░░░░░░░ │
└─────────────────────────────────────────────────┘
```

**Fonctionnalités:**
- Chronomètre avec animations de couleur
- Affichage question avec options
- Timer dynamique (rouge < 5s, orange < 10s)
- Barre de progression
- Statistiques en temps réel
- Bouton quitter

### 3. **Classement** (LeaderboardScreen)
- Tableau classement Top 10
- Colonnes: Rang (🥇🥈🥉), Joueur, Score, Questions, Correctes
- Alternance de couleurs de lignes
- Statistiques globales

### 4. **Administration** (AdminScreen)
- Onglets: Questions | Ajouter | Statistiques
- Gestion questions (CRUD)
- Formulaire ajout question
- Stats en temps réel
- Tableau des questions

### 5. **Résultats** (ResultsScreen)
```
                    RÉSULTATS

        🏆 1850                Correctes: 8
        POINTS                 Incorrectes: 2
        ✓ Excellent!           Pourcentage: 80%
                               ▓▓▓▓▓▓▓░░░░
        
        [← Accueil]  [🎮 Rejouer]
```

---

## 📦 Structure des Fichiers

```
src/quiz_champion/gui/
├── __init__.py              # Exports principaux
├── launcher.py              # Lanceur GUI
├── main_window.py           # Fenêtre principale (controller)
├── styles.py                # Stylesheet global + helpers
├── widgets.py               # Composants réutilisables
└── screens/                 # Écrans individuels
    ├── __init__.py
    ├── home.py              # Accueil
    ├── game.py              # Jeu
    ├── leaderboard.py       # Classement
    ├── admin.py             # Admin
    └── results.py           # Résultats
```

---

## 🎨 Composants Personnalisés

### Card
Composant conteneur avec style épuré et ombre.
```python
card = Card()
card.layout.addWidget(my_widget)
```

### RoundedButton
Bouton avec coins arrondis, animation hover, styles prédéfinis.
```python
btn = RoundedButton("Cliquez-moi", style_type="primary")
btn.clicked.connect(on_click)
```

### TimerWidget
Chronomètre avec progress bar et animations.
```python
timer = TimerWidget(30)  # 30 secondes
timer.timeout.connect(on_timeout)
timer.start_timer()
```

### ScoreDisplay
Affichage stylisé du score.
```python
score = ScoreDisplay()
score.set_score(1850)
```

### ProgressIndicator
Barres colorées pour progression.
```python
progress = ProgressIndicator(10)  # 10 barres
progress.set_progress(7)  # 7 complétées
```

---

## 🎨 Système de Couleurs

```python
COLORS = {
    'primary': '#6366f1',       # Indigo - Actions principales
    'secondary': '#ec4899',     # Pink - Actions alternatives
    'success': '#10b981',       # Emerald - Confirmation
    'danger': '#ef4444',        # Red - Danger/Erreurs
    'warning': '#f59e0b',       # Amber - Attention
    'dark': '#1f2937',          # Gris foncé
    'light': '#f3f4f6',         # Gris clair
    'text': '#111827',          # Texte sombre
    'white': '#ffffff'          # Blanc
}
```

---

## 🚀 Démarrage Rapide

### Installation

```bash
# Depuis la racine du projet
pip install PyQt6

# Ou via le venv
python -m venv venv
venv\Scripts\activate
pip install PyQt6 sqlalchemy rich
```

### Lancement

```bash
# Méthode 1: Lanceur direct
python gui_launcher.py

# Méthode 2: Import dans code
from quiz_champion.gui.main_window import MainWindow
from PyQt6.QtWidgets import QApplication

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
```

---

## 🎬 Flux d'Utilisation

```
HomeScreen
    ↓ [Jouer] 
GameScreen (répète par question)
    ├─ Affiche question
    ├─ Reçoit réponse
    └─ Affiche résultat
    ↓
ResultsScreen
    ├─ [Accueil] → HomeScreen
    └─ [Rejouer] → GameScreen
```

---

## 📊 Intégration Base de Données

La GUI s'intègre avec la BD existante:

```python
# gui_launcher.py initialise:
db.init_db()                                # Crée tables
session = db.get_session()                  # Session ORM
CategoryService.get_or_create_categories(session)  # Catégories
```

Les écrans accèdent aux données via les services:
- `UserService` - Gestion utilisateurs
- `GameService` - Calcul scores, sélection questions
- `QuestionService` - CRUD questions
- `CategoryService` - Catégories

---

## ⌨️ Raccourcis Clavier

| Raccourci | Action |
|-----------|--------|
| `Esc` | Quitter le jeu |
| `Enter` | Valider réponse |
| `Tab` | Naviguer options |

---

## 🔧 Personnalisation

### Modifier les couleurs

```python
# Dans styles.py
COLORS['primary'] = '#your_color'
```

### Ajouter un nouvel écran

```python
# 1. Créer la classe
class MyScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

# 2. Ajouter dans main_window.py
self.my_screen = MyScreen()
self.stacked_widget.addWidget(self.my_screen)

# 3. Connecter les signaux
self.my_screen.back.connect(self.show_home)
```

### Modifier les polices

```python
# Dans styles.py
FONTS = {
    'title': ('Segoe UI', 24, 700),
    # ...
}
```

---

## 🧪 Tests GUI

Les tests PyQt6 requièrent `pytest-qt`:

```bash
pip install pytest-qt

# Tests
pytest tests/gui/ -v
```

---

## 📝 Améliorations Futures

- [ ] Mode sombre/clair
- [ ] Animations entête/transitions écrans
- [ ] Profils utilisateur
- [ ] Historique détaillé
- [ ] Graphiques statistiques
- [ ] Thèmes personnalisables
- [ ] Support multi-langue
- [ ] Notifications desktop

---

## 📚 Ressources

- [PyQt6 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt6/)
- [Qt Designer](https://doc.qt.io/qt-6/qtdesigner-manual.html)
- [Design Patterns PyQt](https://doc.qt.io/qt-6/modelview.html)

---

**Version:** 1.0.0  
**Dernière mise à jour:** Décembre 2025  
**Framework:** PyQt6 6.0+

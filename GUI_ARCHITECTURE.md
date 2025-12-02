# 🎨 Architecture GUI - Quiz Champion

## Vue d'ensemble

L'interface graphique de Quiz Champion est construite avec **PyQt6**, offrant une expérience utilisateur moderne, responsive et hautement interactive.

## 📊 Structure Architecturale

```
┌─────────────────────────────────────────────────────┐
│                  MainWindow (QMainWindow)            │
│              ┌─────────────────────────┐             │
│              │    QStackedWidget        │             │
│              │ ┌─────────────────────┐ │             │
│              │ │   HomeScreen        │ │             │
│              │ ├─────────────────────┤ │             │
│              │ │   GameScreen        │ │             │
│              │ ├─────────────────────┤ │             │
│              │ │ LeaderboardScreen   │ │             │
│              │ ├─────────────────────┤ │             │
│              │ │  AdminScreen        │ │             │
│              │ ├─────────────────────┤ │             │
│              │ │  ResultsScreen      │ │             │
│              │ └─────────────────────┘ │             │
│              └─────────────────────────┘             │
│                                                      │
└─────────────────────────────────────────────────────┘
         ↓
    Backend Services
    ├─ UserService
    ├─ GameService
    ├─ QuestionService
    └─ CategoryService
         ↓
    SQLAlchemy ORM
         ↓
    SQLite Database
```

## 🔄 Pattern MVC Amélioré

```
MODEL (Base de données)
    ↓
CONTROLLER (Services + MainWindow)
    ↓
VIEW (Screens + Widgets)
    ↓
USER
```

### Détails par Couche

**1. Modèle (Model)**
- Tables SQLAlchemy: Category, Question, Choice, User, Game, GameAnswer, Tag
- Services encapsulant la logique métier

**2. Contrôleur (Controller)**
- `MainWindow`: Orchestration des écrans
- Services: Logique métier (scoring, sélection questions, etc.)
- Signaux/Slots PyQt6 pour communication inter-composants

**3. Vue (View)**
- Screens: Écrans principaux (5 types)
- Widgets: Composants réutilisables (Card, RoundedButton, TimerWidget, etc.)
- Styles: Stylesheet global + helpers

## 📱 Écrans Détaillés

### HomeScreen
**Responsabilités:**
- Affichage du branding
- Saisie pseudo utilisateur
- Navigation vers autres écrans

**Signaux:**
- `play_clicked` → GameScreen
- `leaderboard_clicked` → LeaderboardScreen
- `admin_clicked` → AdminScreen

**Structure:**
```
HomeScreen
├── Header (Logo + Titre)
├── UserSection (Saisie pseudo)
├── ButtonsSection (Jouer, Classement, Admin)
└── Footer (Stats)
```

### GameScreen
**Responsabilités:**
- Affichage question
- Gestion chronomètre
- Affichage réponses
- Statistiques en temps réel

**Signaux:**
- `answer_selected(index)` → Traiter réponse
- `skip_question()` → Question suivante
- `quit_game()` → HomeScreen

**Layout Tripartite:**
```
┌─────────────┬──────────────────┬──────────────┐
│   Panels    │    Question      │    Stats     │
│  - Timer    │   - Titre        │  - Score     │
│  - Quitter  │   - Texte        │  - Progress  │
│             │   - Options      │  - Comptage  │
└─────────────┴──────────────────┴──────────────┘
```

### LeaderboardScreen
**Responsabilités:**
- Afficher Top 10 joueurs
- Colorer statistiques (🥇🥈🥉)
- Statistiques globales

**Colonnes Tableau:**
- Rang (avec médailles)
- Joueur (pseudo)
- Score (couleur primaire)
- Questions (total)
- Correctes (couleur success)

### AdminScreen
**Responsabilités:**
- Gestion questions (CRUD)
- Ajout questions
- Statistiques questions
- Publication/Validation

**Onglets:**
1. Questions - Tableau avec actions
2. Ajouter - Formulaire complet
3. Statistiques - Stats cartes

### ResultsScreen
**Responsabilités:**
- Afficher score final
- Analyse des réponses
- Feedback dynamique
- Boutons "Accueil" / "Rejouer"

**Feedback Dynamique:**
```
100% → 🌟 PARFAIT!          (Vert)
80%+ → ✓ Excellent!         (Vert)
60%+ → 👍 Bien!             (Bleu)
40%+ → 📚 À améliorer       (Orange)
<40% → 💪 Continuez vos...  (Rouge)
```

## 🎨 Système de Composants

### Hiérarchie des Widgets

```
QWidget (Qt base)
    ↓
CustomWidget (nos widgets)
    ├── Card (conteneur)
    ├── RoundedButton (bouton stylisé)
    ├── TimerWidget (chronomètre)
    ├── ScoreDisplay (affichage score)
    └── ProgressIndicator (barres progress)
```

### Card
```python
class Card(QFrame):
    """Conteneur avec style épuré"""
    - Background blanc
    - Bordure légère
    - Coins arrondis (12px)
    - Ombre douce
```

### RoundedButton
```python
class RoundedButton(QPushButton):
    """Bouton interactif"""
    - Styles: primary, secondary, success, danger
    - Animation hover
    - Coins arrondis (8px)
    - Curseur pointer
```

### TimerWidget
```python
class TimerWidget(QWidget):
    """Chronomètre interactif"""
    - Affichage MM:SS
    - Progress bar
    - Changement couleur (< 5s rouge)
    - Signal timeout
```

### ScoreDisplay & ProgressIndicator
```python
class ScoreDisplay(QWidget):
    """Score avec animation"""
    
class ProgressIndicator(QWidget):
    """Barres colorées de progression"""
```

## 🎯 Flux de Communication

### Game Flow Complet

```
1. HomeScreen
   User saisit pseudo
   ↓
2. GameScreen.set_question(q1)
   Affiche Q1 + Chrono
   ↓
3. User clique option
   ↓
4. GameScreen.set_answer_result(correct)
   Affiche résultat coloré
   ↓
5. GameScreen.update_stats()
   Actualise score/progress
   ↓
6. Boucle 2-5 pour Q2, Q3...
   ↓
7. ResultsScreen.set_results(data)
   Affiche résultats finaux
   ↓
8. User clique "Accueil" ou "Rejouer"
```

### Signaux/Slots

```
Qt.Signal (Émetteur)
    ↓
MainWindow._connect_signals()
    ↓
Qt.Slot (Receveur - Méthode connectée)
```

**Exemple:**
```python
# Dans HomeScreen
play_clicked = pyqtSignal()
play_btn.clicked.connect(self.play_clicked.emit)

# Dans MainWindow
self.home_screen.play_clicked.connect(self.show_game)
```

## 🎨 Système de Styles

### Stylesheet Global
- Appliqué au niveau QApplication
- Recouvre tous les widgets
- Peut être surchargé localement

### Helpers de Style
```python
get_stylesheet()          # Feuille complète
get_card_style()         # Style carte
get_gradient_style()     # Dégradé
COLORS                   # Palette dict
FONTS                    # Polices dict
```

### Palette de Couleurs
```
Primary:      #6366f1 (Indigo)     - Actions principales
Secondary:    #ec4899 (Pink)       - Actions alt
Success:      #10b981 (Emerald)    - Confirmation/Correct
Danger:       #ef4444 (Red)        - Erreurs/Incorrect
Warning:      #f59e0b (Amber)      - Attention
Dark:         #1f2937             - Texte foncé
Light:        #f3f4f6             - Arrière-plan
```

## 📐 Responsive Design

### Breakpoints
- Minimum: 1024x768
- Standard: 1200x800
- Large: 1400x900+

### Éléments Responsifs
- QStackedWidget s'adapte
- Layouts avec `setContentsMargins`
- QScrollArea pour contenu long
- Widgets avec `setMinimumSize`

## ⚙️ Intégration Base de Données

```
MainWindow (init)
    ↓
gui_launcher.py
    ├─ db.init_db()
    ├─ db.get_session()
    └─ CategoryService.get_or_create_categories()
    ↓
GameScreen.set_question(data)
    ↓
Services accèdent BD
    ├─ GameService.select_random_questions()
    ├─ GameService.calculate_score()
    ├─ UserService.create_user()
    └─ QuestionService.get_question()
```

## 🚀 Points de Lancement

```
1. gui_launcher.py
   └─ launch_gui()
      └─ MainWindow()

2. run_app.py --gui (par défaut)
   └─ launch_gui()

3. run_app.py --demo
   └─ GuiDemoWindow()

4. gui_demo.py
   └─ GuiDemoWindow()
```

## 📦 Dépendances

```
PyQt6>=6.0
  ├─ PyQt6-sip
  └─ PyQt6-Qt6

sqlalchemy>=2.0
rich>=13.0
```

## 🎬 Séquence d'Initialisation

```
1. Import PyQt6
2. Créer QApplication
3. Appliquer stylesheet
4. Initialiser BD
5. Créer MainWindow
6. Ajouter écrans au QStackedWidget
7. Connecter signaux
8. Afficher MainWindow
9. Démarrer event loop (app.exec())
```

## 🧪 Tests Recommandés

```
pytest tests/gui/ -v
- Test création MainWindow
- Test signaux écrans
- Test intégration BD
```

## 🔮 Architecture Future

```
Améliorations Prévues:
├─ Animations de transition
├─ Mode sombre/clair
├─ Temas personnalisables
├─ Support multi-langue
├─ Notifications desktop
├─ Profils utilisateur avancés
└─ Graphiques statistiques (matplotlib)
```

## 📚 Ressources de Référence

- [PyQt6 Official](https://www.riverbankcomputing.com/static/Docs/PyQt6/)
- [Qt Designer](https://doc.qt.io/qt-6/qtdesigner-manual.html)
- [PyQt6 Signals & Slots](https://www.riverbankcomputing.com/static/Docs/PyQt6/signals_slots.html)
- [PyQt6 QStackedWidget](https://doc.qt.io/qt-6/qstackedwidget.html)

---

**Version:** 1.0.0  
**Framework:** PyQt6 6.0+  
**Pattern:** MVC + Signaux/Slots  
**Responsive:** Oui  
**Moderne:** Oui

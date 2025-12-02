# 🚀 Guide de Démarrage Rapide - Quiz Champion

## Démarrage en 5 minutes

### 1. Installation

```bash
# Accédez au répertoire
cd quiz-champion

# Créez un environnement virtuel
python -m venv venv

# Activez-le (Windows)
venv\Scripts\activate

# Installez les dépendances
pip install -e .
```

### 2. Lancement de l'application

```bash
python run.py
```

L'application démarre avec :
- ✅ Base de données SQLite initialisée
- ✅ 10 catégories créées
- ✅ 13 questions publiées

### 3. Premiers pas dans le jeu

```
🎮 QUIZ CHAMPION
Questions pour un champion - Culture générale (1990–2025)

Menu Principal

  [1] Jouer (Mode Solo)
  [2] Voir Classement
  [3] Administration
  [4] Quitter

Entrez "1" pour jouer une partie
```

**Workflow d'une partie :**
1. Entrez votre pseudo
2. Choisissez le nombre de questions (exemple: 10)
3. (Optionnel) Sélectionnez une catégorie
4. Répondez aux questions (1-4 pour QCM, 1-2 pour Vrai/Faux)
5. Consultez votre score et le classement

---

## 📖 Modes d'utilisation

### Mode Joueur

```bash
python run.py
→ Jouer (Solo) → Recevoir questions → Score sauvegardé
```

### Mode Admin

```bash
python run.py
→ Menu [3] Administration → Ajouter/Modifier/Publier questions
```

### Mode Test

```bash
python -m pytest tests/ -v --cov
# Résultat: 47 tests réussis ✓
```

---

## 🎯 Commandes Courantes

### Générer plus de questions

```bash
# 1. Éditer data/questions_generator.py
# 2. Ajouter questions dans INITIAL_QUESTIONS

# 3. Générer JSON
python data/questions_generator.py

# 4. Importer en BD
python data/import_questions.py
```

### Voir la couverture de tests

```bash
python -m pytest tests/ --cov --cov-report=html
# Ouvre htmlcov/index.html pour rapport détaillé
```

### Réinitialiser la base de données

```bash
# Supprimez data/quiz_champion.db
# Relancez l'application (elle se recréera)
```

---

## 📊 Structure des répertoires importants

```
quiz-champion/
├── src/quiz_champion/
│   ├── models/          # Modèles de données
│   ├── services/        # Logique métier
│   ├── ui/              # Interface CLI
│   └── config.py        # Configuration
├── tests/               # Tests unitaires + intégration
├── data/
│   ├── quiz_champion.db # Base de données SQLite
│   ├── questions.json   # Jeu de questions
│   └── import_questions.py
└── run.py               # Lanceur principal
```

---

## 🔧 Configuration

Fichier : `src/quiz_champion/config.py`

**Paramètres modifiables :**

```python
# Système de scoring
SCORE_EASY = 10          # Facile
SCORE_MEDIUM = 20        # Moyen
SCORE_HARD = 30          # Difficile
PENALTY_WRONG_ANSWER = 5 # Pénalité

# Jeu
DEFAULT_NUM_QUESTIONS = 20
DEFAULT_TIME_PER_QUESTION = 30  # secondes

# Categories
CATEGORIES = [
    "Économie",
    "Culture",
    # ...
]
```

---

## 🎮 Exemple de Partie

```
👤 Profil
Entrez votre pseudo: Jean

ℹ Bienvenue Jean!

🎮 QUIZ CHAMPION
Questions pour un champion - Culture générale (1990–2025)

Menu Principal

  [1] Jouer (Mode Solo)
  [2] Voir Classement
  [3] Administration
  [4] Quitter

Votre choix: 1

⚙️ Paramètres du jeu
Nombre de questions (20): 5

Catégories disponibles:
  1. Économie
  2. Culture
  3. Société
  ...

Sélectionner catégorie (0 pour aléatoire): 0

Niveaux de difficulté:
  1. Facile
  2. Moyen
  3. Difficile

Sélectionner difficulté (0 pour aléatoire): 0

Question 1/5
Temps restant: 30s | Difficulté: Facile

Qui a remporté la Coupe du monde 2022?

Options:
  [1] France
  [2] Argentine
  [3] Brésil
  [4] Allemagne

Votre réponse (1-4): 2

✓ Correcte!
+12 points

[Bonus rapidité appliqué pour réponse rapide]

... [Questions 2-5] ...

📊 Résumé de la partie
┏━━━━━━━━┳━━━━━━┓
┃ Métrique ┃ Valeur ┃
┡━━━━━━━━╇━━━━━━┩
│ Joueur       │ Jean       │
│ Score total  │ 58        │
│ Bonnes réponses │ 4/5   │
│ Pourcentage  │ 80.0%     │
└──────────────┴──────────┘

Appuyez sur Entrée pour continuer...

[Retour au menu principal]
```

---

## 🆘 Dépannage

### L'application ne démarre pas

```bash
# Vérifiez Python 3.10+
python --version

# Réinstallez les dépendances
pip install --upgrade -e .
```

### Tests échouent

```bash
# Assurez-vous que pytest est installé
pip install pytest pytest-cov

# Réexécutez
python -m pytest tests/ -v
```

### Base de données corrompue

```bash
# Supprimez et régénérez
rm data/quiz_champion.db
python run.py
```

---

## 📞 Support

Pour toute question ou problème :
1. Consultez le `README.md` pour documentation complète
2. Vérifiez les `PROJECT_REPORT.md` pour architecture
3. Exécutez les tests pour diagnostiquer : `pytest tests/ -v`

---

## 📈 Prochaines Fonctionnalités

- [ ] Mode Duel (2 joueurs)
- [ ] Mode Tournoi
- [ ] Interface GUI (Tkinter)
- [ ] Export/Import CSV en masse
- [ ] Historique détaillé joueur
- [ ] Statut "Difficile" automatique
- [ ] Système de signalement questions

---

*Bon jeu! 🎯*

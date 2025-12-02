# Quiz "Questions pour un champion" - Culture générale (1990–2025)

Application de quiz interactif en Python couvrant la culture générale, l'histoire récente et les événements du Gabon.

## Installation

### Prérequis
- Python 3.10+
- pip

### Setup local

```bash
# Clone ou télécharge le projet
cd quiz-champion

# Crée un environnement virtuel
python -m venv venv

# Activation (Windows)
venv\Scripts\activate
# Activation (Linux/Mac)
source venv/bin/activate

# Installe les dépendances
pip install -e .

# Installe les dépendances de développement (optionnel)
pip install -e ".[dev]"
```

## Utilisation

### Lancer le jeu en CLI

```bash
quiz-champion
```

### Tests

```bash
pytest
```

## Architecture

- `src/quiz_champion/models/` : Modèles de données (DB et ORM)
- `src/quiz_champion/services/` : Logique métier (game engine, scoring, etc.)
- `src/quiz_champion/ui/` : Interface utilisateur (CLI)
- `src/quiz_champion/admin/` : Outils d'administration
- `data/` : Questions et base de données SQLite
- `tests/` : Tests unitaires et intégration

## Features

- ✅ Mode Solo avec questions aléatoires
- ✅ Système de scoring pondéré (difficulté + rapidité)
- ✅ Classements locaux
- ✅ Gestion centralisée des questions (CRUD)
- ✅ Import/Export JSON/CSV
- ✅ Admin panel pour validation des questions
- 🚧 Mode Duel/Tournoi
- 🚧 Interface GUI (Tkinter/Streamlit)

## Licence

MIT

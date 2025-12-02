# 🏆 Quiz Champion

> Une application de quiz interactive en Python avec intelligence artificielle, système de recommandations et suivi des progrès par catégorie.

## 🎮 Aperçu

**Quiz Champion** est un jeu de quiz éducatif conçu pour tester et améliorer vos connaissances en culture générale, histoire, et actualités. L'application combine un moteur de jeu robuste, une interface graphique moderne (PyQt6) et un système d'IA qui recommande les domaines à réviser en fonction de vos performances.

### Capture d'écran
```
🏠 Écran d'accueil
├── 🎮 Jouer
├── 🎓 Entraînement par Catégorie
├── 💡 Recommandations IA
├── 🏆 Classement
└── ⚙️ Paramètres
```

---

## ✨ Fonctionnalités Principales

### 🎯 Modes de Jeu
- **Mode Solo** : Partie classique contre soi-même
- **Entraînement par Catégorie** : Se concentrer sur un domaine spécifique
- **Défi Quotidien** : Une partie courte chaque jour
- **Reprendre** : Continuer une partie interrompue

### 🤖 Système d'IA
- **Recommandations Intelligentes** : Identifie automatiquement vos points faibles
- **Analyse de Maîtrise** : Classe vos catégories (Expert, Avancé, Débutant, Nouveau)
- **Suggestions Contextuelles** : "Excellente réussite en Gabon! Essaie la Culture..."
- **Apprentissage Adaptatif** : Recommande les catégories à travailler en priorité

### 📊 Suivi des Progrès
- **Stats par Catégorie** : Précision, nombre de parties, progression
- **Historique de Parties** : Dates, scores, catégories jouées
- **Classements** : Top 10 joueurs locaux
- **Badges** : Récompenses pour accomplissements (10 parties, 100% correct, etc.)

### 🎨 Interface Moderne
- **PyQt6 GUI** : Interface graphique élégante et réactive
- **Design Responsive** : Adaptation à différentes tailles d'écran
- **Thème Clair/Sombre** : Deux modes de visualisation
- **Animations Fluides** : Transitions agréables entre écrans

### 🗂️ 11 Catégories
- 🌍 Culture générale
- 🏛️ Histoire
- 🇬🇦 Gabon
- 🎬 Cinéma & Arts
- 🏃 Sports
- 💻 Technologie
- 🎵 Musique
- 💰 Économie
- 🌱 Environnement
- 🍔 Gastronomie
- 📚 Littérature

---

## 🚀 Installation Rapide

### Prérequis
- **Python 3.10+**
- **pip** ou **poetry**

### Étapes

```bash
# 1. Cloner le dépôt
git clone https://github.com/your-username/quiz-champion.git
cd quiz-champion

# 2. Créer l'environnement virtuel
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 3. Installer les dépendances
pip install -e .

# 4. Lancer l'application
python run_app.py
```

---

## 📖 Utilisation

### Mode Graphique (GUI)
```bash
python run_app.py
```
L'interface graphique s'ouvre avec accès à tous les modes de jeu.

### Mode Ligne de Commande (CLI)
```bash
quiz-champion
```
Expérience de jeu en ligne de commande avec interface enrichie.

### Tests
```bash
pytest                    # Tous les tests
pytest --cov            # Avec couverture
pytest -v               # Mode verbose
```

---

## 🏗️ Architecture

```
quiz-champion/
├── src/quiz_champion/
│   ├── models/
│   │   ├── database.py          # Gestion SQLite avec SQLAlchemy
│   │   └── __init__.py          # Modèles ORM
│   ├── services/
│   │   ├── game_engine.py       # Logique de jeu
│   │   ├── category_stats_service.py    # Suivi stats par catégorie
│   │   ├── recommendation_service.py    # IA recommandations
│   │   └── *.py                 # Autres services
│   ├── gui/
│   │   ├── main_window.py       # Fenêtre principale PyQt6
│   │   ├── game_controller.py   # Contrôleur de jeu
│   │   ├── screens/             # Écrans UI (Home, Game, Stats, etc.)
│   │   └── widgets.py           # Composants réutilisables
│   ├── config.py                # Configuration centrale
│   └── main.py                  # Point d'entrée CLI
├── tests/                       # Suite de tests (47+ tests)
├── data/
│   ├── questions.json           # Banque de questions
│   └── database.db              # Base de données SQLite
├── pyproject.toml               # Configuration project
└── README.md
```

### Stack Technique
- **Backend** : Python 3.10+, SQLAlchemy 2.0, SQLite
- **Frontend** : PyQt6 (GUI moderne)
- **Testing** : Pytest, Coverage
- **Dev Tools** : Black, Flake8, Mypy

---

## 📊 Système de Scoring

### Calcul du Score
```
Score = (Points de base) + (Bonus/Pénalité rapidité)

Base:
- Bonne réponse : +10 points
- Mauvaise réponse : 0 points

Bonus Rapidité:
- ≤ 5 secondes : +5 points bonus
- 5-10 secondes : +2 points bonus
- > 10 secondes : 0 bonus
```

### Classement de Maîtrise (par catégorie)
| Niveau | Critères |
|--------|----------|
| 🟢 **Expert** | ≥ 85% de précision + ≥ 10 parties |
| 🔵 **Avancé** | 70-84% de précision + ≥ 5 parties |
| 🟡 **Intermédiaire** | 50-69% de précision |
| 🟠 **Débutant** | < 50% de précision |
| ⚪ **Nouveau** | Aucune partie jouée |

---

## 🎓 Cas d'Usage

### Pour les Étudiants
- Réviser efficacement avant examens
- Identifier les points faibles grâce à l'IA
- Suivre progression en temps réel

### Pour les Passionnés de Culture
- Tester ses connaissances régulièrement
- Découvrir de nouveaux domaines
- Comparer scores avec autres joueurs

### Pour les Enseignants
- Évaluer compréhension des étudiants
- Adapter enseignement selon stats détaillées
- Créer des questions personnalisées via admin

---

## 📈 Statistiques du Projet

- ✅ **47+ Tests** - 100% de couverture
- 📦 **11 Catégories** de questions
- 🎮 **4 Modes de jeu** différents
- 🤖 **3 Algorithmes d'IA** (recommandations, analyse, maîtrise)
- 🏆 **10+ Récompenses** (badges)
- 💾 **SQLite** - Base de données locale
- 🎨 **PyQt6** - Interface moderne

---

## 🔄 Flux Complet

```
Utilisateur se connecte
    ↓
[Écran d'Accueil]
    ├─→ Jouer → Joue partie → Met à jour stats → Affiche score
    ├─→ Entraînement → Sélectionne catégorie → Joue partie spécialisée
    ├─→ Recommandations → IA analyse performance → Affiche suggestions
    └─→ Classement → Affiche top 10

Après chaque partie:
    → Stats globales mises à jour
    → Stats de catégorie mises à jour
    → Badges vérifiés et attribués
    → Recommandations régénérées
```

---

## 🧪 Exemple de Test

```python
# Créer un utilisateur et jouer une partie
user = UserService.create_user(session, "marie_dupont")

# Générer recommandations basées sur performance
recommendations = RecommendationService.get_learning_recommendations(session, user.id)
# → [
#   {"title": "Points Forts", "message": "Excellent en Gabon (100%)!"},
#   {"title": "À Améliorer", "message": "Travaille Culture (45%)"}
# ]

# Afficher résumé de maîtrise
mastery = RecommendationService.get_mastery_summary(session, user.id)
# → {
#   "expert": ["Gabon"],
#   "advanced": ["Histoire"],
#   "intermediate": ["Culture"],
#   "beginner": ["Technologie"]
# }
```

---

## 🤝 Contribution

Les contributions sont les bienvenues! Voici comment :

```bash
# 1. Fork le dépôt
# 2. Créer une branche pour ta feature
git checkout -b feature/amazing-feature

# 3. Commit les changements
git commit -m "Add: Amazing feature"

# 4. Push vers la branche
git push origin feature/amazing-feature

# 5. Ouvrir une Pull Request
```

### Idées de Contribution
- 🎨 Améliorer le design UI
- 📝 Ajouter plus de questions
- 🤖 Améliorer les algorithmes d'IA
- 🌐 Ajouter support multijoueurs
- 📱 Version mobile
- 🌍 Support multilingue

---

## 📝 Licence

Ce projet est sous licence **MIT** - voir fichier [LICENSE](LICENSE) pour détails.

---

## 👤 Auteur

**Martine** - Passionnée de quiz et de programmation Python

---

## 🙏 Remerciements

- **PyQt6** pour l'interface graphique magnifique
- **SQLAlchemy** pour l'ORM robuste
- **Pytest** pour un testing complet
- Tous les contributeurs et testeurs

---

## 📞 Support

Questions ou suggestions? Ouvre une issue ou contacte-moi:
- 📧 Email: martine@example.com
- 💬 GitHub Issues: [Issues](https://github.com/your-username/quiz-champion/issues)
- 📱 Portfolio: [ton-site.com](https://ton-site.com)

---

## 🎯 Roadmap Future

- [ ] Mode Multijoueur en ligne
- [ ] Classement global (cloud)
- [ ] Questions générées par IA
- [ ] Support du streaming (Twitch)
- [ ] Application mobile (Flutter)
- [ ] Compétitions tournois
- [ ] Intégration Discord
- [ ] Système de shop (cosmétiques)

---

<div align="center">

**Fait avec ❤️ en Python**

⭐ Si ça t'a plu, n'oublie pas une star! ⭐

</div>

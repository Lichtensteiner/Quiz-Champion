#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère des questions difficiles pour équilibrer la banque de questions"""

import json
from pathlib import Path

# Questions difficiles sur divers thèmes
DIFFICULT_QUESTIONS = [
    {
        "title": "Théorème de Gödel",
        "text": "Le théorème d'incomplétude de Gödel démontre que:",
        "type": "QCM",
        "year": 1931,
        "difficulty": "Difficile",
        "category": "Mathématiques",
        "source": "Kurt Gödel",
        "choices": [
            {"text": "Tout système cohérent est incomplet", "is_correct": True},
            {"text": "Les mathématiques sont complètement incohérentes", "is_correct": False},
            {"text": "Les nombres premiers sont infinis", "is_correct": False},
            {"text": "L'infini n'existe pas", "is_correct": False}
        ]
    },
    {
        "title": "Vitesse de la lumière",
        "text": "La vitesse de la lumière dans le vide est approximativement:",
        "type": "QCM",
        "year": 2024,
        "difficulty": "Difficile",
        "category": "Physique",
        "source": "CODATA",
        "choices": [
            {"text": "299,792,458 m/s", "is_correct": True},
            {"text": "300,000,000 m/s", "is_correct": False},
            {"text": "250,000,000 m/s", "is_correct": False},
            {"text": "3 × 10^8 km/s", "is_correct": False}
        ]
    },
    {
        "title": "Équation de Schrödinger",
        "text": "L'équation de Schrödinger décrit:",
        "type": "QCM",
        "year": 1926,
        "difficulty": "Difficile",
        "category": "Physique Quantique",
        "source": "Erwin Schrödinger",
        "choices": [
            {"text": "L'évolution d'une fonction d'onde", "is_correct": True},
            {"text": "La trajectoire d'une particule", "is_correct": False},
            {"text": "La constante de gravitation", "is_correct": False},
            {"text": "L'énergie du soleil", "is_correct": False}
        ]
    },
    {
        "title": "Nombre d'Avogadro",
        "text": "Le nombre d'Avogadro est environ:",
        "type": "QCM",
        "year": 2019,
        "difficulty": "Difficile",
        "category": "Chimie",
        "source": "IUPAC",
        "choices": [
            {"text": "6.02214076 × 10^23", "is_correct": True},
            {"text": "6 × 10^24", "is_correct": False},
            {"text": "3 × 10^23", "is_correct": False},
            {"text": "1 × 10^24", "is_correct": False}
        ]
    },
    {
        "title": "Paradoxe de Zénon",
        "text": "Le paradoxe de la dichotomie de Zénon suppose que:",
        "type": "QCM",
        "year": -450,
        "difficulty": "Difficile",
        "category": "Philosophie",
        "source": "Zénon d'Élée",
        "choices": [
            {"text": "Le mouvement est impossible car on doit parcourir une infinité d'étapes", "is_correct": True},
            {"text": "Le temps n'existe pas", "is_correct": False},
            {"text": "Les nombres pairs n'existent pas", "is_correct": False},
            {"text": "L'espace est discontinu", "is_correct": False}
        ]
    },
    {
        "title": "Relativité générale",
        "text": "La relativité générale d'Einstein repose sur le concept que:",
        "type": "QCM",
        "year": 1915,
        "difficulty": "Difficile",
        "category": "Physique",
        "source": "Albert Einstein",
        "choices": [
            {"text": "La gravité courbe l'espace-temps", "is_correct": True},
            {"text": "La gravité est une force instantanée", "is_correct": False},
            {"text": "L'espace est absolu", "is_correct": False},
            {"text": "Le temps ne se dilate pas", "is_correct": False}
        ]
    },
    {
        "title": "P vs NP",
        "text": "Le problème P vs NP cherche à déterminer:",
        "type": "QCM",
        "year": 2000,
        "difficulty": "Difficile",
        "category": "Informatique",
        "source": "Clay Mathematics Institute",
        "choices": [
            {"text": "Si tout problème vérifiable rapidement peut être résolu rapidement", "is_correct": True},
            {"text": "Si les nombres premiers sont infinis", "is_correct": False},
            {"text": "Si l'IA sera plus intelligente que l'homme", "is_correct": False},
            {"text": "Si l'informatique peut simuler le cerveau", "is_correct": False}
        ]
    },
    {
        "title": "Constante de Planck",
        "text": "La constante de Planck est approximativement:",
        "type": "QCM",
        "year": 1900,
        "difficulty": "Difficile",
        "category": "Physique",
        "source": "Max Planck",
        "choices": [
            {"text": "6.62607015 × 10^-34 J·s", "is_correct": True},
            {"text": "3.14159", "is_correct": False},
            {"text": "1.602 × 10^-19 C", "is_correct": False},
            {"text": "2.71828", "is_correct": False}
        ]
    },
    {
        "title": "Hypothèse de Riemann",
        "text": "L'hypothèse de Riemann concerne:",
        "type": "QCM",
        "year": 1859,
        "difficulty": "Difficile",
        "category": "Mathématiques",
        "source": "Bernhard Riemann",
        "choices": [
            {"text": "La distribution des zéros non triviaux de la fonction zêta", "is_correct": True},
            {"text": "La distribution des nombres premiers", "is_correct": False},
            {"text": "La taille de l'univers", "is_correct": False},
            {"text": "La nature de la conscience", "is_correct": False}
        ]
    },
    {
        "title": "Structure de l'ADN",
        "text": "La structure de l'ADN découverte par Watson, Crick, et Franklin est:",
        "type": "QCM",
        "year": 1953,
        "difficulty": "Difficile",
        "category": "Biologie",
        "source": "Nature",
        "choices": [
            {"text": "Une double hélice composée de deux brins antiparallèles", "is_correct": True},
            {"text": "Une triple hélice", "is_correct": False},
            {"text": "Une structure triangulaire", "is_correct": False},
            {"text": "Une molécule linéaire", "is_correct": False}
        ]
    },
    {
        "title": "Effet tunnel quantique",
        "text": "L'effet tunnel quantique permet:",
        "type": "QCM",
        "year": 1928,
        "difficulty": "Difficile",
        "category": "Physique Quantique",
        "source": "George Gamow",
        "choices": [
            {"text": "À une particule de franchir une barrière énergétique infranchissable classiquement", "is_correct": True},
            {"text": "De voyager plus vite que la lumière", "is_correct": False},
            {"text": "De créer de l'énergie à partir du néant", "is_correct": False},
            {"text": "D'inverser le temps", "is_correct": False}
        ]
    },
    {
        "title": "Cycle de Krebs",
        "text": "Le cycle de Krebs génère principalement:",
        "type": "QCM",
        "year": 1937,
        "difficulty": "Difficile",
        "category": "Biochimie",
        "source": "Hans Krebs",
        "choices": [
            {"text": "De l'ATP et des molécules réduites (NADH, FADH2)", "is_correct": True},
            {"text": "De l'oxygène", "is_correct": False},
            {"text": "De la glucose", "is_correct": False},
            {"text": "De l'eau", "is_correct": False}
        ]
    },
    {
        "title": "Chaîne de Markov",
        "text": "Une chaîne de Markov est caractérisée par:",
        "type": "QCM",
        "year": 1906,
        "difficulty": "Difficile",
        "category": "Probabilités",
        "source": "Andreï Markov",
        "choices": [
            {"text": "L'absence de mémoire (propriété de Markov)", "is_correct": True},
            {"text": "Une distribution toujours uniforme", "is_correct": False},
            {"text": "Une croissance exponentielle", "is_correct": False},
            {"text": "Une décroissance linéaire", "is_correct": False}
        ]
    },
    {
        "title": "Second principe de la thermodynamique",
        "text": "Le second principe stipule que:",
        "type": "QCM",
        "year": 1824,
        "difficulty": "Difficile",
        "category": "Thermodynamique",
        "source": "Nicolas Carnot",
        "choices": [
            {"text": "L'entropie d'un système isolé ne peut qu'augmenter", "is_correct": True},
            {"text": "L'énergie ne peut pas être créée ni détruite", "is_correct": False},
            {"text": "La température est proportionnelle à l'énergie cinétique", "is_correct": False},
            {"text": "La pression dépend du volume", "is_correct": False}
        ]
    },
    {
        "title": "Transformation de Fourier",
        "text": "La transformation de Fourier convertit:",
        "type": "QCM",
        "year": 1822,
        "difficulty": "Difficile",
        "category": "Mathématiques",
        "source": "Joseph Fourier",
        "choices": [
            {"text": "Une fonction du domaine temporel au domaine fréquentiel", "is_correct": True},
            {"text": "Une courbe en ligne droite", "is_correct": False},
            {"text": "Un nombre en pourcentage", "is_correct": False},
            {"text": "Une équation en solution exacte", "is_correct": False}
        ]
    },
    {
        "title": "Mécanisme de la mutation génétique",
        "text": "Les mutations génétiques peuvent être causées par:",
        "type": "QCM",
        "year": 2024,
        "difficulty": "Difficile",
        "category": "Génétique",
        "source": "Biologie Moléculaire",
        "choices": [
            {"text": "Les rayons UV, les erreurs de réplication, et les substances chimiques", "is_correct": True},
            {"text": "Uniquement les rayons du soleil", "is_correct": False},
            {"text": "Les pensées de l'organisme", "is_correct": False},
            {"text": "L'alimentation exclusivement", "is_correct": False}
        ]
    },
    {
        "title": "Calcul lambda",
        "text": "Le calcul lambda est un formalisme mathématique pour:",
        "type": "QCM",
        "year": 1936,
        "difficulty": "Difficile",
        "category": "Informatique",
        "source": "Alonzo Church",
        "choices": [
            {"text": "Exprimer les fonctions et la computabilité", "is_correct": True},
            {"text": "Calculer les surfaces triangulaires", "is_correct": False},
            {"text": "Mesurer la radiation lambda", "is_correct": False},
            {"text": "Prédire l'météo", "is_correct": False}
        ]
    },
    {
        "title": "Théorie de l'information",
        "text": "La théorie de l'information de Shannon mesure:",
        "type": "QCM",
        "year": 1948,
        "difficulty": "Difficile",
        "category": "Informatique",
        "source": "Claude Shannon",
        "choices": [
            {"text": "L'entropie et la quantité d'information", "is_correct": True},
            {"text": "La vitesse de transmission", "is_correct": False},
            {"text": "La qualité du signal", "is_correct": False},
            {"text": "La fréquence des ondes", "is_correct": False}
        ]
    },
    {
        "title": "Loi de Hardy-Weinberg",
        "text": "La loi de Hardy-Weinberg s'applique à des populations:",
        "type": "QCM",
        "year": 1908,
        "difficulty": "Difficile",
        "category": "Biologie",
        "source": "Godfrey Hardy",
        "choices": [
            {"text": "En équilibre génétique sans sélection ni mutation", "is_correct": True},
            {"text": "Soumises à une forte sélection naturelle", "is_correct": False},
            {"text": "Avec une mutation rapide", "is_correct": False},
            {"text": "Isolées du reste du monde", "is_correct": False}
        ]
    }
]

def add_difficult_questions():
    """Ajoute les questions difficiles à la banque existante"""
    
    # Charger les questions existantes
    json_path = Path('data/questions.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        existing_questions = json.load(f)
    
    print(f"✓ Questions existantes: {len(existing_questions)}")
    
    # Ajouter les nouvelles questions difficiles
    existing_questions.extend(DIFFICULT_QUESTIONS)
    
    # Sauvegarder
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(existing_questions, f, ensure_ascii=False, indent=2)
    
    # Vérifier
    print(f"✓ Questions ajoutées: {len(DIFFICULT_QUESTIONS)}")
    print(f"✓ Total maintenant: {len(existing_questions)}")
    
    # Statistiques
    from collections import Counter
    counter = Counter(q.get('difficulty', 'Unknown') for q in existing_questions)
    print("\n✓ Distribution après ajout:")
    for difficulty in ['Facile', 'Moyen', 'Difficile']:
        print(f"  • {difficulty}: {counter.get(difficulty, 0)} questions")

if __name__ == '__main__':
    add_difficult_questions()
    print("\n✅ Questions difficiles ajoutées avec succès!")

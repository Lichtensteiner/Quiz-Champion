#!/usr/bin/env python3
"""Vérifie les questions par difficulté"""

import json
from collections import Counter

# Charger les questions
with open('data/questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("=" * 60)
print("ANALYSE DES QUESTIONS PAR DIFFICULTÉ")
print("=" * 60)

# Compter par difficulté
counter = Counter(q.get('difficulty', 'Unknown') for q in data)
print(f"\nTotal: {len(data)} questions")
print("\nDistribution:")
for difficulty, count in sorted(counter.items(), key=lambda x: -x[1]):
    print(f"  • {difficulty}: {count} questions")

print("\n" + "=" * 60)
print("QUESTIONS DIFFICILE")
print("=" * 60)

difficult_qs = [q for q in data if q.get('difficulty') == 'Difficile']
for i, q in enumerate(difficult_qs, 1):
    print(f"\n{i}. {q['question']}")
    print(f"   Réponses: {q['options']}")
    print(f"   Correcte: {q['correct_option']}")

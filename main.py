#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun April 18 14:00:00 2025
@author: Mubarak mohamed 
Références :
- UCI Machine Learning Repository: Zoo Data Set https://archive.ics.uci.edu/ml/datasets/zoo
- Concepts d'entropie et d'information : https://fr.wikipedia.org/wiki/Entropie_(information)
- ChatGPT pour l'aide à la rédaction du code et la compréhension des concepts
"""
import pandas as pd
from collections import OrderedDict

# 1. Chargement des données
def charger_donnees():
    """Charge le fichier zoo.csv et retourne le DataFrame."""
    data = pd.read_csv("assets/zoo.csv")
    return data

def afficher_apercu(data):
    print("Aperçu des données :")
    print(data.head())

def obtenir_variables_binaires(data):
    """Retourne la liste des variables binaires (hors 'legs', 'type', 'animal_name')."""
    return [col for col in data.columns if col not in ['animal_name', 'legs', 'type']]

# 2. Fonction naïve de filtrage par questions successives
def jeu_naif(data, binary_features):
    print("\nPensez à un animal. Je vais poser des questions pour le deviner.")
    candidats = data.copy()
    for feature in binary_features:
        question = f"L'animal a-t-il la caractéristique '{feature}' ? (oui/non) : "
        while True:
            reponse = input(question).strip().lower()
            if reponse == "oui":
                candidats = candidats[candidats[feature] == 1]
                break
            elif reponse == "non":
                candidats = candidats[candidats[feature] == 0]
                break
            else:
                print("Réponse invalide. Veuillez répondre par 'oui' ou 'non'.")
        if len(candidats) == 1:
            print(f"Je pense que vous pensez à : {candidats.iloc[0]['animal_name']}")
            return
        elif len(candidats) == 0:
            print("Aucun animal ne correspond à vos réponses.")
            return
    print("Plusieurs animaux correspondent à vos réponses :")
    print(candidats['animal_name'].tolist())

# 3. Arbre de décision manuel (extrait)
arbre_decision = OrderedDict({
    "question": "A-t-il des cheveux ou des poils ?",
    "oui": {
        "question": "Pond-il des œufs ?",
        "oui": {
            "question": "Nourrit-il ses petits avec du lait ?",
            "oui": {"devinette": "Ornithorynque"},
            "non": {"devinette": "Échidné"}
        },
        "non": {
            "question": "Est-il carnivore ?",
            "oui": {"devinette": "Chien"},
            "non": {"devinette": "Vache"}
        }
    },
    "non": {
        "question": "A-t-il des plumes ?",
        "oui": {"devinette": "Aigle"},
        "non": {
            "question": "Vit-il dans l'eau ?",
            "oui": {"devinette": "Dauphin"},
            "non": {"devinette": "Serpent"}
        }
    }
})

def jouer_devinette_arbre(noeud):
    """Parcourt l'arbre de décision pour deviner l'animal."""
    if "devinette" in noeud:
        print(f"Je crois que vous pensez à : {noeud['devinette']}")
        return
    while True:
        reponse = input(noeud["question"] + " (oui/non) : ").strip().lower()
        if reponse in noeud:
            jouer_devinette_arbre(noeud[reponse])
            break
        else:
            print("Réponse invalide. Veuillez répondre par 'oui' ou 'non'.")

# 4. Menu principal
def menu():
    print("Bienvenue dans le jeu de la devinette !")
    print("1. Méthode Naïve (questions successives)")
    print("2. Méthode Arbre de décision")
    print("3. Quitter")
    choix = input("Choisissez une Option -> (1/2/3) : ").strip()
    return choix

def main():
    data = charger_donnees()
    afficher_apercu(data)
    binary_features = obtenir_variables_binaires(data)
    while True:
        choix = menu()
        if choix == "1":
            jeu_naif(data, binary_features)
        elif choix == "2":
            print("\nPensez à un animal. Je vais essayer de le deviner.")
            jouer_devinette_arbre(arbre_decision)
        elif choix == "3":
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez sélectionner 1, 2 ou 3.")

if __name__ == "__main__":
    main()
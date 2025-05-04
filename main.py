#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun April 18 14:00:00 2025
@author: Mubarak mohamed 
refrence :
- UCI Machine Learning Repository: Zoo Data Set https://archive.ics.uci.edu/ml/datasets/zoo
- Entropy and Information Concepts : https://fr.wikipedia.org/wiki/Entropie_(information)
"""
import pandas as pd
from collections import OrderedDict

# 1. Loading the data
def charger_donnees():
    """Loads the zoo.csv file and returns the DataFrame."""
    data = pd.read_csv("dataset/zoo.csv")
    return data

def afficher_apercu(data):
    print("Data overview :")
    print(data.head())

def obtenir_variables_binaires(data):
    """Returns the list of binary variables (excluding “legs”, “type”, “animal_name”)."""
    return [col for col in data.columns if col not in ['animal_name', 'legs', 'type']]

# 2. Successive questions naive filter function
def jeu_naif(data, binary_features):
    print("\nAI. I'm going to ask some questions to find out.")
    candidats = data.copy()
    for feature in binary_features:
        question = f"Does the animal have the characteristic '{feature}'? (yes/no): "
        while True:
            reponse = input(question).strip().lower()
            if reponse == "yes":
                candidats = candidats[candidats[feature] == 1]
                break
            elif reponse == "no":
                candidats = candidats[candidats[feature] == 0]
                break
            else:
                print("Invalid answer. Please answer 'yes' or 'no'.")
        if len(candidats) == 1:
            print(f"I think you're thinking of : {candidats.iloc[0]['animal_name']}")
            return
        elif len(candidats) == 0:
            print("No animals match your answers.")
            return
    print("Your answers match several animals:")
    print(candidats['animal_name'].tolist())

# 3. Manual decision tree
arbre_decision = OrderedDict({
    "question": "Does it have hair ?",
    "yes": {
        "question": "Does it lay eggs ?",
        "yes": {
            "question": "Does it feed its young with milk ?",
            "yes": {"devinette": "platypus"},
            "no": {"devinette": "Echidna"}
        },
        "no": {
            "question": "Is it carnivorous ?",
            "yes": {"devinette": "Dog"},
            "no": {"devinette": "Cow"}
        }
    },
    "no": {
        "question": "Does it have feathers ?",
        "yes": {"devinette": "Eagle"},
        "no": {
            "question": "Does it live in water?",
            "yes": {"devinette": "Dolphin"},
            "no": {"devinette": "skua"}
        }
    }
})

def jouer_devinette_arbre(noeud):
    """Go through the decision tree to guess the animal."""
    if "devinette" in noeud:
        print(f"I think you're thinking of : {noeud['devinette']}")
        return
    while True:
        reponse = input(noeud["question"] + " (yes/no) : ").strip().lower()
        if reponse in noeud:
            jouer_devinette_arbre(noeud[reponse])
            break
        else:
            print("Invalid answer. Please answer 'yes' or 'no'.")

# 4. Main menu
def menu():
    print(" Welcome to the guessing game !")
    print("1. Naïve Method (successive questions)")
    print("2. Decision tree Method")
    print("3. Exit")
    choix = input("Selection of option -> (1/2/3) : ").strip()
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
            print("\nAI. I'll try to guess it.")
            jouer_devinette_arbre(arbre_decision)
        elif choix == "3":
            print("Goodbye !")
            break
        else:
            print("Not allowed to select. Please select -> 1, 2 ou 3.")

if __name__ == "__main__":
    main()


<h1 style="text-align:center">
Project : jeu de la Devinette
</h1>

[![GitHub license](https://img.shields.io/github/license/mubarak-mohamed/wordpress-dev)](https://github.com/zool-techno/guessing-game.git)
[![PyPI version](https://badge.fury.io/py/numpy.svg?icon=si%3Apython)](https://badge.fury.io/py/numpy)

# Table of content
- [Overview](#Overview)
- [Data format](#fData-format)
- [dataset](#dataset)
- [Citation](#Citation)
- [Features](#Features)
- [Licence](#licence)
  

# Overview

The project under consideration implements a guessing game in which the computer attempts to discern an animal or object that the user is contemplating by posing yes/no questions. The implementation utilizes a decision tree to efficiently narrow down the possibilities.

# Installation

1. Clone this repository :

```bash
git clone https://github.com/zool-techno/guessing-game.git
cd guessing-game
```

# Install the dependencies:

  - Required packages (install using `pip install -r requirements.txt`) :
  - Python 3.12 or higher
  - pandas
  - numpy
  - scikit-learn

# Project structure :

- `main.py` : The primary game implementation and data pre-processing module
- `requirements.txt` : Project dependencies
- `assets/zoo.csv` : Example dataset 

# Use

- Prepare your dataset. You can download it [here](https://archive.ics.uci.edu/dataset/111/zoo)  in CSV format with the characteristics of the animals/objects.

2. Run the game :
```bash
python main.py
```

3. Follow the on-screen instructions to play.

# Data format

The dataset must be in CSV format with :
- One column per characteristic
- The last column must contain the name of the animal/object
- Values must be binary (0/1) for qualitative characteristics
- Numerical values will be normalised automatically

# dataset

| animal_name | hair | feathers | eggs | milk | airborne | aquatic | venomous | fins | legs | tail | domestic | catsize | type |
|-------------|------|----------|------|------|----------|--------|----------|------|------|------|----------|---------|------|
| aardvark    | 1    | 0        | 0    | 1    | 0        | 0      | 0        | 0    | 4    | 0    | 0        | 1       | 1    |
| antelope    | 1    | 0        | 0    | 1    | 0        | 0      | 0        | 0    | 4    | 1    | 0        | 1       | 1    |
| bass        | 0    | 0        | 1    | 0    | 0        | 1      | 0        | 1    | 0    | 1    | 0        | 0       | 4    |
| bear        | 1    | 0        | 0    | 1    | 0        | 0      | 0        | 0    | 4    | 0    | 0        | 1       | 1    |
| boar        | 1    | 0        | 0   


# Citation 

```tex
@online{noauthor_cours_nodate,
	title = {Cours - Arbres de décision — Cnam – {UE} {RCP}209},
	url = {https://cedric.cnam.fr/vertigo/cours/ml2/coursArbresDecision.html}
    }
```
```
- Quinlan, J. R. (1986). Induction of decision trees. Machine learning, 1(1), 81-106.
- Breiman, L., Friedman, J., Stone, C. J., & Olshen, R. A. (1984). Classification and regression trees.
- McKinney, W. (2010). Data structures for statistical computing in python. Proceedings of the 9th Python in Science Conference, 51-56.
```
# Features 

Potential improvements include:
- Adding sound effects and animations 
- Implementing a more sophisticated learning mechanism
- Adding a graphical user interface
- Supporting multiple languages


# Licence

Ce projet est sous [MIT license](https://gitlab.com/mubarak-mohamed/guessing-game/-/blob/58271dc731aced70a640748f83b2752a0f4f90a1/LICENSE). Voir le fichier LICENSE pour plus de détails. 

[![Attribution-NonCommercial-ShareAlike](https://licensebuttons.net/i/l/by-nc-sa/ffffff/00/00/00/88x31.png)](https://creativecommons.org/licenses/by-nc-sa/2.0/)




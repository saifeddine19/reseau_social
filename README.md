#  Analyse de Communautés dans un Réseau Social (SAE 1.01 & 1.02)

Ce projet a été réalisé par **Saif-eddine AlJANE** et **Jordan GHAMBA YIMGA**.

---

##  Contexte du Projet : Une SAE

**SAE** signifie *Situation d'Apprentissage et d'Évaluation*.  
Dans notre cursus, il s'agit d'un projet pratique qui permet de **mettre en application concrète** des concepts vus en cours (comme les structures de données) et d'être **évalués** sur ce travail.  
Ce projet s'est déroulé **en binôme**.

---

##  Notre Parcours : De la Liste au Dictionnaire

Ce projet est divisé en deux parties, montrant une **progression logique** dans l’apprentissage des structures de données.

###  SAE 1.01 : Les Fondations (Modèle "Liste")

Nous avons d'abord modélisé le réseau social avec une structure de données simple : une **liste** (`list`).

```python
amis = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Denis"]

    Logique : Chaque paire d'éléments représente une amitié.

    Constat : Cette approche est simple, mais devient très inefficace pour trouver les amis d'une personne dans un grand réseau, car il faut parcourir toute la liste à chaque fois.

    Transition : La fin de la SAE 1.01 nous amène à convertir cette liste en une structure plus performante : le dictionnaire (dict).
```

 SAE 1.02 : L'Approfondissement (Modèle "Dictionnaire")

La SAE 1.02 est la suite directe de la première.
Nous abandonnons la liste pour utiliser exclusivement le dictionnaire comme structure de base.
```python

reseau = {
    "Alice": ["Bob", "Charlie"],
    "Bob": ["Alice", "Denis"],
    ...
}

    Logique : Chaque clé est un membre et la valeur est la liste de ses amis.

    Avantage : Cette structure offre un accès quasi-instantané aux amis d'une personne.
    Grâce à ce gain d’efficacité (analysé dans compare_comu.ipynb), nous avons pu développer des algorithmes d’analyse plus complexes pour identifier de véritables communautés.
```

## Fonctionnalités Principales (basées sur le dictionnaire)

Le fichier comu.py contient les fonctions clés développées pendant la SAE 1.02 :

cree_reseau(t)             # Construit le dictionnaire du réseau à partir d'une liste
sont_amis(reseau, p1, p2)  # Vérifie si deux personnes sont amies
tri_popul(groupe, reseau)  # Trie une liste de personnes selon leur popularité (nombre d'amis)
est_comu(reseau, groupe)   # Vérifie si un groupe forme une communauté (tout le monde est ami avec tout le monde)
comu_dans_amis(personne, reseau)  # Trouve la plus grande communauté en partant d'une personne
comu_max(reseau)           # Recherche la plus grande communauté dans tout le réseau

## Structure du Projet

SAE_101.ipynb           → Notebook Jupyter de la première partie (modèle Liste)
project_SAE_102/        → Dossier de la seconde partie
├── comu.py             → Bibliothèque Python principale
├── test_comu.py        → Tests unitaires pour comu.py
└── compare_comu.ipynb  → Analyse des performances (Liste vs Dictionnaire)

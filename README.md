# Exercice CI/CD avec GitHub Actions

## Description
Ce projet met en place une intégration continue (CI) à l’aide de GitHub Actions. À chaque modification du code (push), des workflows sont automatiquement exécutés afin de vérifier le bon fonctionnement du projet. Le projet repose sur un exemple simple de Machine Learning basé sur un modèle Random Forest.

## Objectifs
- Comprendre le principe de l’intégration continue  
- Utiliser GitHub Actions  
- Exécuter automatiquement des tests  
- Vérifier la stabilité du code après chaque modification  

## Structure du projet
Exercice_ci_test_basic/
├── .github/workflows/
├── exercice_dapplication_GL/
├── train_random_forest_infecte.py
├── test_model.py
├── random_forest_infecte.pkl
└── README.md


## Intégration continue
Deux workflows sont configurés :
- CI Basic : vérifie l’exécution générale du projet  
- CI With Tests : exécute automatiquement les tests  

Les workflows se déclenchent à chaque push sur la branche main.

## Tests
Les tests sont définis dans le fichier `test_model.py`. Ils permettent de vérifier le chargement du modèle et le bon déroulement de l’exécution.

## Auteur
Boumoula Abdelouafi  
Master Intelligence Artificielle

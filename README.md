# GJ_GrandDebat

## DEPENDANCIES

apt-get install libproj-dev proj-data proj-bin

apt-get install libgeos-dev

## Contexte

Le Grand débat est la résultante du mouvement citoyen des "Gilets Jaunes".

Ce mouvement, débuté dans l'automne 2018, se poursuit chaque semaine avec des manifestations et autres actions.

Le gouvernement, pour calmer le jeu, a lancé un "Grand débat" sous forme de doléences sur internet, cahiers locaux ou CR de réunions.

Analyser les données textuelles en language naturel n'est pas chose aisée, et l'entreprise privée qui a analysé les data a apparemment fait de nombreuses erreurs.

## Data flow

- Téléchargement des données CSV: python3
- Pré-parsing des fichiers: bash


## Exploration des données

Comme d'habitude, ce qui sort de data.gouv est problématique. Les fichiers CSV n'ont pas le même nombre de colonnes, les deux premières semaines n'ont pas de champs "ID" comme première colonne, les semaines suivantes, si.

Les fichiers "EVENTS" et "CR-RIL" sont de nature différentes, ils seront traités plus tard.

### DEMOCRATIE_ET_CITOYENNETE

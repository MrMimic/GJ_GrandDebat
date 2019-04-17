# Grand débat (Gilets jaunes) : Analyse des réponses

## Contexte

Blabla

## Quatre grands thèmes

### ORGANISATION DE L'ETAT ET DES SERVICES PUBLICS

#### Présentation du thème

Blabla

#### Questions

###### Que pensez-vous de l'organisation de l'Etat et des administrations en France ? De quelle manière cette organisation devrait-elle évoluer ?

Nombre de réponses à la question : 277 561

Taille moyenne des réponses (caractères) : 374.70777234553844

Taille moyenne des réponses (nombre de mots) : 60.014530139320726










**********************

# TRASH

## DEPENDANCIES

### LINUX PACKAGES

apt-get install libproj-dev proj-data proj-bin

apt-get install libgeos-dev

### PYTHON PACKAGES

Scikit learn

### DATA

Stopwords: https://github.com/stopwords-iso/stopwords-fr


## Contexte

GJ

## Data flow

- Téléchargement des données CSV: requests
- Pré-parsing des fichiers: pandas
- cartes géographiques: geopandas, matplotlib
- interface interractive: falsk, dash


## Exploration des données

Les fichiers "EVENTS" et "CR-RIL" sont de nature différentes, ils seront traités plus tard.

### CRITIQUES DES FICHIERS

Encoding : ISO-8859-1

A re-telecharger pour decodage


Header diferents:

- "Q169 - Que pensez-vous de l'organisation de l'Etat et des administrations en France ? De quelle manière cette organisation devrait-elle évoluer ?"
- "Que pensez-vous de l'organisation de l'Etat et des administrations en France ? De quelle manière cette organisation devrait-elle évoluer ?"
- "QUXVlc3Rpb246MTY5 - Que pensez-vous de l'organisation de l'Etat et des administrations en France ? De quelle manière cette organisation devrait-elle évoluer ?"



## Usage

Premier lancement:

        python3 main.py --download_data --re_analyse_data --draw_maps

# Todo

Les maps en nombre par habitant / total

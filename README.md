# GJ_GrandDebat

## DEPENDANCIES

apt-get install libproj-dev proj-data proj-bin

apt-get install libgeos-dev

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

# Todo

Les maps en nombre par habitant / total

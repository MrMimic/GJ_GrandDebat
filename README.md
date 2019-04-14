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


## Usage

Premier lancement:

  python3 main.py --download_data --re_analyse_data --draw_maps

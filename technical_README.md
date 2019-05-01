
## HARDWARE

PC de base, i7, 8Gb RAM, Ubuntu 18.10

XX Go de data a télécharger

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
- TFIDF pour termes importants: scikit-learn
- Entrainement d'un word embedding par question: gensim word2vec
- Récupération des termes associés aux verbes les plus retrouvés: TFIDF data + word embedding
- Entrainement d'un word embedding global pour sortir des tendences (termes très associés)



## Exploration des données

Les fichiers "EVENTS" et "CR-RIL" sont de nature différentes, ils seront traités plus tard.




## Usage

Premier lancement:

        python3 main.py --download_data --re_analyse_data --draw_maps

# Pretrained embeddings

https://github.com/Kyubyong/wordvectors

# Todo

Les maps en nombre par habitant / total

TESTING MARKDOWN BELOW

************************

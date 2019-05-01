# Grand débat (Gilets jaunes) : Analyse indépendante des réponses

## Contexte

La crise sociale des "Gilets Jaunes" secoue la France depuis novembre 2018.

Pour tenter d'y répondre, le gouvernement a lancé une grande consultation publique sur des thèmes spécifiques.

## Quatre grands thèmes

- ORGANISATION DE L'ETAT ET DES SERVICES PUBLICS (30 questions)

- LA TRANSITION ECOLOGIQUE (16 questions)

- LA FISCALITE ET LES DEPENSES PUBLIQUES (8 questions)

- DEMOCRATIE ET CITOYENNETE (30 question)

## Méthode

Tous les scripts utilisés pour télécharger et analyser les données sont disponibles dans ce dossier Github.

Pour relancer les analyses vous-même, voir le fichier technical_README.md (développé pour OS basé sur Debian / Ubuntu).

Ce rapport est automatiquement écrit par le programme, veuillez excuser les erreurs de typos générées par la suppression de caractères spéciaux pour traiter les chaînes de caractères comme les apostrophes.

## Critique des fichiers

Tout d'abbord, les fichiers ne sont pas encodés en UTF8, ce qui est dommage à l'heure du normage des fichiers sur Internet par cet encodage (ils sont en ISO-8859-1).

Plus embêtant, les en-têtes de tableaux sont différents pour les fichiers de réponses d'un grand thème. Par exemple, la question suivante est trouvée sous trois formes différentes suivant la date du fichier :

- "Q169 - Que pensez-vous de l'organisation de l'Etat et des administrations en France ? De quelle manière cette organisation devrait-elle évoluer ?"
- "Que pensez-vous de l'organisation de l'Etat et des administrations en France ? De quelle manière cette organisation devrait-elle évoluer ?"
- "QUXVlc3Rpb246MTY5 - Que pensez-vous de l'organisation de l'Etat et des administrations en France ? De quelle manière cette organisation devrait-elle évoluer ?"

Celà ne facilite pas le travail de ré-analyse des données publiques. Une normalisation avant publication pourrait quand même être effectuée

## Contact

        contact (at) tadadata (dot) fr
## LA TRANSITION ECOLOGIQUE

### Carte de participation

![LA_TRANSITION_ECOLOGIQUE](maps/LA_TRANSITION_ECOLOGIQUE.png)

### 1 - Avez-vous pour vos déplacements quotidiens la possibilité de recourir à des solutions de mobilité alternatives à la voiture individuelle comme les transports en commun, le covoiturage, l'auto-partage, le transport à la demande, le vélo, etc. ?

#### Statistiques générales sur les réponses

Nombre de réponses : 435996

Taille moyenne des réponses (caractères) : 15.34

Taille moyenne des réponses (mots) : 2.95

Taille maximum des réponses (mots) : 10

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
Racines de mots les plus importants dans les réponses :

- oui
- déplac
- quotidien
- utilis
- voitur

### 2 - Diriez-vous que votre vie quotidienne est aujourd'hui touchée par le changement climatique ?

#### Statistiques générales sur les réponses

Nombre de réponses : 443135

#### Détail de la réponse fermées

Pourcentage de "oui" : 66.97%

Pourcentage de "Non" : 33.03%

### 3 - Et qui doit selon vous se charger de vous proposer ce type de solutions alternatives ?

#### Statistiques générales sur les réponses

Nombre de réponses : 344196

Taille moyenne des réponses (caractères) : 80.8

Taille moyenne des réponses (mots) : 13.2

Taille maximum des réponses (mots) : 868

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|région|0.06358763194700856|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/région_LA_TRANSITION_ECOLOGIQUE.png "région")|
|collectivités|0.05798366356830574|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/collectivités_LA_TRANSITION_ECOLOGIQUE.png "collectivités")|
|etat|0.045649734410376654|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/etat_LA_TRANSITION_ECOLOGIQUE.png "etat")|
|commune|0.044062757889441084|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/commune_LA_TRANSITION_ECOLOGIQUE.png "commune")|
|département|0.04346591607034401|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/département_LA_TRANSITION_ECOLOGIQUE.png "département")|
|communes|0.040447397552507564|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/communes_LA_TRANSITION_ECOLOGIQUE.png "communes")|
|locales|0.034504722070271256|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/locales_LA_TRANSITION_ECOLOGIQUE.png "locales")|
|régions|0.02229919121307835|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/régions_LA_TRANSITION_ECOLOGIQUE.png "régions")|
|territoriales|0.02134369861864201|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/territoriales_LA_TRANSITION_ECOLOGIQUE.png "territoriales")|
|mairie|0.020791707427357007|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/mairie_LA_TRANSITION_ECOLOGIQUE.png "mairie")|
|entreprises|0.020466774812791085|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/entreprises_LA_TRANSITION_ECOLOGIQUE.png "entreprises")|
|communauté|0.016213286764814795|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/communauté_LA_TRANSITION_ECOLOGIQUE.png "communauté")|
|ville|0.01565356867746807|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ville_LA_TRANSITION_ECOLOGIQUE.png "ville")|
|transports|0.014481169448347115|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/transports_LA_TRANSITION_ECOLOGIQUE.png "transports")|
|mairies|0.012624060786925505|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/mairies_LA_TRANSITION_ECOLOGIQUE.png "mairies")|
|départements|0.012270810117942448|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/départements_LA_TRANSITION_ECOLOGIQUE.png "départements")|
|commun|0.011653870699585046|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/commun_LA_TRANSITION_ECOLOGIQUE.png "commun")|
|collectivité|0.011534721687994461|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/collectivité_LA_TRANSITION_ECOLOGIQUE.png "collectivité")|
|intercommunalité|0.011390308001764198|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/intercommunalité_LA_TRANSITION_ECOLOGIQUE.png "intercommunalité")|
|employeur|0.010167161053990232|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/employeur_LA_TRANSITION_ECOLOGIQUE.png "employeur")|
Racines de mots les plus importants dans les réponses :

- commun
- région
- collect
- transport
- etat
- local
- départ
- entrepris
- mair
- vill
- priv
- communaut
- solut
- territorial
- public
- citoyen
- aid
- servic
- fair
- voitur

### 4 - Par rapport à votre mode de chauffage actuel, pensez-vous qu'il existe des solutions alternatives plus écologiques ?

#### Statistiques générales sur les réponses

Nombre de réponses : 420952

#### Détail de la réponse fermées

Pourcentage de "oui" : 60.15%

Pourcentage de "Non" : 39.85%

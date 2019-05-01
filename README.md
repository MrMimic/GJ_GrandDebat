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

## Signification des tableaux

Les mots sont les 10 mots les plus "représentatifs" des réponses à la question donnée. Cette importance est calculée par TF-IDF (le score dans la deuxième colonne). Ils sont donc classés par "importance" à la moyenne des questions (ce n'est pas facile à visualiser).

Le graphe représente ainsi la différence d'utilisation de CE MOT dans les réponses du grand débat par rapport à une utilisation "normale" qui a été modélisée sur tout wikipédia + 20news groups. Une barre verte positif indique donc que le mot (du titre, qui est important pour les réponses à cette question) a été plus associé au mot en abscisse que dans la "moyenne" en français. Une barre rouge indique que le mot étudié est "normalement" souvent associé à ce terme, mais il ne l'a pas été dans les réponses au grand débat pour ce thème.

## Contact

        contact (at) tadadata (dot) fr

## ORGANISATION DE LETAT ET DES SERVICES PUBLICS

### Carte de participation

![ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS](maps/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS.png)

### 1 - Avez-vous déjà utilisé certaines de ces nouvelles formes de services publics ?

#### Statistiques générales sur les réponses

Nombre de réponses : 269796

#### Détail de la réponse fermées

Pourcentage de "oui" : 27.99%

Pourcentage de "Non" : 72.01%

### 2 - Comment l'Etat et les collectivités territoriales peuvent-ils s'améliorer pour mieux répondre aux défis de nos territoires les plus en difficulté ?

#### Statistiques générales sur les réponses

Nombre de réponses : 191064

Taille moyenne des réponses (caractères) : 182.61

Taille moyenne des réponses (mots) : 29.17

Taille maximum des réponses (mots) : 2195

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|services|0.026500942943617427|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_services.png "services")|
|territoires|0.020766910674507318|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_territoires.png "territoires")|
|publics|0.015193085701727522|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_publics.png "publics")|
|citoyens|0.013773060020179683|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_citoyens.png "citoyens")|
|terrain|0.013215766408607487|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_terrain.png "terrain")|
|proximité|0.01275969336567309|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_proximité.png "proximité")|
|faire|0.012711340817785246|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_faire.png "faire")|
|collectivités|0.01218491805650465|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_collectivités.png "collectivités")|
|faut|0.012053776542185377|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_faut.png "faut")|
|communes|0.011786562437071678|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_communes.png "communes")|

Racines de mots les plus importants dans les réponses :

- servic
- territoir
- public
- commun
- administr
- fair
- faut
- collect
- citoyen
- local
- région
- difficult
- moyen
- aid
- etat
- développ
- fonctionnair
- grand
- territorial
- terrain

### 3 - Connaissez-vous le "droit à l'erreur", c'est-à-dire le droit d'affirmer votre bonne foi lorsque vous faites un erreur dans vos déclarations ?

#### Statistiques générales sur les réponses

Nombre de réponses : 272339

#### Détail de la réponse fermées

Pourcentage de "oui" : 79.18%

Pourcentage de "Non" : 20.82%

### 4 - Estimez-vous avoir accès aux services publics dont vous avez besoin ?

#### Statistiques générales sur les réponses

Nombre de réponses : 280682

#### Détail de la réponse fermées

Pourcentage de "oui" : 68.17%

Pourcentage de "Non" : 31.83%

### 5 - Faut-il donner plus d'autonomie aux fonctionnaires de terrain ?

#### Statistiques générales sur les réponses

Nombre de réponses : 230363

#### Détail de la réponse fermées

Pourcentage de "oui" : 71.87%

Pourcentage de "Non" : 28.13%

### 6 - Faut-il revoir le fonctionnement et la formation de l'administration ?

#### Statistiques générales sur les réponses

Nombre de réponses : 231673

#### Détail de la réponse fermées

Pourcentage de "oui" : 90.41%

Pourcentage de "Non" : 9.59%

### 7 - Pouvez-vous identifier des règles que l'administration vous a déjà demandé d'appliquer et que vous avez jugées inutiles ou trop complexes ?

#### Statistiques générales sur les réponses

Nombre de réponses : 131957

Taille moyenne des réponses (caractères) : 158.48

Taille moyenne des réponses (mots) : 26.81

Taille maximum des réponses (mots) : 1996

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|demande|0.01768653606156722|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_demande.png "demande")|
|déclaration|0.0175482387835964|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_déclaration.png "déclaration")|
|permis|0.01748245948116367|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_permis.png "permis")|
|impôts|0.01582799506984266|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_impôts.png "impôts")|
|carte|0.014542685726954838|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_carte.png "carte")|
|règles|0.014524382552464668|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_règles.png "règles")|
|construire|0.01406739523085896|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_construire.png "construire")|
|documents|0.012075645277475844|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_documents.png "documents")|
|faire|0.011868256001632476|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_faire.png "faire")|
|dossier|0.011463179614515377|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_dossier.png "dossier")|

Racines de mots les plus importants dans les réponses :

- demand
- administr
- déclar
- regl
- impôt
- fair
- dossi
- complex
- cart
- docu
- perm
- servic
- exempl
- pai
- faut
- fiscal
- an
- papi
- démarch
- ident

### 8 - Quand vous pensez à l'évolution des services publics au cours des dernières années, quels sont ceux qui ont évolué de manière positive ?

#### Statistiques générales sur les réponses

Nombre de réponses : 201490

Taille moyenne des réponses (caractères) : 84.09

Taille moyenne des réponses (mots) : 13.9

Taille maximum des réponses (mots) : 3613

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|impôts|0.0810407665138223|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_impôts.png "impôts")|
|services|0.034759338979311175|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_services.png "services")|
|internet|0.033563061965905173|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_internet.png "internet")|
|poste|0.032454421794044445|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_poste.png "poste")|
|impots|0.026453648070874858|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_impots.png "impots")|
|service|0.023978190761265002|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_service.png "service")|
|ligne|0.01922549839412496|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_ligne.png "ligne")|
|démarches|0.017047199117189618|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_démarches.png "démarches")|
|sécurité|0.01545614344573096|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_sécurité.png "sécurité")|
|sociale|0.015277582573673747|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_sociale.png "sociale")|

Racines de mots les plus importants dans les réponses :

- servic
- impôt
- internet
- public
- post
- administr
- lign
- évolu
- démarch
- cart
- fiscal
- impot
- déclar
- social
- sécur
- posit
- gris
- fair
- sit
- acces

### 9 - Que pensez-vous de l'organisation de l'Etat et des administrations en France ? De quelle manière cette organisation devrait-elle évoluer ?

#### Statistiques générales sur les réponses

Nombre de réponses : 277561

Taille moyenne des réponses (caractères) : 374.71

Taille moyenne des réponses (mots) : 60.01

Taille maximum des réponses (mots) : 13113

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|faut|0.02049482015291343|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_faut.png "faut")|
|services|0.01909998876091498|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_services.png "services")|
|communes|0.018405075958391512|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_communes.png "communes")|
|simplification|0.017449647514262673|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_simplification.png "simplification")|
|organisation|0.016732427528829537|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_organisation.png "organisation")|
|administrations|0.01626484514298994|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_administrations.png "administrations")|
|supprimer|0.01608867586687618|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_supprimer.png "supprimer")|
|etat|0.015898146386921625|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_etat.png "etat")|
|fonctionnaires|0.01563442524126127|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_fonctionnaires.png "fonctionnaires")|
|simplifier|0.015321306521301557|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_simplifier.png "simplifier")|

Racines de mots les plus importants dans les réponses :

- administr
- servic
- commun
- faut
- région
- etat
- citoyen
- fonctionnair
- franc
- fair
- organis
- départ
- supprim
- public
- fonction
- nombr
- niveau
- grand
- pouvoir
- élus

### 10 - Quelles améliorations préconiseriez-vous ?

#### Statistiques générales sur les réponses

Nombre de réponses : 100236

Taille moyenne des réponses (caractères) : 145.64

Taille moyenne des réponses (mots) : 23.99

Taille maximum des réponses (mots) : 1528

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|services|0.039592797879774114|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_services.png "services")|
|publics|0.024494823524800622|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_publics.png "publics")|
|service|0.021278594677852584|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_service.png "service")|
|public|0.019377197411972243|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_public.png "public")|
|agents|0.018649167236720943|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_agents.png "agents")|
|internet|0.017261139893059416|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_internet.png "internet")|
|développer|0.015069577606914868|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_développer.png "développer")|
|rendez|0.014338770114422568|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_rendez.png "rendez")|
|horaires|0.01287008049239618|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_horaires.png "horaires")|
|faut|0.012818770395939965|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_faut.png "faut")|

Racines de mots les plus importants dans les réponses :

- servic
- public
- agent
- administr
- internet
- fair
- faut
- maison
- rend
- commun
- développ
- démarch
- polyvalent
- horair
- form
- mair
- citoyen
- pris
- regroup
- aid

### 11 - Quels nouveaux services ou quelles démarches souhaitez-vous voir développées sur Internet en priorité ?

#### Statistiques générales sur les réponses

Nombre de réponses : 153637

Taille moyenne des réponses (caractères) : 138.16

Taille moyenne des réponses (mots) : 22.73

Taille maximum des réponses (mots) : 2597

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|internet|0.04862799427573432|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_internet.png "internet")|
|démarches|0.028860867853604068|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_démarches.png "démarches")|
|services|0.02874823875770586|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_services.png "services")|
|accès|0.01694444162481033|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_accès.png "accès")|
|vote|0.0154895277879298|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_vote.png "vote")|
|déjà|0.01500285673813061|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_déjà.png "déjà")|
|administratives|0.01474731095559256|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_administratives.png "administratives")|
|faut|0.014584479614947613|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_faut.png "faut")|
|service|0.0139485088834156|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_service.png "service")|
|faire|0.013838247742834148|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_faire.png "faire")|

Racines de mots les plus importants dans les réponses :

- internet
- servic
- démarch
- administr
- acces
- public
- faut
- fair
- cart
- citoyen
- aid
- développ
- lign
- demand
- pouvoir
- sit
- déjà
- humain
- numer
- utilis

### 12 - Quels sont les services publics qui doivent le plus évoluer selon vous ?

#### Statistiques générales sur les réponses

Nombre de réponses : 202809

Taille moyenne des réponses (caractères) : 138.58

Taille moyenne des réponses (mots) : 22.63

Taille maximum des réponses (mots) : 3761

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|santé|0.046158560254828084|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_santé.png "santé")|
|éducation|0.03532839079231233|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_éducation.png "éducation")|
|services|0.03337091311575908|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_services.png "services")|
|justice|0.03210891912870628|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_justice.png "justice")|
|nationale|0.0271670029680097|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_nationale.png "nationale")|
|emploi|0.02651348109527244|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_emploi.png "emploi")|
|transports|0.019681827291750165|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_transports.png "transports")|
|poste|0.019394691120561948|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_poste.png "poste")|
|caf|0.018716481511624482|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_caf.png "caf")|
|education|0.018466202451952744|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_education.png "education")|

Racines de mots les plus importants dans les réponses :

- servic
- sant
- éduc
- public
- hôpital
- emploi
- national
- justic
- social
- administr
- transport
- faut
- post
- fair
- enseign
- sécur
- polic
- impôt
- aid
- caf

### 13 - Selon vous, l'Etat doit-il aujourd'hui transférer de nouvelles missions aux collectivités territoriales ?

#### Statistiques générales sur les réponses

Nombre de réponses : 259220

#### Détail de la réponse fermées

Pourcentage de "oui" : 50.72%

Pourcentage de "Non" : 49.28%

### 14 - Si non, quels types de services publics vous manquent dans votre territoire et qu'il est nécessaire de renforcer ?

#### Statistiques générales sur les réponses

Nombre de réponses : 113055

Taille moyenne des réponses (caractères) : 170.34

Taille moyenne des réponses (mots) : 28.36

Taille maximum des réponses (mots) : 1829

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|services|0.036721402070373624|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_services.png "services")|
|poste|0.030283294936106375|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_poste.png "poste")|
|santé|0.03010477486373241|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_santé.png "santé")|
|transports|0.02756050989039113|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_transports.png "transports")|
|publics|0.021020164926161485|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_publics.png "publics")|
|service|0.019970485548633492|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_service.png "service")|
|accès|0.017920830349730913|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_accès.png "accès")|
|commun|0.015702203090550874|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_commun.png "commun")|
|internet|0.015603305179821938|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_internet.png "internet")|
|public|0.015232351599441588|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_public.png "public")|

Racines de mots les plus importants dans les réponses :

- servic
- public
- transport
- post
- commun
- sant
- acces
- médecin
- faut
- internet
- vill
- hôpital
- fair
- administr
- habit
- rural
- manqu
- cart
- impôt
- proxim

### 15 - Si oui, avez-vous déjà utilisé ce droit à l'erreur ?

#### Statistiques générales sur les réponses

Nombre de réponses : 238369

#### Détail de la réponse fermées

Pourcentage de "oui" : 8.54%

Pourcentage de "Non" : 91.46%

### 16 - Si oui, en avez-vous été satisfait ?

#### Statistiques générales sur les réponses

Nombre de réponses : 82622

#### Détail de la réponse fermées

Pourcentage de "oui" : 68.54%

Pourcentage de "Non" : 31.46%

### 17 - Si oui, à quelle occasion en avez-vous fait usage ?

#### Statistiques générales sur les réponses

Nombre de réponses : 28057

Taille moyenne des réponses (caractères) : 106.17

Taille moyenne des réponses (mots) : 19.12

Taille maximum des réponses (mots) : 1084

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|déclaration|0.09007462305519211|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_déclaration.png "déclaration")|
|impôts|0.07591312830832607|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_impôts.png "impôts")|
|erreur|0.048835125938862634|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_erreur.png "erreur")|
|impôt|0.03729335687599984|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_impôt.png "impôt")|
|revenus|0.03534726269440357|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_revenus.png "revenus")|
|revenu|0.02771963049227179|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_revenu.png "revenu")|
|impots|0.02713409637983466|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_impots.png "impots")|
|fiscale|0.022187231466722555|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_fiscale.png "fiscale")|
|droit|0.02073427449192404|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_droit.png "droit")|
|paiement|0.01749018733506997|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_paiement.png "paiement")|

Racines de mots les plus importants dans les réponses :

- déclar
- impôt
- erreur
- droit
- pai
- fiscal
- administr
- revenus
- impot
- revenu
- bon
- tax
- fair
- servic
- foi
- retard
- oubl
- pénal
- demand
- jam

### 18 - Si vous avez été amené à chercher un emploi, pouvez-vous indiquer les éléments de satisfaction et/ou les difficultés rencontrés en précisant, pour chaque point, l'administration concernée :

#### Statistiques générales sur les réponses

Nombre de réponses : 81254

Taille moyenne des réponses (caractères) : 169.84

Taille moyenne des réponses (mots) : 29.69

Taille maximum des réponses (mots) : 2458

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|emploi|0.07109475415389228|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_emploi.png "emploi")|
|concerné|0.0565236024185389|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_concerné.png "concerné")|
|pôle|0.04090740309760205|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_pôle.png "pôle")|
|pole|0.03500602252479142|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_pole.png "pole")|
|ras|0.02203980275673893|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_ras.png "ras")|
|objet|0.01686092876584811|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_objet.png "objet")|
|travail|0.015457402717253849|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_travail.png "travail")|
|recherche|0.01540239465547769|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_recherche.png "recherche")|
|aide|0.013937298545200984|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_aide.png "aide")|
|jamais|0.013776753811956957|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_jamais.png "jamais")|

Racines de mots les plus importants dans les réponses :

- emploi
- pôl
- pol
- trouv
- aid
- format
- recherch
- travail
- concern
- an
- propos
- fair
- entrepris
- offre
- servic
- jam
- chômag
- administr
- faut
- conseil

### 19 - Si vous avez été amené à chercher une formation, pouvez-vous indiquer les éléments de satisfaction et/ou les difficultés rencontrés en précisant, pour chaque point, l'administration concernée :

#### Statistiques générales sur les réponses

Nombre de réponses : 69664

Taille moyenne des réponses (caractères) : 150.28

Taille moyenne des réponses (mots) : 25.73

Taille maximum des réponses (mots) : 1994

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|concerné|0.07194944114856493|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_concerné.png "concerné")|
|formation|0.04360122086059855|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_formation.png "formation")|
|emploi|0.03348306449930921|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_emploi.png "emploi")|
|ras|0.026659230268451777|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_ras.png "ras")|
|formations|0.02358211453960411|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_formations.png "formations")|
|objet|0.022629700096052457|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_objet.png "objet")|
|pôle|0.019862192843702144|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_pôle.png "pôle")|
|concernée|0.016262162423794604|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_concernée.png "concernée")|
|pole|0.016142947303177294|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_pole.png "pole")|
|néant|0.012795452764568215|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_néant.png "néant")|

Racines de mots les plus importants dans les réponses :

- format
- emploi
- pôl
- concern
- financ
- trouv
- pol
- fair
- aid
- an
- professionnel
- demand
- entrepris
- organ
- faut
- propos
- administr
- difficult
- travail
- form

### 20 - Si vous avez été amené à créer une entreprise, pouvez-vous indiquer les éléments de satisfaction et/ou les difficultés rencontrés en précisant, pour chaque point, l'administration concernée :

#### Statistiques générales sur les réponses

Nombre de réponses : 55542

Taille moyenne des réponses (caractères) : 143.91

Taille moyenne des réponses (mots) : 24.41

Taille maximum des réponses (mots) : 8977

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|concerné|0.07454779503883963|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_concerné.png "concerné")|
|entreprise|0.026304649788639237|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_entreprise.png "entreprise")|
|ras|0.02455224591134362|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_ras.png "ras")|
|objet|0.021028349563571417|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_objet.png "objet")|
|création|0.019189707206557226|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_création.png "création")|
|concernée|0.017218053328089747|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_concernée.png "concernée")|
|urssaf|0.015720878950069683|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_urssaf.png "urssaf")|
|nc|0.014191087194037683|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_nc.png "nc")|
|auto|0.01309877484124258|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_auto.png "auto")|
|rsi|0.013053514029769772|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_rsi.png "rsi")|

Racines de mots les plus importants dans les réponses :

- entrepris
- création
- cré
- administr
- concern
- urssaf
- aid
- pai
- servic
- entrepreneur
- démarch
- auto
- rsi
- fair
- complex
- activ
- commerc
- difficult
- faut
- impôt

### 21 - Si vous avez été amené à demander un remboursement de soins de santé, pouvez-vous indiquer les éléments de satisfaction et/ou les difficultés rencontrés en précisant, pour chaque point, l'administration concernée :

#### Statistiques générales sur les réponses

Nombre de réponses : 114287

Taille moyenne des réponses (caractères) : 142.59

Taille moyenne des réponses (mots) : 24.12

Taille maximum des réponses (mots) : 1789

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|problème|0.03879493378908498|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_problème.png "problème")|
|ras|0.0350672584217509|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_ras.png "ras")|
|remboursement|0.024849292457859048|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_remboursement.png "remboursement")|
|cpam|0.022186371405381742|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_cpam.png "cpam")|
|sociale|0.022067314411009495|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_sociale.png "sociale")|
|mutuelle|0.02175317826002509|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_mutuelle.png "mutuelle")|
|sécurité|0.021542693789499034|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_sécurité.png "sécurité")|
|remboursements|0.019705126406071357|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_remboursements.png "remboursements")|
|fonctionne|0.018754124182122137|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_fonctionne.png "fonctionne")|
|soins|0.01813581567457738|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_soins.png "soins")|

Racines de mots les plus importants dans les réponses :

- rembours
- mutuel
- social
- soin
- sécur
- cpam
- problem
- sant
- cart
- fonction
- charg
- pai
- médecin
- vital
- malad
- pris
- fair
- difficult
- demand
- rapid

### 22 - Si vous avez été amené à faire une demande d'aide pour une situation de handicap, pouvez-vous indiquer les éléments de satisfaction et/ou les difficultés rencontrés en précisant, pour chaque point, l'administration concernée :

#### Statistiques générales sur les réponses

Nombre de réponses : 54341

Taille moyenne des réponses (caractères) : 147.46

Taille moyenne des réponses (mots) : 25.49

Taille maximum des réponses (mots) : 2977

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|concerné|0.11401729860349824|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_concerné.png "concerné")|
|ras|0.04092201650834126|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_ras.png "ras")|
|objet|0.03192154288983359|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_objet.png "objet")|
|concernée|0.026983603438290097|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_concernée.png "concernée")|
|mdph|0.0247015637709079|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_mdph.png "mdph")|
|néant|0.018612559702008865|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_néant.png "néant")|
|handicap|0.018413523361493954|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_handicap.png "handicap")|
|nc|0.018255164822621642|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_nc.png "nc")|
|dossier|0.017098372185628492|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_dossier.png "dossier")|
|demande|0.016448398415427258|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_demande.png "demande")|

Racines de mots les plus importants dans les réponses :

- handicap
- mdph
- dossi
- concern
- demand
- aid
- an
- mois
- del
- enfant
- fair
- long
- administr
- situat
- trait
- répons
- pris
- faut
- cart
- charg

### 23 - Si vous avez été amené à former du personnel, pouvez-vous indiquer les éléments de satisfaction et/ou les difficultés rencontrés en précisant, pour chaque point, l'administration concernée :

#### Statistiques générales sur les réponses

Nombre de réponses : 33768

Taille moyenne des réponses (caractères) : 90.38

Taille moyenne des réponses (mots) : 15.07

Taille maximum des réponses (mots) : 1084

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|concerné|0.12004981901498692|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_concerné.png "concerné")|
|ras|0.04873485522990254|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_ras.png "ras")|
|objet|0.03568167895266342|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_objet.png "objet")|
|formation|0.03219361918817955|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_formation.png "formation")|
|nc|0.026359712764606608|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_nc.png "nc")|
|concernée|0.025996831097915053|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_concernée.png "concernée")|
|néant|0.023054196533889296|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_néant.png "néant")|
|formations|0.01580331304009336|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_formations.png "formations")|
|idem|0.011334985054306164|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_idem.png "idem")|
|personnel|0.009891105958040599|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_personnel.png "personnel")|

Racines de mots les plus importants dans les réponses :

- format
- concern
- entrepris
- form
- organ
- professionnel
- personnel
- emploi
- ras
- administr
- fair
- opca
- travail
- objet
- salari
- aid
- charg
- financ
- temp
- besoin

### 24 - Si vous avez été amené à mettre fin à votre activité, pouvez-vous indiquer les éléments de satisfaction et/ou les difficultés rencontrés en précisant, pour chaque point, l'administration concernée :

#### Statistiques générales sur les réponses

Nombre de réponses : 33237

Taille moyenne des réponses (caractères) : 89.1

Taille moyenne des réponses (mots) : 15.53

Taille maximum des réponses (mots) : 1084

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|concerné|0.11731166575849278|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_concerné.png "concerné")|
|ras|0.05361644042315962|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_ras.png "ras")|
|objet|0.0371174339195898|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_objet.png "objet")|
|nc|0.027627744641136136|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_nc.png "nc")|
|concernée|0.02434015041739338|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_concernée.png "concernée")|
|néant|0.021067335079123672|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_néant.png "néant")|
|activité|0.01599170206084087|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_activité.png "activité")|
|retraite|0.012381847241637406|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_retraite.png "retraite")|
|problème|0.01219800367424288|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_problème.png "problème")|
|entreprise|0.011680186876169535|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_entreprise.png "entreprise")|

Racines de mots les plus importants dans les réponses :

- concern
- activ
- entrepris
- retrait
- administr
- an
- ras
- fin
- urssaf
- difficult
- rsi
- pai
- fair
- objet
- servic
- liquid
- problem
- societ
- emploi
- commerc

### 25 - Si vous avez été amené à préparer votre retraite, pouvez-vous indiquer les éléments de satisfaction et/ou les difficultés rencontrés en précisant, pour chaque point, l'administration concernée :

#### Statistiques générales sur les réponses

Nombre de réponses : 102440

Taille moyenne des réponses (caractères) : 148.41

Taille moyenne des réponses (mots) : 25.52

Taille maximum des réponses (mots) : 1084

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|retraite|0.04452220909407884|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_retraite.png "retraite")|
|problème|0.02341980790292286|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_problème.png "problème")|
|concerné|0.022623145228633595|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_concerné.png "concerné")|
|dossier|0.020793194883472747|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_dossier.png "dossier")|
|carsat|0.018915960404553043|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_carsat.png "carsat")|
|ras|0.018233806283094234|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_ras.png "ras")|
|difficulté|0.017966104500346223|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_difficulté.png "difficulté")|
|ans|0.014990157484678527|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_ans.png "ans")|
|cnav|0.014425205765598074|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_cnav.png "cnav")|
|internet|0.013478026761609809|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_internet.png "internet")|

Racines de mots les plus importants dans les réponses :

- retrait
- dossi
- an
- demand
- carsat
- servic
- caiss
- difficult
- mois
- carri
- problem
- cnav
- fair
- inform
- administr
- internet
- répons
- complémentair
- sit
- prépar

### 26 - Si vous avez été amené à recruter du personnel, pouvez-vous indiquer les éléments de satisfaction et/ou les difficultés rencontrés en précisant, pour chaque point, l'administration concernée :

#### Statistiques générales sur les réponses

Nombre de réponses : 45047

Taille moyenne des réponses (caractères) : 113.31

Taille moyenne des réponses (mots) : 19.25

Taille maximum des réponses (mots) : 1084

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|concerné|0.08840358461638213|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_concerné.png "concerné")|
|emploi|0.03927149557701007|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_emploi.png "emploi")|
|ras|0.033812245500332516|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_ras.png "ras")|
|objet|0.02571294462495431|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_objet.png "objet")|
|pôle|0.023583550909507867|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_pôle.png "pôle")|
|pole|0.01996650621103956|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_pole.png "pole")|
|concernée|0.01842848397563094|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_concernée.png "concernée")|
|nc|0.017661083690933888|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_nc.png "nc")|
|néant|0.01521395734889793|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_néant.png "néant")|
|travail|0.012887472010674552|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_travail.png "travail")|

Racines de mots les plus importants dans les réponses :

- emploi
- recrut
- pôl
- concern
- pol
- travail
- entrepris
- embauch
- personnel
- aid
- servic
- administr
- candidat
- fair
- salari
- difficult
- trouv
- charg
- faut
- format

### 27 - Si vous avez été amené à recruter une personne portant un handicap, pouvez-vous indiquer les éléments de satisfaction et/ou les difficultés rencontrés en précisant, pour chaque point, l'administration concernée :

#### Statistiques générales sur les réponses

Nombre de réponses : 24193

Taille moyenne des réponses (caractères) : 46.14

Taille moyenne des réponses (mots) : 8.0

Taille maximum des réponses (mots) : 1084

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|concerné|0.1921045291563323|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_concerné.png "concerné")|
|ras|0.07634919166586042|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_ras.png "ras")|
|objet|0.05901369634924607|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_objet.png "objet")|
|concernée|0.04182317838874052|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_concernée.png "concernée")|
|nc|0.04050758483858956|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_nc.png "nc")|
|néant|0.03417891245394025|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_néant.png "néant")|
|applicable|0.011861821974621753|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_applicable.png "applicable")|
|idem|0.009871748956157923|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_idem.png "idem")|
|concerne|0.00889364845266747|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_concerne.png "concerne")|
|handicap|0.008718541259396521|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_handicap.png "handicap")|

Racines de mots les plus importants dans les réponses :

- concern
- handicap
- ras
- objet
- entrepris
- nc
- emploi
- aid
- recrut
- né
- travail
- administr
- post
- embauch
- situat
- fair
- servic
- adapt
- cas
- salari

### 28 - Si vous avez été amené à rémunérer du personnel, pouvez-vous indiquer les éléments de satisfaction et/ou les difficultés rencontrés en précisant, pour chaque point, l'administration concernée :

#### Statistiques générales sur les réponses

Nombre de réponses : 40775

Taille moyenne des réponses (caractères) : 97.02

Taille moyenne des réponses (mots) : 16.47

Taille maximum des réponses (mots) : 1084

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|concerné|0.09318159234146067|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_concerné.png "concerné")|
|ras|0.0424150186975582|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_ras.png "ras")|
|objet|0.02750829186851247|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_objet.png "objet")|
|charges|0.026225553587407434|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_charges.png "charges")|
|cesu|0.02581255926556164|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_cesu.png "cesu")|
|nc|0.019993942222069124|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_nc.png "nc")|
|concernée|0.01889268464241595|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_concernée.png "concernée")|
|néant|0.016976199810141535|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_néant.png "néant")|
|urssaf|0.015483161394745794|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_urssaf.png "urssaf")|
|emploi|0.013345232691958734|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_emploi.png "emploi")|

Racines de mots les plus importants dans les réponses :

- charg
- concern
- pai
- emploi
- salair
- entrepris
- cesu
- urssaf
- complex
- salari
- travail
- servic
- social
- fair
- pay
- comptabl
- fich
- ras
- rémuner
- administr

### 29 - Si vous avez été amené à scolariser votre enfant, pouvez-vous indiquer les éléments de satisfaction et/ou les difficultés rencontrés en précisant, pour chaque point, l'administration concernée :

#### Statistiques générales sur les réponses

Nombre de réponses : 87938

Taille moyenne des réponses (caractères) : 206.64

Taille moyenne des réponses (mots) : 34.89

Taille maximum des réponses (mots) : 5211

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|concerné|0.04221589068707815|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_concerné.png "concerné")|
|enfants|0.028213713945572042|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_enfants.png "enfants")|
|ras|0.02403106322038487|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_ras.png "ras")|
|école|0.023118499424543273|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_école.png "école")|
|enfant|0.023018370061048697|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_enfant.png "enfant")|
|scolaire|0.016794495270884526|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_scolaire.png "scolaire")|
|difficulté|0.015284341711844727|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_difficulté.png "difficulté")|
|problème|0.015043130295359688|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_problème.png "problème")|
|nationale|0.014591411949714727|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_nationale.png "nationale")|
|enseignants|0.014324287243770108|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_enseignants.png "enseignants")|

Racines de mots les plus importants dans les réponses :

- enfant
- écol
- enseign
- scolair
- élev
- class
- éduc
- colleg
- national
- difficult
- priv
- lyc
- parent
- établ
- professeur
- fair
- scolaris
- faut
- niveau
- problem

### 30 - Y a-t-il d'autres points sur l'organisation de l'Etat et des services publics sur lesquels vous souhaiteriez vous exprimer ?

#### Statistiques générales sur les réponses

Nombre de réponses : 175415

Taille moyenne des réponses (caractères) : 705.0

Taille moyenne des réponses (mots) : 114.52

Taille maximum des réponses (mots) : 12890

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|vitesse|0.06887168017032361|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_vitesse.png "vitesse")|
|conducteurs|0.052115070329983026|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_conducteurs.png "conducteurs")|
|gouvernement|0.0510944446601219|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_gouvernement.png "gouvernement")|
|lieu|0.05046343015844594|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_lieu.png "lieu")|
|limitation|0.03523366444317675|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_limitation.png "limitation")|
|sécurité|0.034980338600422205|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_sécurité.png "sécurité")|
|radars|0.03473530419981668|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_radars.png "radars")|
|routière|0.034686866648140476|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_routière.png "routière")|
|politique|0.034476997712517554|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_politique.png "politique")|
|faut|0.025425529894245937|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS_faut.png "faut")|

Racines de mots les plus importants dans les réponses :

- vitess
- gouvern
- conducteur
- lieu
- servic
- limit
- polit
- rout
- faut
- sécur
- franc
- fair
- routi
- radar
- citoyen
- temp
- km
- mettr
- 80
- mesur

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
|oui|0.4129625042412908|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_oui.png "oui")|
|déplacements|0.10820626794743922|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_déplacements.png "déplacements")|
|quotidiens|0.10820626794743922|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_quotidiens.png "quotidiens")|
|utilise|0.10820626794743922|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_utilise.png "utilise")|
|voiture|0.10820626794743922|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_voiture.png "voiture")|

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
|région|0.06358763194700856|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_région.png "région")|
|collectivités|0.05798366356830574|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_collectivités.png "collectivités")|
|etat|0.045649734410376654|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_etat.png "etat")|
|commune|0.044062757889441084|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_commune.png "commune")|
|département|0.04346591607034401|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_département.png "département")|
|communes|0.040447397552507564|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_communes.png "communes")|
|locales|0.034504722070271256|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_locales.png "locales")|
|régions|0.02229919121307835|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_régions.png "régions")|
|territoriales|0.02134369861864201|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_territoriales.png "territoriales")|
|mairie|0.020791707427357007|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_mairie.png "mairie")|

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

### 5 - Qu'est-ce qui pourrait vous inciter à changer vos comportements comme par exemple mieux entretenir et régler votre chauffage, modifier votre manière de conduire ou renoncer à prendre votre véhicule pour de très petites distances ?

#### Statistiques générales sur les réponses

Nombre de réponses : 384587

Taille moyenne des réponses (caractères) : 165.89

Taille moyenne des réponses (mots) : 27.77

Taille maximum des réponses (mots) : 1681

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|déjà|0.06670854321842333|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_déjà.png "déjà")|
|transports|0.029193855364077644|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_transports.png "transports")|
|commun|0.026177979780067858|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_commun.png "commun")|
|voiture|0.018552866745300503|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_voiture.png "voiture")|
|chauffage|0.017835240441194326|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_chauffage.png "chauffage")|
|faire|0.015256994009511528|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_faire.png "faire")|
|transport|0.013963954416062631|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_transport.png "transport")|
|véhicule|0.01269986853476107|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_véhicule.png "véhicule")|
|aides|0.012259540033944739|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_aides.png "aides")|
|vélo|0.011899066582179263|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_vélo.png "vélo")|

Racines de mots les plus importants dans les réponses :

- transport
- commun
- voitur
- déjà
- chauffag
- aid
- véhicul
- fair
- chang
- électr
- incit
- vill
- isol
- développ
- vélo
- faut
- utilis
- cyclabl
- petit
- pist

### 6 - Que faudrait-il faire selon vous pour apporter des réponses à ce problème ?

#### Statistiques générales sur les réponses

Nombre de réponses : 437097

Taille moyenne des réponses (caractères) : 387.78

Taille moyenne des réponses (mots) : 61.52

Taille maximum des réponses (mots) : 10470

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|produits|0.016719302855932372|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_produits.png "produits")|
|faire|0.015846786064025828|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_faire.png "faire")|
|transports|0.015447731998906793|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_transports.png "transports")|
|taxer|0.014034055408251462|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_taxer.png "taxer")|
|réduire|0.013687014383460363|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_réduire.png "réduire")|
|développer|0.013367554418160905|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_développer.png "développer")|
|interdire|0.013117609726865952|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_interdire.png "interdire")|
|faut|0.012597394991391904|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_faut.png "faut")|
|limiter|0.012440695634748386|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_limiter.png "limiter")|
|entreprises|0.012215460264618519|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_entreprises.png "entreprises")|

Racines de mots les plus importants dans les réponses :

- transport
- produit
- tax
- consomm
- fair
- énerg
- développ
- faut
- écolog
- franc
- pollu
- entrepris
- utilis
- grand
- voitur
- électr
- limit
- favoris
- product
- pollut

### 7 - Que pourrait faire la France pour faire partager ses choix en matière d'environnement au niveau européen et international ?

#### Statistiques générales sur les réponses

Nombre de réponses : 361027

Taille moyenne des réponses (caractères) : 170.43

Taille moyenne des réponses (mots) : 28.09

Taille maximum des réponses (mots) : 5694

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|exemple|0.05545839037344588|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_exemple.png "exemple")|
|montrer|0.04293080501406361|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_montrer.png "montrer")|
|pays|0.029031703929525022|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_pays.png "pays")|
|faire|0.02415467050805222|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_faire.png "faire")|
|donner|0.02397895056512208|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_donner.png "donner")|
|france|0.0232175541202768|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_france.png "france")|
|déjà|0.01609968667785267|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_déjà.png "déjà")|
|europe|0.015651819290672858|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_europe.png "europe")|
|choix|0.015275791560987954|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_choix.png "choix")|
|exemplaire|0.014274613337317403|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_exemplaire.png "exemplaire")|

Racines de mots les plus importants dans les réponses :

- exempl
- pay
- franc
- européen
- fair
- montr
- écolog
- tax
- europ
- produit
- niveau
- don
- choix
- environ
- polit
- déjà
- faut
- développ
- international
- énerg

### 8 - Quel est aujourd'hui pour vous le problème concret le plus important dans le domaine de l'environnement ?

#### Statistiques générales sur les réponses

Nombre de réponses : 456919

Taille moyenne des réponses (caractères) : 59.14

Taille moyenne des réponses (mots) : 9.06

Taille maximum des réponses (mots) : 4087

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|air|0.14298803032085325|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_air.png "air")|
|pollution|0.14294378414589023|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_pollution.png "pollution")|
|crue|0.13912361031784243|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_crue.png "crue")|
|sécheresse|0.13904437682257698|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_sécheresse.png "sécheresse")|
|dérèglements|0.1389061395430113|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_dérèglements.png "dérèglements")|
|climatiques|0.138643987567412|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_climatiques.png "climatiques")|
|disparition|0.11366940683283475|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_disparition.png "disparition")|
|espèces|0.11362044277236148|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_espèces.png "espèces")|
|biodiversité|0.11346936595050344|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_biodiversité.png "biodiversité")|
|problèmes|0.0093759936558531|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_problèmes.png "problèmes")|

Racines de mots les plus importants dans les réponses :

- climat
- déregl
- sécheress
- cru
- pollut
- air
- biodivers
- disparit
- espec
- problem
- import
- li
- eau
- sol
- déchet
- environ
- éros
- ensembl
- terr
- littoral

### 9 - Quelles seraient pour vous les solutions les plus simples et les plus supportables sur un plan financier pour vous inciter à changer vos comportements ?

#### Statistiques générales sur les réponses

Nombre de réponses : 332870

Taille moyenne des réponses (caractères) : 162.38

Taille moyenne des réponses (mots) : 26.75

Taille maximum des réponses (mots) : 8350

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|transports|0.022771992084740244|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_transports.png "transports")|
|commun|0.019233392431612702|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_commun.png "commun")|
|produits|0.016879867950531757|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_produits.png "produits")|
|aides|0.016567939189374364|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_aides.png "aides")|
|prix|0.0164629875135966|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_prix.png "prix")|
|aide|0.014293819997260145|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_aide.png "aide")|
|faire|0.013584235750204642|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_faire.png "faire")|
|voiture|0.012162090092194046|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_voiture.png "voiture")|
|changer|0.011304812918800535|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_changer.png "changer")|
|déjà|0.010587708632930903|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_déjà.png "déjà")|

Racines de mots les plus importants dans les réponses :

- aid
- transport
- tax
- produit
- commun
- chang
- voitur
- fair
- véhicul
- électr
- financi
- prix
- écolog
- incit
- consomm
- comport
- faut
- solut
- isol
- impôt

### 10 - Si non, quelles sont les solutions de mobilité alternatives que vous souhaiteriez pouvoir utiliser ?

#### Statistiques générales sur les réponses

Nombre de réponses : 309509

Taille moyenne des réponses (caractères) : 51.51

Taille moyenne des réponses (mots) : 8.98

Taille maximum des réponses (mots) : 1555

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|transports|0.2835119680801581|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_transports.png "transports")|
|commun|0.2834762022241322|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_commun.png "commun")|
|vélo|0.20763091183057586|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_vélo.png "vélo")|
|covoiturage|0.1293751383754913|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_covoiturage.png "covoiturage")|
|demande|0.1223424240394383|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_demande.png "demande")|
|transport|0.12190756198785921|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_transport.png "transport")|
|auto|0.07452246349806914|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_auto.png "auto")|
|partage|0.07446161650601522|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_partage.png "partage")|
|voiture|0.01400511667259641|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_voiture.png "voiture")|
|marche|0.0131243150822077|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_marche.png "marche")|

Racines de mots les plus importants dans les réponses :

- transport
- commun
- vélo
- demand
- covoiturag
- partag
- auto
- voitur
- électr
- march
- véhicul
- pied
- solut
- train
- déplac
- vill
- utilis
- campagn
- travail
- rural

### 11 - Si oui, de quelle manière votre vie quotidienne est-elle touchée par le changement climatique ?

#### Statistiques générales sur les réponses

Nombre de réponses : 288692

Taille moyenne des réponses (caractères) : 125.45

Taille moyenne des réponses (mots) : 20.39

Taille maximum des réponses (mots) : 2080

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|pollution|0.043216536873980374|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_pollution.png "pollution")|
|air|0.03130563237351926|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_air.png "air")|
|sécheresse|0.02479180390592117|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_sécheresse.png "sécheresse")|
|saisons|0.021739903550965216|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_saisons.png "saisons")|
|canicule|0.016382978131249535|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_canicule.png "canicule")|
|inondations|0.016056526824035463|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_inondations.png "inondations")|
|chaleur|0.015811017769240182|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_chaleur.png "chaleur")|
|climatique|0.015440937336205258|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_climatique.png "climatique")|
|climatiques|0.015215925063186166|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_climatiques.png "climatiques")|
|températures|0.01510109004596608|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_températures.png "températures")|

Racines de mots les plus importants dans les réponses :

- pollut
- climat
- air
- sécheress
- saison
- chang
- canicul
- températur
- eau
- chaleur
- inond
- disparit
- déregl
- chaud
- augment
- oiseau
- espec
- tempêt
- insect
- vi

### 12 - Si oui, que faites-vous aujourd'hui pour protéger l'environnement et/ou que pourriez-vous faire ?

#### Statistiques générales sur les réponses

Nombre de réponses : 416575

Taille moyenne des réponses (caractères) : 192.58

Taille moyenne des réponses (mots) : 31.65

Taille maximum des réponses (mots) : 9703

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|tri|0.04362303012120248|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_tri.png "tri")|
|déchets|0.04151930128185252|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_déchets.png "déchets")|
|consommation|0.031109942175868734|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_consommation.png "consommation")|
|produits|0.030384858707684342|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_produits.png "produits")|
|voiture|0.030174947708799273|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_voiture.png "voiture")|
|eau|0.023634889512468064|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_eau.png "eau")|
|sélectif|0.02283958385360352|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_sélectif.png "sélectif")|
|transports|0.022537111857860156|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_transports.png "transports")|
|bio|0.02252654802237684|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_bio.png "bio")|
|commun|0.02169485761837201|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_commun.png "commun")|

Racines de mots les plus importants dans les réponses :

- tri
- consomm
- déchet
- produit
- utilis
- voitur
- eau
- local
- transport
- limit
- déplac
- achet
- bio
- commun
- achat
- électr
- chauffag
- vélo
- fair
- sélect

### 13 - Si oui, que faudrait-il faire pour vous convaincre ou vous aider à changer de mode de chauffage ?

#### Statistiques générales sur les réponses

Nombre de réponses : 271703

Taille moyenne des réponses (caractères) : 121.28

Taille moyenne des réponses (mots) : 20.19

Taille maximum des réponses (mots) : 1313

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|chauffage|0.03330558482144534|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_chauffage.png "chauffage")|
|aide|0.032455028458143444|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_aide.png "aide")|
|aides|0.025997181506635523|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_aides.png "aides")|
|financière|0.022263519127843582|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_financière.png "financière")|
|solaire|0.017814856998950634|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_solaire.png "solaire")|
|chaleur|0.017288820287598303|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_chaleur.png "chaleur")|
|panneaux|0.016272247754084437|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_panneaux.png "panneaux")|
|isolation|0.015729284077762654|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_isolation.png "isolation")|
|chaudière|0.015297051100322853|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_chaudière.png "chaudière")|
|changer|0.014526063428875505|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_changer.png "changer")|

Racines de mots les plus importants dans les réponses :

- aid
- chauffag
- solair
- financi
- chang
- isol
- électr
- chaudi
- install
- énerg
- panneau
- chaleur
- mod
- fair
- pomp
- solut
- gaz
- écolog
- maison
- invest

### 14 - Si oui, que faudrait-il faire pour vous convaincre ou vous aider à utiliser ces solutions alternatives ?

#### Statistiques générales sur les réponses

Nombre de réponses : 230102

Taille moyenne des réponses (caractères) : 136.99

Taille moyenne des réponses (mots) : 23.22

Taille maximum des réponses (mots) : 1631

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|transports|0.047189091465880635|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_transports.png "transports")|
|commun|0.04427460913701742|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_commun.png "commun")|
|déjà|0.03513564337623144|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_déjà.png "déjà")|
|utilise|0.029752970599406944|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_utilise.png "utilise")|
|transport|0.02462749810965383|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_transport.png "transport")|
|vélo|0.02462470031199489|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_vélo.png "vélo")|
|cyclables|0.022355866710177672|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_cyclables.png "cyclables")|
|bus|0.02225163812443127|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_bus.png "bus")|
|pistes|0.02187847920943489|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_pistes.png "pistes")|
|voiture|0.02030555162104893|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_voiture.png "voiture")|

Racines de mots les plus importants dans les réponses :

- transport
- commun
- voitur
- utilis
- vélo
- bus
- cyclabl
- vill
- pist
- développ
- train
- déjà
- horair
- gratuit
- travail
- déplac
- solut
- covoiturag
- fair
- électr

### 15 - Y a-t-il d'autres points sur la transition écologique sur lesquels vous souhaiteriez vous exprimer ?

#### Statistiques générales sur les réponses

Nombre de réponses : 346482

Taille moyenne des réponses (caractères) : 447.76

Taille moyenne des réponses (mots) : 72.64

Taille maximum des réponses (mots) : 51212

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|faut|0.019287633784408797|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_faut.png "faut")|
|faire|0.017313095191467936|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_faire.png "faire")|
|écologique|0.01658885952883699|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_écologique.png "écologique")|
|transition|0.01632412794677502|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_transition.png "transition")|
|produits|0.013272300014813724|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_produits.png "produits")|
|taxer|0.010962904909907428|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_taxer.png "taxer")|
|france|0.010943939270395282|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_france.png "france")|
|nucléaire|0.010870987116878741|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_nucléaire.png "nucléaire")|
|énergie|0.010746200054157008|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_énergie.png "énergie")|
|développer|0.010582022380383943|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_TRANSITION_ECOLOGIQUE_développer.png "développer")|

Racines de mots les plus importants dans les réponses :

- écolog
- faut
- fair
- tax
- franc
- énerg
- produit
- transit
- électr
- développ
- transport
- consomm
- voitur
- grand
- nucléair
- entrepris
- utilis
- véhicul
- product
- pollu

### 16 - À titre personnel, pensez-vous pouvoir contribuer à protéger l'environnement ?

#### Statistiques générales sur les réponses

Nombre de réponses : 443117

#### Détail de la réponse fermées

Pourcentage de "oui" : 94.51%

Pourcentage de "Non" : 5.49%

## LA FISCALITE ET LES DEPENSES PUBLIQUES

### Carte de participation

![LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES](maps/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES.png)

### 1 - Afin de financer les dépenses sociales, faut-il selon vous...

#### Statistiques générales sur les réponses

Nombre de réponses : 522223

Taille moyenne des réponses (caractères) : 141.44

Taille moyenne des réponses (mots) : 22.63

Taille maximum des réponses (mots) : 3525

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|aides|0.1484676571730609|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_aides.png "aides")|
|sociales|0.1463531801806897|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_sociales.png "sociales")|
|attribution|0.14596774787888045|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_attribution.png "attribution")|
|revoir|0.14574743716466468|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_revoir.png "revoir")|
|conditions|0.14562799678290583|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_conditions.png "conditions")|
|augmenter|0.09559027647037384|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_augmenter.png "augmenter")|
|travail|0.08847347821785678|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_travail.png "travail")|
|temps|0.08789227846863287|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_temps.png "temps")|
|retraite|0.07762184105264297|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_retraite.png "retraite")|
|âge|0.07669888006881342|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_âge.png "âge")|

Racines de mots les plus importants dans les réponses :

- social
- aid
- revoir
- attribu
- condit
- augment
- travail
- retrait
- temp
- âge
- recul
- fiscal
- impôt
- tax
- dépens
- fair
- entrepris
- franc
- supprim
- fraud

### 2 - Pour quelle(s) politique(s) publique(s) ou pour quels domaines d'action publique, seriez-vous prêts à payer plus d'impôts ?

#### Statistiques générales sur les réponses

Nombre de réponses : 442531

Taille moyenne des réponses (caractères) : 100.81

Taille moyenne des réponses (mots) : 16.94

Taille maximum des réponses (mots) : 2884

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|santé|0.07091291784045908|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_santé.png "santé")|
|éducation|0.04663874166951176|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_éducation.png "éducation")|
|impôts|0.025518425080341346|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_impôts.png "impôts")|
|déjà|0.02436622946300346|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_déjà.png "déjà")|
|sécurité|0.021215356239522132|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_sécurité.png "sécurité")|
|education|0.019967109227169377|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_education.png "education")|
|environnement|0.017620528230940916|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_environnement.png "environnement")|
|payer|0.017447297250681327|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_payer.png "payer")|
|transition|0.017087651544700055|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_transition.png "transition")|
|justice|0.015537721490431361|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_justice.png "justice")|

Racines de mots les plus importants dans les réponses :

- impôt
- sant
- pai
- éduc
- déjà
- faut
- écolog
- pay
- dépens
- aid
- publiqu
- franc
- fair
- sécur
- augment
- transit
- tax
- social
- fiscal
- justic

### 3 - Que faudrait-il faire pour rendre la fiscalité plus juste et plus efficace ?

#### Statistiques générales sur les réponses

Nombre de réponses : 518709

Taille moyenne des réponses (caractères) : 355.11

Taille moyenne des réponses (mots) : 59.7

Taille maximum des réponses (mots) : 13304

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|impôt|0.04188724906476025|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_impôt.png "impôt")|
|revenus|0.0318071638856003|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_revenus.png "revenus")|
|revenu|0.0293505453068842|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_revenu.png "revenu")|
|impôts|0.027637711376805076|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_impôts.png "impôts")|
|monde|0.02585536876424201|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_monde.png "monde")|
|payer|0.02377745797277555|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_payer.png "payer")|
|supprimer|0.02167417075000979|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_supprimer.png "supprimer")|
|fiscales|0.020258690737834862|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_fiscales.png "fiscales")|
|faire|0.020242259481376798|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_faire.png "faire")|
|tranches|0.0199442097344549|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_tranches.png "tranches")|

Racines de mots les plus importants dans les réponses :

- impôt
- fiscal
- tax
- pai
- revenus
- revenu
- franc
- entrepris
- tranch
- supprim
- fair
- mond
- tva
- augment
- nich
- social
- aid
- citoyen
- produit
- retrait

### 4 - Quelles sont toutes les choses qui pourraient être faites pour améliorer l'information des citoyens sur l'utilisation des impôts ?

#### Statistiques générales sur les réponses

Nombre de réponses : 436728

Taille moyenne des réponses (caractères) : 216.92

Taille moyenne des réponses (mots) : 35.71

Taille maximum des réponses (mots) : 14963

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|impôts|0.03206809766214051|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_impôts.png "impôts")|
|dépenses|0.03112732386948845|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_dépenses.png "dépenses")|
|transparence|0.02741105572087249|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_transparence.png "transparence")|
|utilisation|0.022358518659873053|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_utilisation.png "utilisation")|
|impôt|0.019906220518847887|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_impôt.png "impôt")|
|information|0.018766412516226936|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_information.png "information")|
|site|0.015350070981174689|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_site.png "site")|
|citoyens|0.014473629536209887|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_citoyens.png "citoyens")|
|internet|0.014271212050805095|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_internet.png "internet")|
|faire|0.013497766022547738|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_faire.png "faire")|

Racines de mots les plus importants dans les réponses :

- impôt
- dépens
- inform
- utilis
- citoyen
- publiqu
- transparent
- compt
- fair
- franc
- budget
- public
- fiscal
- tax
- pai
- annuel
- social
- anné
- servic
- sit

### 5 - Quels sont les domaines prioritaires où notre protection sociale doit être renforcée ?

#### Statistiques générales sur les réponses

Nombre de réponses : 439536

Taille moyenne des réponses (caractères) : 102.81

Taille moyenne des réponses (mots) : 17.0

Taille maximum des réponses (mots) : 3926

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|santé|0.12649689213547624|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_santé.png "santé")|
|dépendance|0.02876736785619803|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_dépendance.png "dépendance")|
|logement|0.02838579000816582|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_logement.png "logement")|
|âgées|0.027687386433217664|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_âgées.png "âgées")|
|aide|0.023708850455142434|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_aide.png "aide")|
|éducation|0.02333443825073337|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_éducation.png "éducation")|
|handicap|0.022961233220141267|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_handicap.png "handicap")|
|retraite|0.022355433872094557|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_retraite.png "retraite")|
|enfance|0.02086257126386532|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_enfance.png "enfance")|
|vieillesse|0.017683162820666374|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_vieillesse.png "vieillesse")|

Racines de mots les plus importants dans les réponses :

- sant
- aid
- retrait
- handicap
- social
- log
- âgé
- dépend
- enfant
- protect
- malad
- soin
- éduc
- charg
- vi
- faut
- enfanc
- famill
- franc
- pris

### 6 - Quels sont selon vous les impôts qu'il faut baisser en priorité ?

#### Statistiques générales sur les réponses

Nombre de réponses : 474190

Taille moyenne des réponses (caractères) : 134.86

Taille moyenne des réponses (mots) : 23.32

Taille maximum des réponses (mots) : 6954

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|tva|0.10281548730147227|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_tva.png "tva")|
|revenu|0.06091578964477664|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_revenu.png "revenu")|
|produits|0.04919567624447329|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_produits.png "produits")|
|impôt|0.0471667284600007|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_impôt.png "impôt")|
|impôts|0.04488340092846636|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_impôts.png "impôts")|
|csg|0.043023918373106554|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_csg.png "csg")|
|taxe|0.04010335414078276|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_taxe.png "taxe")|
|nécessité|0.03581453935499507|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_nécessité.png "nécessité")|
|habitation|0.02965359108943941|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_habitation.png "habitation")|
|taxes|0.02725196806498995|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_taxes.png "taxes")|

Racines de mots les plus importants dans les réponses :

- impôt
- tva
- tax
- produit
- revenu
- baiss
- csg
- nécess
- habit
- supprim
- faut
- revenus
- retrait
- fonci
- augment
- pai
- impot
- fiscal
- moyen
- franc

### 7 - S'il faut selon vous revoir les conditions d'attribution de certaines aides sociales, lesquelles doivent être concernées ?

#### Statistiques générales sur les réponses

Nombre de réponses : 418642

Taille moyenne des réponses (caractères) : 190.1

Taille moyenne des réponses (mots) : 31.59

Taille maximum des réponses (mots) : 11947

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|allocations|0.05095356652277424|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_allocations.png "allocations")|
|aides|0.04522199414295729|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_aides.png "aides")|
|familiales|0.04262612945537584|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_familiales.png "familiales")|
|rsa|0.033886687169422613|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_rsa.png "rsa")|
|chômage|0.033868039167636484|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_chômage.png "chômage")|
|sociales|0.02266324100327895|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_sociales.png "sociales")|
|aide|0.02123962233584299|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_aide.png "aide")|
|allocation|0.01892544059614491|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_allocation.png "allocation")|
|enfants|0.018121585791101152|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_enfants.png "enfants")|
|revenus|0.017334572555472973|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_revenus.png "revenus")|

Racines de mots les plus importants dans les réponses :

- aid
- alloc
- social
- familial
- enfant
- chômag
- rsa
- faut
- attribu
- franc
- travail
- log
- revenus
- contrôl
- travaill
- famill
- fair
- emploi
- condit
- supprim

### 8 - Y a-t-il d'autres points sur les impôts et les dépenses sur lesquels vous souhaiteriez vous exprimer ?

#### Statistiques générales sur les réponses

Nombre de réponses : 446559

Taille moyenne des réponses (caractères) : 471.49

Taille moyenne des réponses (mots) : 78.42

Taille maximum des réponses (mots) : 12890

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|dépenses|0.018914469171846603|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_dépenses.png "dépenses")|
|faut|0.01812112095710074|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_faut.png "faut")|
|impôts|0.017693774079779265|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_impôts.png "impôts")|
|impôt|0.017503959352217574|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_impôt.png "impôt")|
|supprimer|0.0161578507919409|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_supprimer.png "supprimer")|
|faire|0.015104268911591905|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_faire.png "faire")|
|vie|0.013074349672101457|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_vie.png "vie")|
|retraites|0.01283491551482261|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_retraites.png "retraites")|
|réduire|0.012535711093564796|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_réduire.png "réduire")|
|france|0.01244096162466063|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES_france.png "france")|

Racines de mots les plus importants dans les réponses :

- impôt
- retrait
- franc
- fiscal
- dépens
- tax
- faut
- pai
- fair
- entrepris
- social
- supprim
- aid
- salair
- publiqu
- augment
- pay
- vi
- fonction
- économ

## DEMOCRATIE ET CITOYENNETE

### Carte de participation

![DEMOCRATIE_ET_CITOYENNETE](maps/DEMOCRATIE_ET_CITOYENNETE.png)

### 1 - Comment garantir le respect par tous de la compréhension réciproque et des valeurs intangibles de la République ?

#### Statistiques générales sur les réponses

Nombre de réponses : 242539

Taille moyenne des réponses (caractères) : 152.34

Taille moyenne des réponses (mots) : 25.58

Taille maximum des réponses (mots) : 5753

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|éducation|0.05517211430960885|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_éducation.png "éducation")|
|école|0.042607134389282236|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_école.png "école")|
|civique|0.032094813606750594|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_civique.png "civique")|
|valeurs|0.026196059147979872|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_valeurs.png "valeurs")|
|république|0.02292502170106708|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_république.png "république")|
|education|0.02174742153239562|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_education.png "education")|
|loi|0.02107090255234669|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_loi.png "loi")|
|respect|0.020152550840226022|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_respect.png "respect")|
|faire|0.01847472429401398|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_faire.png "faire")|
|instruction|0.015261384519201584|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_instruction.png "instruction")|

Racines de mots les plus importants dans les réponses :

- écol
- éduc
- respect
- valeur
- républ
- civiqu
- fair
- franc
- citoyen
- enseign
- loi
- faut
- appliqu
- droit
- jeun
- national
- sanction
- lois
- servic
- cour

### 2 - En dehors des élus politiques, faut-il donner un rôle plus important aux associations et aux organisations syndicales et professionnelles ?

#### Statistiques générales sur les réponses

Nombre de réponses : 307638

#### Détail de la réponse fermées

Pourcentage de "oui" : 60.31%

Pourcentage de "Non" : 39.69%

### 3 - En matière d'immigration, une fois nos obligations d'asile remplies, souhaitez-vous que nous puissions nous fixer des objectifs annuels définis par le Parlement ?

#### Statistiques générales sur les réponses

Nombre de réponses : 246511

Taille moyenne des réponses (caractères) : 79.05

Taille moyenne des réponses (mots) : 13.76

Taille maximum des réponses (mots) : 5753

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|oui|0.2992649489428453|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_oui.png "oui")|
|objectifs|0.01764635036872736|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_objectifs.png "objectifs")|
|quotas|0.017364251363602732|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_quotas.png "quotas")|
|immigration|0.016434660763635055|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_immigration.png "immigration")|
|pays|0.01626614681969808|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_pays.png "pays")|
|faut|0.014281820242193597|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_faut.png "faut")|
|asile|0.013633611105225157|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_asile.png "asile")|
|besoins|0.012021476002245655|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_besoins.png "besoins")|
|fonction|0.011312278129542474|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_fonction.png "fonction")|
|obligations|0.010347977651052845|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_obligations.png "obligations")|

Racines de mots les plus importants dans les réponses :

- oui
- immigr
- object
- pay
- franc
- quot
- asil
- accueil
- faut
- oblig
- besoin
- fix
- fonction
- integr
- fair
- économ
- migr
- parl
- polit
- annuel

### 4 - En qui faites-vous le plus confiance pour vous faire représenter dans la société et pourquoi ?

#### Statistiques générales sur les réponses

Nombre de réponses : 289691

Taille moyenne des réponses (caractères) : 145.72

Taille moyenne des réponses (mots) : 24.73

Taille maximum des réponses (mots) : 9291

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|maire|0.09258825492246711|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_maire.png "maire")|
|élus|0.062486345057959844|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_élus.png "élus")|
|député|0.038122682972748144|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_député.png "député")|
|maires|0.027587313657943886|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_maires.png "maires")|
|députés|0.027059391221273054|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_députés.png "députés")|
|citoyens|0.023353094640945704|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_citoyens.png "citoyens")|
|confiance|0.02250651099338917|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_confiance.png "confiance")|
|associations|0.018832549715569417|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_associations.png "associations")|
|proximité|0.018616758238829908|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_proximité.png "proximité")|
|locaux|0.018446474911808182|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_locaux.png "locaux")|

Racines de mots les plus importants dans les réponses :

- mair
- élus
- déput
- représent
- citoyen
- polit
- confianc
- local
- vot
- élu
- démocrat
- associ
- président
- part
- commun
- fair
- pouvoir
- franc
- national
- intérêt

### 5 - Faut-il faciliter le déclenchement du référendum d'initiative partagée (le RIP est organisé à l'initiative de membres du Parlement soutenu par une partie du corps électoral) qui est applicable depuis 2015 ?

#### Statistiques générales sur les réponses

Nombre de réponses : 307444

Taille moyenne des réponses (caractères) : 5.31

Taille moyenne des réponses (mots) : 1.63

Taille maximum des réponses (mots) : 4

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|oui|0.5208623359056849|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_oui.png "oui")|
|sais|0.2104513342268578|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_sais.png "sais")|

Racines de mots les plus importants dans les réponses :

- oui
- sais

### 6 - Faut-il prendre en compte le vote blanc ?

#### Statistiques générales sur les réponses

Nombre de réponses : 314030

#### Détail de la réponse fermées

Pourcentage de "oui" : 82.09%

Pourcentage de "Non" : 17.91%

### 7 - Le non-cumul des mandats instauré en 2017 pour les parlementaires (députés et sénateurs) est :

#### Statistiques générales sur les réponses

Nombre de réponses : 316723

Taille moyenne des réponses (caractères) : 15.32

Taille moyenne des réponses (mots) : 3.11

Taille maximum des réponses (mots) : 4

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|bonne|0.5673865337348706|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_bonne.png "bonne")|
|chose|0.5410852479166174|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_chose.png "chose")|
|mauvaise|0.1333521295102892|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_mauvaise.png "mauvaise")|
|sais|0.10729880684390296|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_sais.png "sais")|

Racines de mots les plus importants dans les réponses :

- chos
- bon
- mauvais
- sais

### 8 - Pensez-vous qu'il faille instaurer des contreparties aux différentes allocations de solidarité ?

#### Statistiques générales sur les réponses

Nombre de réponses : 270162

#### Détail de la réponse fermées

Pourcentage de "oui" : 73.19%

Pourcentage de "Non" : 26.81%

### 9 - Pensez-vous qu'il serait souhaitable de réduire le nombre d'élus (hors députés et sénateurs) ?

#### Statistiques générales sur les réponses

Nombre de réponses : 302108

#### Détail de la réponse fermées

Pourcentage de "oui" : 72.38%

Pourcentage de "Non" : 27.62%

### 10 - Que faudrait-il faire aujourd'hui pour mieux associer les citoyens aux grandes orientations et à la décision publique ? Comment mettre en place une démocratie plus participative ?

#### Statistiques générales sur les réponses

Nombre de réponses : 278734

Taille moyenne des réponses (caractères) : 192.94

Taille moyenne des réponses (mots) : 31.43

Taille maximum des réponses (mots) : 8083

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|référendum|0.04930449889401059|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_référendum.png "référendum")|
|citoyens|0.030523207907659555|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_citoyens.png "citoyens")|
|ric|0.02990038104547567|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_ric.png "ric")|
|référendums|0.023045918600710816|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_référendums.png "référendums")|
|faire|0.01985497429285095|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_faire.png "faire")|
|vote|0.016651322955487106|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_vote.png "vote")|
|internet|0.016212491053962483|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_internet.png "internet")|
|débat|0.016200234978399713|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_débat.png "débat")|
|referendum|0.01567488959261274|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_referendum.png "referendum")|
|élus|0.015542835526271972|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_élus.png "élus")|

Racines de mots les plus importants dans les réponses :

- citoyen
- référendum
- débat
- grand
- vot
- local
- particip
- fair
- consult
- décis
- élus
- national
- sort
- question
- polit
- démocrat
- plac
- niveau
- faut
- organis

### 11 - Que faudrait-il faire aujourd'hui pour renforcer l'engagement citoyen dans la société ?

#### Statistiques générales sur les réponses

Nombre de réponses : 235686

Taille moyenne des réponses (caractères) : 144.67

Taille moyenne des réponses (mots) : 23.88

Taille maximum des réponses (mots) : 6081

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|service|0.03329915212354945|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_service.png "service")|
|obligatoire|0.029511806030043445|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_obligatoire.png "obligatoire")|
|civique|0.02424808368458855|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_civique.png "civique")|
|citoyens|0.023057386561742537|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_citoyens.png "citoyens")|
|vote|0.022862103412250628|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_vote.png "vote")|
|citoyen|0.021000944599724337|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_citoyen.png "citoyen")|
|faire|0.01694331248709785|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_faire.png "faire")|
|engagement|0.01643797750674779|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_engagement.png "engagement")|
|éducation|0.016175680271843938|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_éducation.png "éducation")|
|militaire|0.01421750430594759|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_militaire.png "militaire")|

Racines de mots les plus importants dans les réponses :

- citoyen
- servic
- engag
- associ
- obligatoir
- civiqu
- fair
- vot
- don
- jeun
- écol
- societ
- polit
- particip
- respect
- éduc
- franc
- national
- vi
- faut

### 12 - Que faudrait-il faire pour consulter plus directement les citoyens sur l'utilisation de l'argent public, par l'Etat et les collectivités ?

#### Statistiques générales sur les réponses

Nombre de réponses : 255466

Taille moyenne des réponses (caractères) : 147.15

Taille moyenne des réponses (mots) : 24.08

Taille maximum des réponses (mots) : 4162

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|référendum|0.03378335772925214|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_référendum.png "référendum")|
|citoyens|0.026333342508919586|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_citoyens.png "citoyens")|
|internet|0.02558856136736636|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_internet.png "internet")|
|ric|0.0195643259108307|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_ric.png "ric")|
|faire|0.018700413506496993|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_faire.png "faire")|
|comptes|0.018595434249497483|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_comptes.png "comptes")|
|transparence|0.01613723424982734|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_transparence.png "transparence")|
|dépenses|0.016126684246584005|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_dépenses.png "dépenses")|
|argent|0.015871385523688664|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_argent.png "argent")|
|élus|0.013800961706843275|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_élus.png "élus")|

Racines de mots les plus importants dans les réponses :

- citoyen
- consult
- compt
- dépens
- public
- référendum
- fair
- argent
- utilis
- budget
- inform
- vot
- internet
- local
- publiqu
- élus
- grand
- cour
- transparent
- niveau

### 13 - Que faudrait-il faire pour favoriser le développement de ces comportements civiques et par quels engagements concrets chacun peut-il y participer ?

#### Statistiques générales sur les réponses

Nombre de réponses : 204929

Taille moyenne des réponses (caractères) : 146.04

Taille moyenne des réponses (mots) : 24.04

Taille maximum des réponses (mots) : 5753

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|éducation|0.0385747394831132|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_éducation.png "éducation")|
|école|0.02969962637574783|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_école.png "école")|
|civique|0.024234230158799136|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_civique.png "civique")|
|service|0.020082836117163626|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_service.png "service")|
|education|0.017257093080446238|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_education.png "education")|
|exemple|0.016450543500884103|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_exemple.png "exemple")|
|faire|0.014827635988785648|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_faire.png "faire")|
|parents|0.013916464468983753|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_parents.png "parents")|
|associations|0.01262903657731838|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_associations.png "associations")|
|respect|0.012214574447809308|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_respect.png "respect")|

Racines de mots les plus importants dans les réponses :

- écol
- éduc
- civiqu
- citoyen
- servic
- fair
- associ
- comport
- respect
- exempl
- jeun
- parent
- enfant
- faut
- don
- engag
- sanction
- aid
- vi
- enseign

### 14 - Que faudrait-il faire pour lutter contre ces discriminations et construire une société plus solidaire et plus tolérante ?

#### Statistiques générales sur les réponses

Nombre de réponses : 197670

Taille moyenne des réponses (caractères) : 135.52

Taille moyenne des réponses (mots) : 22.47

Taille maximum des réponses (mots) : 5753

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|éducation|0.0396244751818861|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_éducation.png "éducation")|
|education|0.019952953676908088|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_education.png "education")|
|éduquer|0.017823433839938268|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_éduquer.png "éduquer")|
|école|0.0175369560229533|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_école.png "école")|
|faire|0.016662431560572316|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_faire.png "faire")|
|eduquer|0.0124071600292045|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_eduquer.png "eduquer")|
|respect|0.011284361463705886|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_respect.png "respect")|
|société|0.010883891502614847|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_société.png "société")|
|tolérance|0.010122669186262973|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_tolérance.png "tolérance")|
|sanctionner|0.010095410880863387|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_sanctionner.png "sanctionner")|

Racines de mots les plus importants dans les réponses :

- éduc
- fair
- écol
- discrimin
- respect
- social
- toler
- societ
- faut
- franc
- sanction
- jeun
- éduqu
- enfant
- citoyen
- femm
- exempl
- égal
- educ
- arrêt

### 15 - Que faudrait-il faire pour mieux représenter les différentes sensibilités politiques ?

#### Statistiques générales sur les réponses

Nombre de réponses : 260642

Taille moyenne des réponses (caractères) : 128.94

Taille moyenne des réponses (mots) : 20.58

Taille maximum des réponses (mots) : 2544

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|proportionnelle|0.15337079304257595|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_proportionnelle.png "proportionnelle")|
|dose|0.05435368753693798|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_dose.png "dose")|
|élections|0.03247772198216188|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_élections.png "élections")|
|instaurer|0.023195892967363466|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_instaurer.png "instaurer")|
|vote|0.022973403631387702|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_vote.png "vote")|
|introduire|0.02204702272802706|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_introduire.png "introduire")|
|intégrale|0.018712907101002787|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_intégrale.png "intégrale")|
|proportionnel|0.018543601687059215|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_proportionnel.png "proportionnel")|
|législatives|0.017350267543515447|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_législatives.png "législatives")|
|assemblée|0.0172915149509952|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_assemblée.png "assemblée")|

Racines de mots les plus importants dans les réponses :

- proportionnel
- part
- polit
- dos
- représent
- élect
- vot
- assembl
- citoyen
- sensibil
- national
- déput
- élus
- major
- instaur
- législ
- faut
- introduir
- scrutin
- fair

### 16 - Que faudrait-il faire pour renouer le lien entre les citoyens et les élus qui les représentent ?

#### Statistiques générales sur les réponses

Nombre de réponses : 290274

Taille moyenne des réponses (caractères) : 242.11

Taille moyenne des réponses (mots) : 40.08

Taille maximum des réponses (mots) : 6986

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|élus|0.045164762148170653|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_élus.png "élus")|
|citoyens|0.030563188409118452|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_citoyens.png "citoyens")|
|faire|0.016418869122692293|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_faire.png "faire")|
|transparence|0.015864932212423057|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_transparence.png "transparence")|
|politique|0.012689790976094194|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_politique.png "politique")|
|élu|0.012200101577237589|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_élu.png "élu")|
|mandat|0.012193065443213363|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_mandat.png "mandat")|
|vie|0.01175363003686193|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_vie.png "vie")|
|vote|0.011411364328727268|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_vote.png "vote")|
|députés|0.01137928269841853|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_députés.png "députés")|

Racines de mots les plus importants dans les réponses :

- élus
- citoyen
- polit
- mandat
- vot
- fair
- représent
- déput
- élu
- faut
- part
- vi
- compt
- local
- pouvoir
- assembl
- élect
- franc
- commun
- national

### 17 - Que faudrait-il faire pour valoriser l'engagement citoyen dans les parcours de vie, dans les relations avec l'administration et les pouvoirs publics ?

#### Statistiques générales sur les réponses

Nombre de réponses : 167474

Taille moyenne des réponses (caractères) : 125.41

Taille moyenne des réponses (mots) : 20.5

Taille maximum des réponses (mots) : 5753

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|sais|0.025168662293206804|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_sais.png "sais")|
|citoyen|0.019359067393986133|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_citoyen.png "citoyen")|
|citoyens|0.018679555073647734|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_citoyens.png "citoyens")|
|administration|0.017664895572998933|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_administration.png "administration")|
|engagement|0.017555265731683364|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_engagement.png "engagement")|
|service|0.016706437314228564|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_service.png "service")|
|faire|0.013779732780709692|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_faire.png "faire")|
|publics|0.012968933775974651|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_publics.png "publics")|
|question|0.012727819995418325|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_question.png "question")|
|valoriser|0.01244339990567247|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_valoriser.png "valoriser")|

Racines de mots les plus importants dans les réponses :

- citoyen
- administr
- engag
- servic
- public
- fair
- valoris
- pouvoir
- associ
- vi
- don
- retrait
- faut
- respect
- exempl
- civiqu
- temp
- aid
- question
- publiqu

### 18 - Que pensez-vous de la participation des citoyens aux élections et comment les inciter à y participer davantage ?

#### Statistiques générales sur les réponses

Nombre de réponses : 284508

Taille moyenne des réponses (caractères) : 168.51

Taille moyenne des réponses (mots) : 28.26

Taille maximum des réponses (mots) : 2313

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|vote|0.11607638126909245|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_vote.png "vote")|
|obligatoire|0.10788272619151115|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_obligatoire.png "obligatoire")|
|blanc|0.033299930831001794|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_blanc.png "blanc")|
|citoyens|0.02374395999489513|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_citoyens.png "citoyens")|
|compte|0.023364787941410375|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_compte.png "compte")|
|participation|0.022268429538307953|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_participation.png "participation")|
|voter|0.02138388936248304|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_voter.png "voter")|
|faut|0.020413854476200755|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_faut.png "faut")|
|élections|0.018026793602629956|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_élections.png "élections")|
|élus|0.016603565239040417|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_élus.png "élus")|

Racines de mots les plus importants dans les réponses :

- vot
- obligatoir
- citoyen
- particip
- blanc
- polit
- élect
- faut
- élus
- compt
- fair
- représent
- faibl
- candidat
- part
- droit
- franc
- confianc
- démocrat
- pris

### 19 - Que pensez-vous de la situation de l'immigration en France aujourd'hui et de la politique migratoire ? Quelles sont, selon vous, les critères à mettre en place pour définir la politique migratoire ?

#### Statistiques générales sur les réponses

Nombre de réponses : 259397

Taille moyenne des réponses (caractères) : 240.27

Taille moyenne des réponses (mots) : 40.46

Taille maximum des réponses (mots) : 5753

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|immigration|0.04094690759505482|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_immigration.png "immigration")|
|pays|0.03447113977152414|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_pays.png "pays")|
|france|0.029902304224460923|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_france.png "france")|
|faut|0.02517390040237864|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_faut.png "faut")|
|politique|0.024039348310026194|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_politique.png "politique")|
|accueillir|0.021808026179719796|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_accueillir.png "accueillir")|
|migrants|0.02107267008046928|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_migrants.png "migrants")|
|quotas|0.01797663885389308|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_quotas.png "quotas")|
|accueil|0.016714323859485947|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_accueil.png "accueil")|
|asile|0.015389298724804285|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_asile.png "asile")|

Racines de mots les plus importants dans les réponses :

- immigr
- franc
- pay
- accueil
- polit
- faut
- migr
- integr
- migratoir
- aid
- économ
- droit
- fair
- asil
- besoin
- situat
- quot
- criter
- problem
- accept

### 20 - Que peuvent et doivent faire les pouvoirs publics pour répondre aux incivilités ?

#### Statistiques générales sur les réponses

Nombre de réponses : 241040

Taille moyenne des réponses (caractères) : 115.79

Taille moyenne des réponses (mots) : 18.84

Taille maximum des réponses (mots) : 5753

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|sanctionner|0.037347539909807895|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_sanctionner.png "sanctionner")|
|faire|0.026143475830507322|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_faire.png "faire")|
|appliquer|0.02368944564369204|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_appliquer.png "appliquer")|
|loi|0.023110603354077813|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_loi.png "loi")|
|éducation|0.020184637330756375|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_éducation.png "éducation")|
|sanctions|0.018519981454694776|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_sanctions.png "sanctions")|
|amendes|0.018268997725583054|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_amendes.png "amendes")|
|punir|0.015012834130478202|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_punir.png "punir")|
|lois|0.014309309049419829|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_lois.png "lois")|
|éduquer|0.013999864882340325|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_éduquer.png "éduquer")|

Racines de mots les plus importants dans les réponses :

- sanction
- fair
- incivil
- appliqu
- éduc
- amend
- loi
- respect
- polic
- intérêt
- traval
- général
- justic
- faut
- pein
- exempl
- lois
- écol
- mettr
- pun

### 21 - Que proposez-vous afin de répondre à ce défi qui va durer ?

#### Statistiques générales sur les réponses

Nombre de réponses : 235735

Taille moyenne des réponses (caractères) : 174.72

Taille moyenne des réponses (mots) : 29.07

Taille maximum des réponses (mots) : 5753

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|pays|0.04768077746976889|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_pays.png "pays")|
|aider|0.023296882656574674|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_aider.png "aider")|
|immigration|0.021922986840655048|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_immigration.png "immigration")|
|migrants|0.017158217696261104|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_migrants.png "migrants")|
|faut|0.016114113650469594|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_faut.png "faut")|
|politique|0.016040882012442702|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_politique.png "politique")|
|voir|0.01549003689756003|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_voir.png "voir")|
|faire|0.015483458263548164|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_faire.png "faire")|
|développement|0.01512337553495886|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_développement.png "développement")|
|france|0.01490672326788802|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_france.png "france")|

Racines de mots les plus importants dans les réponses :

- pay
- aid
- immigr
- franc
- accueil
- développ
- migr
- polit
- faut
- integr
- fair
- européen
- économ
- origin
- fronti
- popul
- droit
- plac
- europ
- mettr

### 22 - Que proposez-vous pour renforcer les principes de la laïcité dans le rapport entre l'Etat et les religions de notre pays ?

#### Statistiques générales sur les réponses

Nombre de réponses : 250414

Taille moyenne des réponses (caractères) : 193.2

Taille moyenne des réponses (mots) : 32.59

Taille maximum des réponses (mots) : 5753

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|loi|0.04333453537487667|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_loi.png "loi")|
|religions|0.03262893692602248|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_religions.png "religions")|
|religion|0.030134406587066287|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_religion.png "religion")|
|laïcité|0.030105638303334924|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_laïcité.png "laïcité")|
|1905|0.02905205069647162|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_1905.png "1905")|
|appliquer|0.027261017883050718|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_appliquer.png "appliquer")|
|faire|0.022007594833643517|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_faire.png "faire")|
|religieux|0.01928319871709288|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_religieux.png "religieux")|
|lois|0.01918072603273239|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_lois.png "lois")|
|respecter|0.018058732514247524|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_respecter.png "respecter")|

Racines de mots les plus importants dans les réponses :

- relig
- religion
- religi
- laïcit
- loi
- respect
- franc
- appliqu
- fair
- écol
- princip
- 1905
- public
- cult
- sign
- faut
- pay
- etat
- lois
- républ

### 23 - Quel pourrait être le rôle de chacun pour faire reculer les incivilités dans la société ?

#### Statistiques générales sur les réponses

Nombre de réponses : 196499

Taille moyenne des réponses (caractères) : 93.5

Taille moyenne des réponses (mots) : 15.94

Taille maximum des réponses (mots) : 5753

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|exemple|0.03197438068233973|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_exemple.png "exemple")|
|éducation|0.025620607602369172|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_éducation.png "éducation")|
|faire|0.025113938006436652|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_faire.png "faire")|
|enfants|0.02297388586920372|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_enfants.png "enfants")|
|respect|0.020667404756045307|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_respect.png "respect")|
|respecter|0.018070428383535554|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_respecter.png "respecter")|
|montrer|0.017641013073360953|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_montrer.png "montrer")|
|éduquer|0.015910935140105536|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_éduquer.png "éduquer")|
|dénoncer|0.015598847191987035|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_dénoncer.png "dénoncer")|
|incivilités|0.015319704336474168|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_incivilités.png "incivilités")|

Racines de mots les plus importants dans les réponses :

- fair
- incivil
- respect
- exempl
- enfant
- éduc
- citoyen
- parent
- comport
- rôl
- éduqu
- montr
- dénonc
- don
- interven
- respons
- faut
- pouvoir
- polic
- écol

### 24 - Quel rôle nos assemblées, dont le Sénat et le Conseil économique, social et environnemental, doivent-elles jouer pour représenter nos territoires et la société civile ?

#### Statistiques générales sur les réponses

Nombre de réponses : 214323

Taille moyenne des réponses (caractères) : 148.27

Taille moyenne des réponses (mots) : 24.85

Taille maximum des réponses (mots) : 1717

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|rôle|0.033002300141341166|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_rôle.png "rôle")|
|sénat|0.03248306672401724|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_sénat.png "sénat")|
|sais|0.029591077059420087|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_sais.png "sais")|
|cese|0.02585230945490176|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_cese.png "cese")|
|citoyens|0.023627671841417404|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_citoyens.png "citoyens")|
|supprimer|0.022481768547742614|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_supprimer.png "supprimer")|
|conseil|0.02017485366024986|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_conseil.png "conseil")|
|économique|0.01568601774681838|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_économique.png "économique")|
|assemblée|0.015119017403483908|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_assemblée.png "assemblée")|
|assemblées|0.0147891087937499|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_assemblées.png "assemblées")|

Racines de mots les plus importants dans les réponses :

- sénat
- rôl
- assembl
- citoyen
- représent
- ces
- conseil
- supprim
- économ
- territoir
- social
- élus
- pouvoir
- fair
- faut
- national
- lois
- polit
- societ
- compt

### 25 - Quelles sont les discriminations les plus répandues dont vous êtes témoin ou victime ?

#### Statistiques générales sur les réponses

Nombre de réponses : 199373

Taille moyenne des réponses (caractères) : 94.29

Taille moyenne des réponses (mots) : 15.51

Taille maximum des réponses (mots) : 1832

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|racisme|0.07930830219791092|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_racisme.png "racisme")|
|sexisme|0.03687983697425204|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_sexisme.png "sexisme")|
|discrimination|0.034172446359797035|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_discrimination.png "discrimination")|
|homophobie|0.0330255041179052|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_homophobie.png "homophobie")|
|femmes|0.032603946391504955|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_femmes.png "femmes")|
|discriminations|0.027577544904643054|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_discriminations.png "discriminations")|
|anti|0.016204437831883255|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_anti.png "anti")|
|respect|0.01458049357562819|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_respect.png "respect")|
|raciales|0.014074343449152586|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_raciales.png "raciales")|
|femme|0.013998041593802288|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_femme.png "femme")|

Racines de mots les plus importants dans les réponses :

- discrimin
- racism
- femm
- homophob
- sexism
- social
- franc
- homm
- handicap
- anti
- respect
- racial
- blanc
- vis
- origin
- témoin
- travail
- couleur
- jeun
- victim

### 26 - Quelles sont les incivilités les plus pénibles dans la vie quotidienne et que faudrait-il faire pour lutter contre ces incivilités ?

#### Statistiques générales sur les réponses

Nombre de réponses : 243582

Taille moyenne des réponses (caractères) : 163.43

Taille moyenne des réponses (mots) : 26.75

Taille maximum des réponses (mots) : 5753

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|respect|0.04961078732288744|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_respect.png "respect")|
|manque|0.025954419746743486|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_manque.png "manque")|
|incivilités|0.01824362694205574|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_incivilités.png "incivilités")|
|insultes|0.01587344813928446|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_insultes.png "insultes")|
|biens|0.015664689398223103|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_biens.png "biens")|
|publics|0.015603514012841654|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_publics.png "publics")|
|violence|0.014919048365580818|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_violence.png "violence")|
|éducation|0.01478162636455622|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_éducation.png "éducation")|
|dégradations|0.014757115639037217|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_dégradations.png "dégradations")|
|déchets|0.014234008836433587|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_déchets.png "déchets")|

Racines de mots les plus importants dans les réponses :

- respect
- incivil
- public
- manqu
- dégrad
- agress
- violenc
- fair
- ru
- insult
- sanction
- rout
- éduc
- faut
- déchet
- comport
- vol
- jet
- publiqu
- bien

### 27 - Quelles sont, selon vous, les modalités d'intégration les plus efficaces et les plus justes à mettre en place aujourd'hui dans la société ?

#### Statistiques générales sur les réponses

Nombre de réponses : 237491

Taille moyenne des réponses (caractères) : 151.67

Taille moyenne des réponses (mots) : 25.1

Taille maximum des réponses (mots) : 5753

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|travail|0.04735047566176957|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_travail.png "travail")|
|langue|0.04407171858855422|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_langue.png "langue")|
|français|0.03516471204509106|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_français.png "français")|
|apprentissage|0.030427884493551292|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_apprentissage.png "apprentissage")|
|éducation|0.028954848044739162|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_éducation.png "éducation")|
|intégration|0.024086522102524953|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_intégration.png "intégration")|
|française|0.023143940834334607|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_française.png "française")|
|apprendre|0.02279951912909503|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_apprendre.png "apprendre")|
|formation|0.02254197222111761|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_formation.png "formation")|
|école|0.022127242394395116|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_école.png "école")|

Racines de mots les plus importants dans les réponses :

- franc
- integr
- langu
- travail
- français
- pay
- apprentissag
- immigr
- respect
- format
- apprendr
- accueil
- éduc
- valeur
- faut
- aid
- fair
- écol
- migr
- droit

### 28 - Quels sont les comportements civiques qu'il faut promouvoir dans notre vie quotidienne ou collective ?

#### Statistiques générales sur les réponses

Nombre de réponses : 236399

Taille moyenne des réponses (caractères) : 110.42

Taille moyenne des réponses (mots) : 18.33

Taille maximum des réponses (mots) : 5753

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|respect|0.1265637923963278|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_respect.png "respect")|
|solidarité|0.02658615206220745|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_solidarité.png "solidarité")|
|politesse|0.02633862707422614|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_politesse.png "politesse")|
|tolérance|0.025103096688158872|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_tolérance.png "tolérance")|
|entraide|0.024172255626223667|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_entraide.png "entraide")|
|environnement|0.016399010139147383|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_environnement.png "environnement")|
|engagement|0.013290816083323179|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_engagement.png "engagement")|
|biens|0.012612538784049587|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_biens.png "biens")|
|lois|0.012491431081609602|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_lois.png "lois")|
|aide|0.012180485988856559|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_aide.png "aide")|

Racines de mots les plus importants dans les réponses :

- respect
- politess
- solidar
- comport
- citoyen
- toler
- aid
- associ
- entraid
- vi
- fair
- public
- engag
- environ
- civiqu
- faut
- collect
- commun
- regl
- écol

### 29 - Si oui, à quel type d'associations ou d'organisations ? Et avec quel rôle ?

#### Statistiques générales sur les réponses

Nombre de réponses : 184380

Taille moyenne des réponses (caractères) : 170.56

Taille moyenne des réponses (mots) : 26.31

Taille maximum des réponses (mots) : 1805

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|associations|0.06279653320827701|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_associations.png "associations")|
|syndicats|0.057404029624218436|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_syndicats.png "syndicats")|
|organisations|0.03262148457193477|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_organisations.png "organisations")|
|syndicales|0.024192680747664723|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_syndicales.png "syndicales")|
|rôle|0.023994333589481887|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_rôle.png "rôle")|
|citoyens|0.021722685755653028|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_citoyens.png "citoyens")|
|association|0.018697528081027377|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_association.png "association")|
|ong|0.016490590495397386|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_ong.png "ong")|
|professionnelles|0.016367419933227267|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_professionnelles.png "professionnelles")|
|consommateurs|0.014382630058771908|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_consommateurs.png "consommateurs")|

Racines de mots les plus importants dans les réponses :

- associ
- syndicat
- organis
- citoyen
- rôl
- représent
- syndical
- social
- professionnel
- polit
- consult
- pouvoir
- faut
- fair
- intérêt
- entrepris
- salari
- local
- proposit
- don

### 30 - Y a-t-il d'autres points sur la démocratie et la citoyenneté sur lesquels vous souhaiteriez vous exprimer ?

#### Statistiques générales sur les réponses

Nombre de réponses : 182753

Taille moyenne des réponses (caractères) : 474.7

Taille moyenne des réponses (mots) : 78.75

Taille maximum des réponses (mots) : 55831

#### Thèmes majoritaires dans la question ouverte :

Mots les plus importants dans les réponses :


|MOT|SCORE_TFIDF|GRAPHE|
|--|--|--|
|démocratie|0.017315533819091154|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_démocratie.png "démocratie")|
|faut|0.015794955640409867|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_faut.png "faut")|
|faire|0.013781148960097914|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_faire.png "faire")|
|france|0.013760097513475343|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_france.png "france")|
|citoyens|0.013630612069624477|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_citoyens.png "citoyens")|
|français|0.013173410435511995|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_français.png "français")|
|pays|0.013048386897777937|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_pays.png "pays")|
|élus|0.012402231158529115|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_élus.png "élus")|
|droit|0.01102320334270824|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_droit.png "droit")|
|vote|0.009948847677518068|[graph](https://raw.githubusercontent.com/MrMimic/GJ_GrandDebat/master/words/DEMOCRATIE_ET_CITOYENNETE_vote.png "vote")|

Racines de mots les plus importants dans les réponses :

- franc
- citoyen
- démocrat
- faut
- fair
- polit
- pay
- droit
- vot
- national
- pouvoir
- élus
- grand
- part
- vi
- social
- an
- respect
- président
- représent

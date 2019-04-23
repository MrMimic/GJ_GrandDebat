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

******************

# Rapport automatique

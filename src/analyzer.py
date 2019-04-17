#/usr/bin/env python3
"""
analyzer.py
============================
This script will batch analyse downloaded data.
"""

import re
import os
import json
import itertools
import pandas as pd



class ANALYZER():

    def __init__(self):
        """"""
        self.data_dir = 'data'

    def write_json_file_from_dict(self, dictionnary, file_name):
        """"""
        with open(file_name, 'w') as handler:
            handler.write(json.dumps(dictionnary, indent=2, ensure_ascii=True))

    def analyse_participants_zip_codes(self, theme):
        """"""

        seen_zip_codes = dict()
        seen_departments = dict()

        # Zip codes analysis
        for csv_file in [file_name for file_name in os.listdir(os.path.join(self.data_dir, theme)) if file_name.endswith('csv')]:
            csv_data = pd.read_csv(os.path.join(self.data_dir, theme, csv_file), low_memory=False)
            # Using pandas counter cause of layzyness
            zip_codes_counts = csv_data['authorZipCode'].value_counts()
            for zip_code, count in zip(csv_data['authorZipCode'], zip_codes_counts):
                try:
                    seen_zip_codes[zip_code] += count
                except KeyError as error:
                    seen_zip_codes[zip_code] = count
        self.write_json_file_from_dict(dictionnary=seen_zip_codes, file_name=os.path.join(self.data_dir, theme, 'zip_codes.json'))

        # Seen departments
        for zip_code, count in seen_zip_codes.items():
            department = str(zip_code)[:2]
            try:
                seen_departments[department] += count
            except KeyError as error:
                seen_departments[department] = count
        self.write_json_file_from_dict(dictionnary=seen_departments, file_name=os.path.join(self.data_dir, theme, 'departments.json'))

    def analyse_specific_question(self, data_dir, theme_folder, question):
        """
        The input will be a folder about a specific subject
        We should parse all files from this folder whil all have the same shape (and same questions)
        However, they cannot be joined into one big csv due to the number of columns, differents for each
        """

        # First, we gonna read all CSV about a specific theme and then keep all answers about this question from all 4 files
        total_answers = list()
        for file_name in os.listdir(os.path.join(data_dir, theme_folder)):
            if file_name.endswith('csv') and theme_folder in file_name:
                # Extract data
                csv_data = pd.read_csv(os.path.join(data_dir, theme_folder, file_name), low_memory=False, encoding = 'utf8')
                try:
                    answers = list(csv_data[question].dropna())
                except KeyError:
                    # Of course, header are not the same, we should correct it
                    corrected_question = [header_title for header_title in csv_data.head() if question in header_title][0]
                    answers = list(csv_data[corrected_question].dropna())
                total_answers.extend(answers[1:]) # We remove the first element because of header
        print('Extracted {} answers from files (question: "{}")'.format(len(total_answers), question))

        # Now, these question will be analysed by TF-IDF and ambedded as vector to be used as machine learning input


if __name__ == '__main__':
    A = ANALYZER()
    etat = 'ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS'
    A.analyse_specific_question('data', etat, "Que pensez-vous de l'organisation de l'Etat et des administrations en France ? De quelle manière cette organisation devrait-elle évoluer ?")

    """
    Que pensez-vous de l'organisation de l'Etat et des administrations en France ? De quelle manière cette organisation devrait-elle évoluer ?
    Selon vous, l'Etat doit-il aujourd'hui transférer de nouvelles missions aux collectivités territoriales ?
    Si oui, lesquelles ?
    Estimez-vous avoir accès aux services publics dont vous avez besoin ?
    Si non, quels types de services publics vous manquent dans votre territoire et qu'il est nécessaire de renforcer ?
    Quels nouveaux services ou quelles démarches souhaitez-vous voir développées sur Internet en priorité ?
    Avez-vous déjà utilisé certaines de ces nouvelles formes de services publics ?
    Si oui, en avez-vous été satisfait ?
    Quelles améliorations préconiseriez-vous ?
    Quand vous pensez à l'évolution des services publics au cours des dernières années, quels sont ceux qui ont évolué de manière positive ?
    Quels sont les services publics qui doivent le plus évoluer selon vous ?
    Connaissez-vous le "droit à l'erreur", c'est-à-dire le droit d'affirmer votre bonne foi lorsque vous faites un erreur dans vos déclarations ?
    Si oui, avez-vous déjà utilisé ce droit à l'erreur ?
    Si oui, à quelle occasion en avez-vous fait usage ?
    Pouvez-vous identifier des règles que l'administration vous a déjà demandé d'appliquer et que vous avez jugées inutiles ou trop complexes ?
    Faut-il donner plus d'autonomie aux fonctionnaires de terrain ?
    Si oui, comment ?
    Faut-il revoir le fonctionnement et la formation de l'administration ?
    Comment l'Etat et les collectivités territoriales peuvent-ils s'améliorer pour mieux répondre aux défis de nos territoires les plus en difficulté ?
    Si vous avez été amené à chercher une formation, pouvez-vous indiquer les éléments de satisfaction et/ou les difficultés rencontrés en précisant, pour chaque point, l'administration concernée :
    Si vous avez été amené à scolariser votre enfant, pouvez-vous indiquer les éléments de satisfaction et/ou les difficultés rencontrés en précisant, pour chaque point, l'administration concernée :
    Si vous avez été amené à chercher un emploi, pouvez-vous indiquer les éléments de satisfaction et/ou les difficultés rencontrés en précisant, pour chaque point, l'administration concernée :
    Si vous avez été amené à préparer votre retraite, pouvez-vous indiquer les éléments de satisfaction et/ou les difficultés rencontrés en précisant, pour chaque point, l'administration concernée :
    Si vous avez été amené à demander un remboursement de soins de santé, pouvez-vous indiquer les éléments de satisfaction et/ou les difficultés rencontrés en précisant, pour chaque point, l'administration concernée :
    Si vous avez été amené à faire une demande d'aide pour une situation de handicap, pouvez-vous indiquer les éléments de satisfaction et/ou les difficultés rencontrés en précisant, pour chaque point, l'administration concernée :
    Si vous avez été amené à créer une entreprise, pouvez-vous indiquer les éléments de satisfaction et/ou les difficultés rencontrés en précisant, pour chaque point, l'administration concernée :
    Si vous avez été amené à recruter du personnel, pouvez-vous indiquer les éléments de satisfaction et/ou les difficultés rencontrés en précisant, pour chaque point, l'administration concernée :
    Si vous avez été amené à former du personnel, pouvez-vous indiquer les éléments de satisfaction et/ou les difficultés rencontrés en précisant, pour chaque point, l'administration concernée :
    Si vous avez été amené à rémunérer du personnel, pouvez-vous indiquer les éléments de satisfaction et/ou les difficultés rencontrés en précisant, pour chaque point, l'administration concernée :
    Si vous avez été amené à mettre fin à votre activité, pouvez-vous indiquer les éléments de satisfaction et/ou les difficultés rencontrés en précisant, pour chaque point, l'administration concernée :
    Si vous avez été amené à recruter une personne portant un handicap, pouvez-vous indiquer les éléments de satisfaction et/ou les difficultés rencontrés en précisant, pour chaque point, l'administration concernée :
    Y a-t-il d'autres points sur l'organisation de l'Etat et des services publics sur lesquels vous souhaiteriez vous exprimer ?
    """

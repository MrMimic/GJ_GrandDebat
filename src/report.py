#!/usr/bin/env python3

import sys

sys.path.append('./')
from writer import MARKDOWN


class REPORT():
    """
    This class will handler reporting data for all question from this debat
    """
    def __init__(self):

        # Data for the markdown report
        self.debat_theme = None
        self.studied_question = None

        # Stats about answers string themselves (average length, number, number of misspells ...)
        self.number_of_answers = None
        self.average_chars_length = None
        self.average_tokens_length = None
        self.max_token_length = None

        # Open or close question
        self.question_type = None

        # Close question
        self.percentage_yes = None
        self.percentage_no = None

        # Stats coming from TF-IDF data
        self.max_used_token = None
        self.max_used_token_count = None
        self.top_20_terms = None
        self.top_20_stems = None

    def write_to_file(self, report_file=None):
        """"""

        # Writer class
        writer = MARKDOWN()

        if report_file is not None:
            writer.write_title_lvl_4(string='Statistiques générales sur les réponses', file_name=report_file)
            writer.write_string(string='Nombre de réponses : {}'.format(self.number_of_answers), file_name=report_file)

            if self.question_type == 'open':

                writer.write_string(string='Taille moyenne des réponses (caractères) : {}'.format(self.average_chars_length), file_name=report_file)
                writer.write_string(string='Taille moyenne des réponses (mots) : {}'.format(self.average_tokens_length), file_name=report_file)
                writer.write_string(string='Taille maximum des réponses (mots) : {}'.format(self.max_token_length), file_name=report_file)

                writer.write_title_lvl_4(string='Thèmes majoritaires dans la question ouverte :', file_name=report_file)
                writer.write_string(string='Mots les plus importants dans les réponses :', file_name=report_file)
                writer.write_itemize_list(list_to_itemize=self.top_20_terms, file_name=report_file)
                writer.write_string(string='Racines de mots les plus importants dans les réponses :', file_name=report_file)
                writer.write_itemize_list(list_to_itemize=self.top_20_stems, file_name=report_file)

            else:
                writer.write_title_lvl_4(string='Détail de la réponse fermées', file_name=report_file)
                writer.write_string(string='Pourcentage de "oui" : {}%'.format(self.percentage_yes), file_name=report_file)
                writer.write_string(string='Pourcentage de "Non" : {}%'.format(self.percentage_no), file_name=report_file)

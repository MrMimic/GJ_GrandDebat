#/usr/bin/env python3

import sys
import argparse

sys.path.append('src')

from analyzer import ANALYZER
from downloader import DOWNLOADER
from cartographier import CARTOGRAPHIER
from writer import MARKDOWN


class EXECUTOR(object):

    def __init__(self):

        self.report_file = '/home/emeric/Desktop/GJ_GrandDebat/README.md'
        self.data_dir = 'data'

        self.etat = 'ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS'
        self.ecologie = 'LA_TRANSITION_ECOLOGIQUE'
        self.fiscalite = 'LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES'
        self.democratie = 'DEMOCRATIE_ET_CITOYENNETE'

        self.downloader = DOWNLOADER()
        self.analyzer = ANALYZER(report_file=self.report_file)
        self.cartographier = CARTOGRAPHIER()
        self.writer = MARKDOWN()

if __name__ == '__main__':

    # Get arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--download_data', action='store_true', help='Download base data on data.gouv.fr.')
    parser.add_argument('-m', '--draw_maps', action='store_true', help='Draw maps for each theme')
    parser.add_argument('-a', '--analyse_data_tfidf', action='store_true', help='Analyse raw data for plots, maps, etc.')
    parser.add_argument('-t', '--train_we', action='store_true', help='Train word embeddings specifics to each question.')
    args = parser.parse_args()

    # Main executor
    executor = EXECUTOR()

    # Download raw data from data.gouv.fr
    if args.download_data is True:
        executor.downloader.get_distant_data()

    for theme in [executor.etat, executor.ecologie, executor.fiscalite, executor.democratie]:

        # Write theme in report as section title
        print('\n{}\n'.format(theme))
        executor.writer.write_title_lvl_2(string=theme.replace('_', ' '), file_name=executor.report_file)

        # Draw a map for each theme with zip codes from answers
        if args.draw_maps is True:
            executor.analyzer.analyse_participants_zip_codes(theme)
            image_path = executor.cartographier.draw_french_map(theme=theme)
            executor.writer.write_title_lvl_3(string='Carte de participation', file_name=executor.report_file)
            executor.writer.include_image(image_path=image_path, alt_text=theme, file_name=executor.report_file)

        # Now, let's extract questions for this particular theme
        questions = executor.analyzer.extract_questions_from_theme(theme)

        # Analyse questions, one by one
        for indice, question in enumerate(questions):
            indice += 1
            print('\t{} : {}'.format(indice, question))

            # Do TFIDF or frequencies (depending open or close question)
            if args.analyse_data_tfidf is True:
                executor.writer.write_title_lvl_3(string='{} - {}'.format(indice, question), file_name=executor.report_file)
                executor.analyzer.analyse_specific_question(theme_folder=theme, question=question, indice=indice)

            # Train a word embedding specific to this question
            if args.train_we is True:
                total_answers = executor.analyzer.get_answers_to_question(data_dir=executor.data_dir, theme_folder=theme, question=question)
                # We don't need WE for close questions
                if len(list(set(total_answers))) > 2:
                    executor.analyzer.train_word_embedding(theme_folder=theme, question=question, documents=total_answers)


        # Then, train a global D2V to see if 4 cluster are found

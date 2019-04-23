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

        self.etat = 'ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS'
        self.ecologie = 'LA_TRANSITION_ECOLOGIQUE'
        self.fiscalite = 'LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES'
        self.democratie = 'DEMOCRATIE_ET_CITOYENNETE'

        self.downloader = DOWNLOADER()
        self.analyzer = ANALYZER(report_file=self.report_file)
        self.cartographier = CARTOGRAPHIER()
        self.writer = MARKDOWN()

if __name__ == '__main__':

    # PARAMETERS
    parser = argparse.ArgumentParser()
    parser.add_argument(  # Download distant data from data.gouv.fr
        '-d',
        '--download_data',
        action='store_true',
        help='Download base data on data.gouv.fr.')
    parser.add_argument(  # Full update of MELoDiST models.
        '-r',
        '--re_analyse_data',
        action='store_true',
        help='Re-analyse raw data before plots, maps, etc.')
    parser.add_argument(  # Draw differents maps after raw data has been analyzed.
        '-m',
        '--draw_maps',
        action='store_true',
        help='Use analyzed data to draw static maps.')
    args = parser.parse_args()

    # MAIN EXECUTOR
    executor = EXECUTOR()

    # DOWNLOAD RAW DATA
    if args.download_data is True:
        executor.downloader.get_distant_data()

    for theme in [executor.etat, executor.ecologie, executor.fiscalite, executor.democratie]:

        executor.writer.write_title_lvl_2(string=theme.replace('_', ' '), file_name=executor.report_file)

        if args.re_analyse_data is True:

            # Draw a map based on participants zip codes
            #######executor.analyzer.analyse_participants_zip_codes(theme)

            # Now, let's get questions
            questions = executor.analyzer.extract_questions_from_theme(theme)
            # And analyse them one by one
            for indice, question in enumerate(questions):
                indice += 1
                executor.writer.write_title_lvl_3(string='{} - {}'.format(indice, question), file_name=executor.report_file)
                executor.analyzer.analyse_specific_question(theme_folder=theme, question=question, indice=indice)

        # DRAW MAPS ON THIS THEME
        if args.draw_maps is True:
            executor.cartographier.draw_french_map(theme)

        # HERE, FIND QUESTION AND ANALYSE SPECIFIC QUESTION OF EACH THEME

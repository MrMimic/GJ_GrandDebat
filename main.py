#/usr/bin/env python3

import sys
import argparse

sys.path.append('src')

from analyzer import ANALYZER
from downloader import DOWNLOADER
from cartographier import CARTOGRAPHIER


class EXECUTOR(object):

    def __init__(self):

        self.etat = 'ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS'
        self.ecologie = 'LA_TRANSITION_ECOLOGIQUE'
        self.fiscalite = 'LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES'
        self.democratie = 'DEMOCRATIE_ET_CITOYENNETE'

        self.downloader = DOWNLOADER()
        self.analyzer = ANALYZER()
        self.cartographier = CARTOGRAPHIER()

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

        if args.re_analyse_data is True:
            # ANALYZE THIS THEME
            executor.analyzer.analyse_participants_zip_codes(theme)

        # DRAW MAPS ON THIS THEME
        if args.draw_maps is True:
            executor.cartographier.draw_french_map(theme)

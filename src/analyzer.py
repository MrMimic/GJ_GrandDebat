#/usr/bin/env python3
"""
analyzer.py
============================
This script will batch analyse downloaded data.
"""

import os
import json
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

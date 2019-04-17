#/usr/bin/env python3
#coding: utf-8

"""
downloader.py
============================
This script will download locally all data released by the French gov.
"""

import re
import os
import sys
import time
import json
import requests
import datetime
from bs4 import BeautifulSoup as BS


class DOWNLOADER():

    def __init__(self):
        """"""
        self.base_url = 'https://granddebat.fr/pages/donnees-ouvertes'
        self.data_dir = 'data'

    def get_distant_data(self):
        """"""
        # Get home page
        data = requests.get(self.base_url).text
        data = BS(data, 'lxml')
        # Index links ending with "json"
        for link in data.find_all('a'):
            if link.get('href').endswith('csv'):
                file_name = link.get('href').split('net/')[1].replace('/', '_')
                file_link = link.get('href')
                folder_name = re.sub('[0-9]{4}-[0-9]{2}-[0-9]{2}_', '', file_name.replace('.csv', ''))
                # Make folder if absent
                if folder_name not in os.listdir(self.data_dir):
                    os.mkdir(os.path.join(self.data_dir, folder_name))
                # Download the file content and write it locally
                if file_name not in os.listdir('data'):
                    tic = time.time()

                    try:
                        file_content = requests.get(file_link)
                        # Files were encoded with shitty ISO-8859-1
                        file_content.encoding = 'utf8'
                        with open(os.path.join(self.data_dir, folder_name, file_name), 'w', encoding='utf8') as handler:
                            handler.write(file_content.text)
                    except Exception as error:
                        with open('data/error.log', 'a') as error_handler:
                            error_handler.write('{}\t{}\t{}\n'.format(datetime.datetime.now(), error, file_name))
                            print('{}\t{}\t{}'.format(datetime.datetime.now(), error, file_name))
                            continue

                    toc = time.time()
                    print('{} downloaded ({} secs).'.format(file_name, round(toc-tic, 2)))

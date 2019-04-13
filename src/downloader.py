#/usr/bin/env python3
"""
downloader.py
============================
This script will download locally all data released by the French gov.
"""

import requests
from bs4 import BeautifulSoup as BS


class DOWNLOADER():
    def __init__(self):
        """"""
        self.base_url = "https://granddebat.fr/pages/donnees-ouvertes"

    def scan_page(self):
        """"""
        data = requests.get(self.base_url).text
        data = BS(data, 'lxml')
        for link in data.find_all('a'):
            if link.get('href').endswith('json'):
                file_name =
                link = link.get('href')



if __name__ == '__main__':

    D =DOWNLOADER()
    D.scan_page()

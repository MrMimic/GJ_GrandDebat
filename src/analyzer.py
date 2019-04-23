#/usr/bin/env python3
"""
analyzer.py
============================
This script will batch analyse downloaded data.
"""



import re
import os
import sys
import json
import time
import unidecode
import itertools
import numpy as np
import pandas as pd
from collections import Counter
from gensim.models import Word2Vec
from nltk.stem.snowball import FrenchStemmer
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

sys.path.append('./')
from report import REPORT



class ANALYZER():

    def __init__(self, report_file):
        """"""

        self.data_dir = 'data'
        self.report_file = report_file

        # Get stopwords (see README for source)
        with open(os.path.join(self.data_dir, 'stopwords', 'stopwords-fr.txt'), 'r') as file_handler:
            self.stopwords = [word.strip('\n') for word in file_handler.readlines()]

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

    def extract_questions_from_theme(self, theme):
        """Extracts question from a specific theme header"""

        theme_questions = list()

        # Parse each file from a specific theme
        for file_name in os.listdir(os.path.join(self.data_dir, theme)):
            if file_name.endswith('csv') and theme in file_name:
                # Extract data and headers
                csv_data = pd.read_csv(os.path.join(self.data_dir, theme, file_name), low_memory=False, encoding = 'utf8')
                questions = [header if ' - ' not in header else header.split(' - ')[1] for header in csv_data.columns.values if len(header) > 50]
                # ANd keep possible questions
                for question in questions:
                    theme_questions.append(question)

        return sorted(list(set(theme_questions)))

    def get_answers_to_question(self, data_dir, theme_folder, question):
        """"""

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

        return total_answers

    def analyse_specific_question(self, theme_folder, question, indice):
        """
        The input will be a folder about a specific subject
        We should parse all files from this folder whil all have the same shape (and same questions)
        However, they cannot be joined into one big csv due to the number of columns, differents for each
        """

        data_dir = self.data_dir

        # Create subdir in results/ and question-specific dir in this subdir
        if theme_folder not in os.listdir('results'):
            os.mkdir(os.path.join('results', theme_folder))
        # Question-specific folder
        question_folder = unidecode.unidecode(question[:70].lower().replace(' ', '_').replace("'", '').replace(',', '').replace('/', ''))
        if question_folder not in os.listdir(os.path.join('results', theme_folder)):
            os.mkdir(os.path.join('results', theme_folder, question_folder))
        # Get path to record results
        results_records_path = os.path.join('results', theme_folder, question_folder)

        # Create report class which will be markdown-formatted
        report = REPORT()
        report.debat_theme = theme_folder.replace('_', ' ')
        report.studied_question = '{} - {}'.format(indice, question)

        # Get answers for this specific question
        total_answers = self.get_answers_to_question(data_dir=self.data_dir, theme_folder=theme_folder, question=question)
        report.number_of_answers = len(total_answers)

        # Different treatment for openned or closed questions
        if len(list(set(total_answers))) > 2:

            report.question_type = 'open'

            # Let's store some data for the report
            report.average_chars_length = round(np.mean([len(answer) for answer in total_answers]), 2)
            report.average_tokens_length = round(np.mean([len(re.findall('\w+', answer)) for answer in total_answers]), 2)
            report.max_token_length = max([len(re.findall('\w+', answer)) for answer in total_answers])

            # First, count words for IDF later
            count_vectorizer = CountVectorizer(
                max_df=0.95,
                stop_words=self.stopwords,
                strip_accents=None,
                lowercase=True)
            counted_data = count_vectorizer.fit_transform(total_answers)

            # Now TF-IDF for each answer
            tfidf_vectorizer = TfidfTransformer(
                smooth_idf=True,
                use_idf=True)
            vectorized_data = tfidf_vectorizer.fit_transform(counted_data)

            # Extract TFIDF scores, counts, terms, and write that as CSV
            word_features = count_vectorizer.get_feature_names()
            weights = np.asarray(vectorized_data.mean(axis=0)).ravel().tolist()
            counts = counted_data.sum(axis=0).tolist()[0]
            tfidf_full_data = pd.DataFrame({'term': word_features, 'weight': weights, 'counts': counts})
            pd.DataFrame(tfidf_full_data.sort_values(by='weight', ascending=False)).to_csv(os.path.join(results_records_path, 'word_counts_scores_sorted.csv'))

            # To parse data doc per doc, uncomment below
            #for answer, tfidf_data in zip(total_answers, vectorized_data):
            #    words_indices = tfidf_data.indices
            #    tfidf_scores = tfidf_data.data

            # Add some stuff in the markdown report
            report.max_used_token = tfidf_full_data.loc[tfidf_full_data['counts'].idxmax()]['term']
            report.max_used_token_count = tfidf_full_data.loc[tfidf_full_data['counts'].idxmax()]['counts']
            report.top_20_terms = tfidf_full_data.sort_values(by='weight', ascending=False)['term'].head(20).tolist()

            # Now, let's stem the vocabulary and recount it
            stemmer = FrenchStemmer()
            stems_count = {}
            for word, count in zip(word_features, counts):
                try:
                    stems_count[stemmer.stem(word)] += count
                except KeyError:
                    stems_count[stemmer.stem(word)] = count
            # And also keep it as CSV
            stems_count = sorted(stems_count.items(), key=lambda kv: kv[1], reverse=True)
            pd.DataFrame(stems_count, columns=['term', 'count']).to_csv(os.path.join(results_records_path, 'stem_counts_sorted.csv'))
            report.top_20_stems = [word[0] for word in stems_count[:20]]

        # No TFIDF needed for closed questions
        else:
            report.question_type = 'close'
            # Get simple percentage
            counted_answers = Counter(total_answers)
            report.percentage_yes = round((counted_answers['Oui'] * 100) / report.number_of_answers, 2)
            report.percentage_no = round((counted_answers['Non'] * 100) / report.number_of_answers, 2)

        report.write_to_file(report_file=self.report_file)

    def train_word_embedding(self, documents, theme_folder, question):
        """
        Train a word embedding by using W2V (each per question and one global)
        """

        # Get data soring path to save word embedding model
        question_folder = unidecode.unidecode(question[:70].lower().replace(' ', '_').replace("'", '').replace(',', '').replace('/', ''))
        results_records_path = os.path.join('results', theme_folder, question_folder)

        # THIS STUFF HAS TO BE A PARALLEL FUNCTION

        # First, let's lower texts and remove stowords
        documents = [[word for word in re.findall('\w+', document.lower()) if word not in self.stopwords and re.search('[a-z]', word)] for document in documents]

        # Initialise and train a W2V model with Gensim's API
        model = Word2Vec(
            sentences=documents,
            size=100,
            window=5,
            min_count=10,
            workers=4,
            iter=10)
        # Then save it
        model.save(os.path.join(results_records_path, 'words_embedding.mod'))

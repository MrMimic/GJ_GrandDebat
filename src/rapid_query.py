#!/usr/bin/env python3
# coding: utf8


import time
import argparse
import configparser
from gensim.models import word2vec


parser = argparse.ArgumentParser()
parser.add_argument('-m', '--model', type=str, nargs='?', default='./', help='Path to your model')
parser.add_argument('-n', '--number', type=int, nargs='?', default='./', help='Number of top-close term you want')
parser.add_argument('-w', '--word2vec', action='store_true', help='Load a W2V model')
parser.add_argument('-q', '--query', action='store_true', help='Query the model with an input from the user')
args = parser.parse_args()


if args.word2vec is True:          # W2V
	# Load
	try:
		model = word2vec.Word2Vec.load(args.model)
		print('\nWord2Vec model [{}] loaded.\n'.format(args.model))
	except FileNotFoundError:
		print('\nNo model [{}]\n'.format(args.model))
		exit(0)
	if args.query is True:
		while True:
			try:
				word = input('Enter: ')
				top_close = model.most_similar(positive=word, topn=args.number)
				print(model[word])
				print('\n\t- ' + '\n\t- '.join([str(x) for x in top_close]))
				print()
			except KeyError:
				print('Word [{}] not in your model'.format(word))
				continue
			except KeyboardInterrupt:
				exit(0)

import pandas as pd
import numpy as np
import nltk
from nltk.corpus.reader import PlaintextCorpusReader
from sklearn.feature_extraction.text import CountVectorizer


championsLeague = pd.read_csv('championsLeague.csv',header=None)
championsLeague.columns = ['Date', 'text']
laliga = pd.read_csv('laliga.csv',header=None)
championsLeague.columns = ['Date', 'text']
premierLeague = pd.read_csv('premierLeague.csv',header=None)
championsLeague.columns = ['Date', 'text']

x = type(championsLeague['text'][0].decode(encoding = 'ascii'))
print(x)



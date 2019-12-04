import pandas as pd
import numpy as np
import nltk
from nltk.corpus.reader import PlaintextCorpusReader
from sklearn.feature_extraction.text import CountVectorizer

mycorpus = PlaintextCorpusReader(r"championsLeague.csv")

championsLeague = pd.read_csv('championsLeague.csv')
laliga = pd.read_csv('laliga.csv')
premierLeague = pd.read_csv('premierLeague.csv')


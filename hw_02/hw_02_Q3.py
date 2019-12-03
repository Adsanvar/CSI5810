import numpy as np
import nltk
import pandas as pd
from nltk.corpus.reader import PlaintextCorpusReader
from sklearn.feature_extraction.text import CountVectorizer
mycorpus = PlaintextCorpusReader(r"CSI58100TextFiles", r".*\.txt")
vec = CountVectorizer()
indx = 0
lst = []
for i in mycorpus.fileids():
    nlst = mycorpus.raw(i)
    indx = indx+1
    lst.append(nlst)
corpus = np.array(lst)

#-----------Stop Words---------
vec = CountVectorizer(stop_words="english")
vec.fit(corpus)
#Sparse matrix
X = vec.transform(corpus)
#tfidf
from sklearn.feature_extraction.text import TfidfTransformer
tfidf = TfidfTransformer()
xTfidf = tfidf.fit_transform(X)
df_tfidf = pd.DataFrame(xTfidf.toarray(), columns = vec.get_feature_names(), index = mycorpus.fileids()).T
df_tfidf = df_tfidf.round(5)
df_tfidf.to_csv('tfidfMatrix.csv')
# Cosine similarity
from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity(xTfidf,xTfidf)
print(similarity)

df = pd.DataFrame(similarity, columns = mycorpus.fileids(), index = mycorpus.fileids())
df = df.round(5)
df.to_csv('sample_Q3.csv')
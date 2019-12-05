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
bM = pd.DataFrame(X.toarray(), columns = vec.get_feature_names(), index = mycorpus.fileids()).T
print(type(corpus))
print(corpus)
print(bM)
# bM.to_csv('booleanMatrix.csv')
# # Jaccards similarity
# from sklearn.metrics import jaccard_score
# similarity = []
# for i in range(0, len(X.toarray())):
#     matrix = []
#     for k in range(0, len(X.toarray())):
#         matrix.append(jaccard_score( X.toarray()[i], X.toarray()[k], average ='weighted')) # Calculate metrics for each label, and find their average, weighted by support (the number of true instances for each label).
#         if(k == 7):
#             similarity.append(matrix)

# df = pd.DataFrame(similarity, columns = mycorpus.fileids(), index = mycorpus.fileids())
# df = df.round(5)
# print(df)
# df.to_csv('sample.csv')
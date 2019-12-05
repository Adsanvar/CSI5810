import pandas as pd
import numpy as np
import nltk
from nltk.corpus.reader import PlaintextCorpusReader
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt

championsLeague = pd.read_csv('championsLeague.csv',header=None, encoding='utf-8')
championsLeague.columns = ['Date', 'text']
laliga = pd.read_csv('laliga.csv',header=None,encoding='utf-8')
laliga.columns = ['Date', 'text']
premierLeague = pd.read_csv('premierLeague.csv',header=None,encoding='utf-8')
premierLeague.columns = ['Date', 'text']


vec = CountVectorizer(stop_words="english")
w = []
for i in championsLeague['text']:
    w.append(i)
w = ' '.join(w)
z = []
z.append(w)

from nameparser.parser import HumanName
from nltk.corpus import wordnet
person_list = []

def get_human_names(text):
    tokens = nltk.tokenize.word_tokenize(text)
    pos = nltk.pos_tag(tokens)
    sentt = nltk.ne_chunk(pos, binary = False)

    person = []
    name = ""
    for subtree in sentt.subtrees(filter=lambda t: t.label() == 'PERSON'):
        for leaf in subtree.leaves():
            person.append(leaf[0])
        if len(person) > 1: #avoid grabbing lone surnames
            for part in person:
                name += part + ' '
            if name[:-1] not in person_list:
                person_list.append(name[:-1])
            name = ''
        person = []
    #print(person_list)

#names = get_human_names(z[0])
# person_names=person_list
# for person in person_list:
#     person_split = person.split(" ")
#     for name in person_split:
#         if wordnet.synsets(name):
#             if(name in person):
#                 person_names.remove(person)
#                 break

# print(person_names)
#concat_name = pd.DataFrame(person_list, columns=['Name'])


w = []
for i in laliga['text']:
    w.append(i)
w = ' '.join(w)
z.append(w)


w = []
for i in premierLeague['text']:
    w.append(i)
w = ' '.join(w)
z.append(w)

x = vec.fit_transform(z)
y =[i for i in vec.vocabulary_.keys()]
y.reverse()
bM = pd.DataFrame(x.toarray(), columns=y, index=['Champions League','La Liga', 'Premier League']).T
#bM.to_csv('count_matrix.csv')
# print(w)

plt.scatter(bM['Champions League'], bM.T.columns)
plt.show()

human_names = []

# for i in z:
#     person_list = []
#     get_human_names(i)
#     human_names.append(person_list)

# df = pd.DataFrame(human_names, index=['Champions League','La Liga', 'Premier League']).T
#df.to_csv('resulting_names.csv')
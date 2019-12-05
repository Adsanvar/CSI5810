import pandas as pd
import numpy as np
import nltk
from nltk.corpus.reader import PlaintextCorpusReader
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
import datetime
import plotly.express as px

trump = pd.read_csv('realdonaldtrump.csv',header=None, encoding='utf-8')
trump.columns = ['Date', 'text']

x = []
for i in np.array(trump['Date']):
    info = i.split()
    x.append(info)
df = pd.DataFrame(x, columns=['Date', 'Time'])
counts = df['Date'].value_counts().sort_index()

fig = plt.figure()
ax = fig.add_subplot()
ax.yaxis_date()
plt.show()


# fig = px.line(df, x='Date', y='Time')
# fig.show()

# plt.title('Tweets Per Day')
# plt.bar(counts.index, counts.values, label="mean: " +str(np.mean(counts.values)))
# plt.xticks(counts.index, rotation='vertical')
# plt.subplots_adjust(bottom=0.25)
# plt.legend()
# plt.show()
# #plt.savefig('tweetsperday.png', format='png')


# vec = CountVectorizer(stop_words="english")
# w = []
# for i in championsLeague['text']:
#     w.append(i)
# w = ' '.join(w)
# z = []
# z.append(w)

# x = vec.fit_transform(z)
# y =[i for i in vec.vocabulary_.keys()]
# y.reverse()
# bM = pd.DataFrame(x.toarray(), columns=y, index=['Champions League','La Liga', 'Premier League']).T
# #bM.to_csv('count_matrix.csv')
# # print(w)


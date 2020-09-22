import pandas as pd
import numpy as np
import nltk
from nltk.corpus.reader import PlaintextCorpusReader
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
import datetime
from textblob import TextBlob
from urlextract import URLExtract

tlc = pd.read_csv('tlc.csv',header=None, encoding='utf-8')
#tlc.dropna(axis=1, how='any', inplace=True)
tlc.columns = ['Date', 'text']
tlc2 = pd.read_csv('tlc_nht.csv',header=None, encoding='utf-8')
#tlc.dropna(axis=1, how='any', inplace=True)
tlc2.columns = ['Date', 'text']
tlc3 = pd.read_csv('tlc_1.csv',header=None, encoding='utf-8')
#tlc.dropna(axis=1, how='any', inplace=True)
tlc3.columns = ['Date', 'text']
tlc4 = pd.read_csv('tlc_1nht.csv',header=None, encoding='utf-8')
#tlc.dropna(axis=1, how='any', inplace=True)
tlc4.columns = ['Date', 'text']

tlc_total = pd.concat([tlc, tlc2, tlc3, tlc4], ignore_index=True)
tlc_total.to_csv("total_tlc.csv")
x = []
for i in np.array(tlc_total['Date']):
    info = i.split()
    x.append(info)
df = pd.DataFrame(x, columns=['Date', 'Time'])
print(df)
counts = df['Date'].value_counts().sort_index()


hour = []
for i in df['Time']:
    h, m, s= map(int,i.split(':'))
    hour.append(h)
    
ds = pd.DataFrame(hour, columns=['hours'])
freq = ds['hours'].value_counts().sort_index()


morning = []
evening = []
afternoon = []
night = []
for i in range(len(freq)):   
    if freq.index[i] < 12 and freq.index[i] >=6:
        morning.append(freq.values[i])
    if freq.index[i] < 17 and freq.index[i] >=12:
        afternoon.append(freq.values[i])
    if freq.index[i] < 20 and freq.index[i] >=17:
        evening.append(freq.values[i])
    if freq.index[i] >= 20 or freq.index[i] < 6 :
        night.append(freq.values[i])

timeofday = []
timeofday.append(sum(morning))
timeofday.append(sum(afternoon))  
timeofday.append(sum(evening))  
timeofday.append(sum(night))     

# plt.title('Tweets')
# plt.bar(['Morning', 'Afternoon', 'Evening', 'Night'], timeofday)
# plt.xticks(['Morning', 'Afternoon', 'Evening', 'Night'], rotation='vertical')
# # plt.ylabel('QTY')
# # plt.xlabel('Hour')
# plt.subplots_adjust(bottom=0.25)
# #plt.legend()
# plt.show()
# #plt.savefig('tlc_tweets.png', format='png')

# plt.title('Tweets Per hour')
# plt.bar(freq.index, freq.values,label="mean: " +str(np.round(np.mean(freq.values), decimals=0)))
# plt.xticks(freq.index)
# plt.ylabel('QTY')
# plt.xlabel('Hour')
# plt.subplots_adjust(bottom=0.25)
# plt.legend()
# plt.show()
# #plt.savefig('tlc_tweetsperhour.png', format='png')

# plt.title('Tweets Per Day')
# plt.bar(counts.index, counts.values, label="mean: " +str(np.mean(counts.values)))
# plt.xticks(counts.index, rotation='vertical')
# plt.subplots_adjust(bottom=0.25)
# plt.legend()
# plt.show()
# #plt.savefig('tlc_tweetsperday.png', format='png')

extractor = URLExtract()
vec = CountVectorizer(stop_words="english")
w = []
for i in tlc_total['text']:
    if extractor.has_urls(i):
        url = extractor.find_urls(i)
        #print('\n^^^ {} Does Have URL'.format(url))
        for k in url:
            #print(k)
            i = i.replace(k, '')
            w.append(i)
    else:
        w.append(i)

for i in range(len(w)):
    if '@' in w[i]:
        w[i] = w[i].replace('@','')
    if '#' in w[i]:
        w[i] = w[i].replace('#','')
    if '&amp' in w[i]:
        w[i] = w[i].replace('&amp', '')
    if '"' in w[i]:
        w[i] = w[i].replace('"', '')

#used for Sentiment
filterDF = pd.DataFrame(df['Date'], columns=['Date'])
filterDF['Tweet'] = w

#combines into one string
w = ' '.join(w)

z = []
z.append(w)
#print(z)
x = vec.fit_transform(z)
y =[i for i in vec.vocabulary_.keys()]
y.reverse()
bM = pd.DataFrame(x.toarray(),index=['count'] ,columns=y).T

print(bM)
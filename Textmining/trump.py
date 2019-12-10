import pandas as pd
import numpy as np
import nltk
from nltk.corpus.reader import PlaintextCorpusReader
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
import datetime
from textblob import TextBlob
from urlextract import URLExtract

trump = pd.read_csv('realdonaldtrump.csv',header=None, encoding='utf-8')
trump.dropna(axis=1, how='any', inplace=True)
trump.columns = ['Date', 'text']
#trump.to_csv('trumpdata.csv')

extractor = URLExtract()

x = []
for i in np.array(trump['Date']):
    info = i.split()
    x.append(info)
df = pd.DataFrame(x, columns=['Date', 'Time'])
counts = df['Date'].value_counts().sort_index()

s = []
for i in df['Time']:
    h, m = map(int,i.split(':'))
    s.append(h)
ds = pd.DataFrame(s, columns=['hours'])
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
# #plt.savefig('tweets.png', format='png')


# plt.title('Tweets Per hour')
# plt.bar(freq.index, freq.values,label="mean: " +str(np.round(np.mean(freq.values), decimals=0)))
# plt.xticks(freq.index)
# plt.ylabel('QTY')
# plt.xlabel('Hour')
# plt.subplots_adjust(bottom=0.25)
# plt.legend()
# plt.show()
# #plt.savefig('tweetsperhour.png', format='png')


# plt.title('Tweets Per Day')
# plt.bar(counts.index, counts.values, label="mean: " +str(np.mean(counts.values)))
# plt.xticks(counts.index, rotation='vertical')
# plt.subplots_adjust(bottom=0.25)
# plt.legend()
# plt.show()
# #plt.savefig('tweetsperday.png', format='png')

# selected = []
# for i in range(len(df['Date'])):
#     if df['Date'][i] == '12/2/2019':
#         selected.append(trump['text'][i])
        

vec = CountVectorizer(stop_words="english")
w = []
for i in trump['text']:
    if extractor.has_urls(i):
        url = extractor.find_urls(i)
        for k in url:
            i = i.replace(k, '')
            w.append(i)
    else:
        w.append(i)

w.remove(' https://t.co/G6lGfyxSUs')
#remove '@' and '#'
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

#selected = ' '.join(selected)
# z = []
# z.append(selected)

z = []
z.append(w)
#print(z)
x = vec.fit_transform(z)
y =[i for i in vec.vocabulary_.keys()]
y.reverse()
bM = pd.DataFrame(x.toarray(),index=['count'] ,columns=y).T
#bM.to_csv('count_matrix.csv')

# word = []
# qt = []
# words = []
# qty = []
# for i in range(len(bM['count'])):
#     sym = bM.index[i]
#     if sym == 'did' or sym == 'dnil5o1wod' or sym == 'atgsntphk6'  or sym == 'utxqn6ge4q' or sym == 'https' or  sym == 'w1wsjinu3a' or sym == 'y0em0ks1cq' or sym == 'lujdrxg3bv' or sym == 'eole1xlqze' or sym == 'zlfv4mokom' or sym == 'xrjsusm9wq' or sym == 'jp7wb8b4hj' or sym == 'w51pdktm2g' or sym == 'lvvcujz5cw' or sym =='wcmmi7q7q2' or sym == 'gekugvw7sj' or sym == '6xh3iq7bsk' or sym == 'thjhcx6lqv' or sym == 'scgeo0pu5o' or sym == 'atgsntphk6' or sym == '4luj6dpgl2' or sym == '7dff3j8rev' or sym == 'dnil5o1wod' or sym == '21' or sym == '2018' or sym == 'jxjxnw8gll' or sym == 'htkwe89s8a' or sym == 'fpoecstlmq' or sym == 'ae0wyng7k1' or sym == '2016' or sym == '100' or sym =='9ijcplhrxk': 
#         continue

#     words.append(bM.index[i])
#     qty.append(bM['count'][i])

#     if bM['count'][i] > 1:
#         word.append(bM.index[i])
#         qt.append(bM['count'][i])

       
# df2 = pd.DataFrame(words, columns=['word'])
# df2['count'] = qty
#df2.to_csv('count_matrix.csv')

# plt.bar(word, qt )
# plt.xticks(word, rotation='vertical')
# plt.yticks(qt, rotation='vertical')
# plt.ylabel('12/02/2019 Common Words')
# plt.subplots_adjust(bottom=0.25)
# #plt.legend()
# plt.show()
# #plt.savefig('common_in_day.png', format='png')

######Common in all days above 1

# words = []
# qty = []
# for i in range(len(bM['count'])):
#     if bM['count'][i] > 2:
#         if not bM.index[i].isdigit():
#             #print(bM.index[i], bM['count'][i])
#             words.append(bM.index[i])
#             qty.append(bM['count'][i])

       
# df2 = pd.DataFrame(words, columns=['word'])
# df2['count'] = qty
# #df2.to_csv('count_matrix.csv')

# plt.bar(words, qty )
# plt.xticks(words, rotation='vertical', fontsize=10)
# plt.yticks(qty, rotation='vertical', fontsize =6)
# plt.ylabel('DJT Common Words')
# plt.subplots_adjust(bottom=0.25)
# #plt.legend()
# plt.show()

####

### special case  for the day
# special = []
# for i in range(len(df['Date'])):
#     if df['Date'][i] == '12/2/2019':
#         special.append(df['Time'][i])

# fd = pd.DataFrame(special, columns=['Time'])

# s = []
# for i in fd['Time']:
#     h, m = map(int,i.split(':'))
#     s.append(h)
# ds = pd.DataFrame(s, columns=['hours'])

# freq = ds['hours'].value_counts().sort_index()

# plt.title('Tweets Per hour on 12/02/2019')
# #plt.bar(freq.index, freq.values,label="mean: " +str(np.round(np.mean(freq.values), decimals=0)))
# plt.plot(freq.index, freq.values, label="mean: " + str(np.round(np.mean(freq.values), decimals=0)))
# axis = [i for i in range(25)]
# plt.xticks(axis)
# plt.ylabel('QTY')
# plt.xlabel('Hour')
# plt.subplots_adjust(bottom=0.25)
# plt.legend()
# #plt.show()
# plt.savefig('tweetsperhour12_02_2019.png', format='png')

# person_list = []

# def get_human_names(text):
#     tokens = nltk.tokenize.word_tokenize(text)
#     pos = nltk.pos_tag(tokens)
#     sentt = nltk.ne_chunk(pos, binary = False)

#     person = []
#     name = ""
#     for subtree in sentt.subtrees(filter=lambda t: t.label() == 'PERSON'):
#         print(subtree.leaves())
#         for leaf in subtree.leaves():
#             person.append(leaf[0])
#         if len(person) > 1: #avoid grabbing lone surnames
#             for part in person:
#                 name += part + ' '
#             if name[:-1] not in person_list:
#                 person_list.append(name[:-1])
#             name = ''
#         person = []

# get_human_names(z[0])

# print(person_list)

###TExtblob for sentiment
filterDF['polarity'] = filterDF.apply(lambda x: TextBlob(x['Tweet']).sentiment.polarity, axis=1)
filterDF['subjectivity'] = filterDF.apply(lambda x: TextBlob(x['Tweet']).sentiment.subjectivity, axis=1)

# plt.title("Sentiment of Trump's Tweets")
# plt.plot(filterDF['polarity'], label='Polarity Mean: ' +str(np.round(np.mean(filterDF['polarity']), 3)))
# plt.plot(filterDF['subjectivity'], label='Sujectivity Mean: ' +str(np.round(np.mean(filterDF['subjectivity']), 3)))
# plt.legend()
# plt.show()

###Sentinment on 12/02/2019
# polar = []
# subj = []
# time = []
# for i in range(len(df['Date'])):
#     if filterDF['Date'][i] == '12/2/2019':
#         polar.append(filterDF['polarity'][i])
#         subj.append(filterDF['subjectivity'][i])
#         time.append(df['Time'][i])

# # time.reverse()
# # polar.reverse()
# # time.reverse()
# plt.title("Sentiment of Trump's Tweets on 12/02/2019")
# plt.plot(time, polar, label='Polarity Mean: ' +str(np.round(np.mean(polar), 3)))
# plt.plot(time, subj, label='Sujectivity Mean: ' +str(np.round(np.mean(subj), 3)))
# plt.xticks(rotation = 'vertical')
# plt.legend()
# plt.show()




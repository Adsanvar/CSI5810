import tweepy
import csv
import pandas as pd
key = ''
sec = ''
at = ''
atc = ''

auth = tweepy.OAuthHandler(key, sec)
auth.set_access_token(at, atc)
api = tweepy.API(auth,wait_on_rate_limit=True)

#####United Airlines
# Open/Create a file to append data
csvFile = open('championsLeague.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.user_timeline,id='ChampionsLeague',
                           lang="en").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

# for tweet in tweepy.Cursor(api.search,q="@LaLiga",
#                            lang="en",
#                            since="2019-01-01").items():
#     print (tweet.created_at, tweet.text)
#     csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
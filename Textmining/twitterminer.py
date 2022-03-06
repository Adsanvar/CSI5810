import tweepy
import csv
import pandas as pd


auth = tweepy.OAuthHandler(key, sec)
auth.set_access_token(at, atc)
api = tweepy.API(auth,wait_on_rate_limit=True)

with open('tlc_nht.csv', 'a', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    for tweet in tweepy.Cursor(api.search, q='tlchq',
                            lang="en", since="2019-01-01", tweet_mode='extended').items():
        print (tweet.created_at, tweet.full_text)
        writer.writerow([tweet.created_at, tweet.full_text])



# with open('realdonaldtrump2.csv', 'a', encoding='utf-8', newline='') as file:
#     writer = csv.writer(file)
#     for tweet in tweepy.Cursor(api.user_timeline,id='realdonaldtrump',
#                             lang="en", include_rts = False):
#         print (tweet.created_at, tweet.text)
#         writer.writerow([tweet.created_at, tweet.text])


# # Open/Create a file to append data
# csvFile = open('championsLeague.csv', 'a')
# #Use csv Writer
# csvWriter = csv.writer(csvFile)
# for tweet in tweepy.Cursor(api.user_timeline,id='ChampionsLeague',
#                            lang="en").items():
#     print (tweet.created_at, tweet.text)
#     csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

# for tweet in tweepy.Cursor(api.search,q="@LaLiga",
#                            lang="en",
#                            since="2019-01-01").items():
#     print (tweet.created_at, tweet.text)
#     csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])




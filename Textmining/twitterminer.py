import tweepy
import csv
import pandas as pd
key = 'OdrgZP76yhFmUE13v4DZlr5SG'
sec = '9dhATYiSQQeKuODYZSXlKzKiOkb2n1XhnqHlnbqpN0sm6s2CBB'
at = '935321954638184449-EClvjsAyfxZRof3LbxvYQHwvBBX3gAT'
atc = 'AsmdQwSVOWuyINLu2HDRs8QuyiiYU9FBsL9AHtUrAXWU9'

auth = tweepy.OAuthHandler(key, sec)
auth.set_access_token(at, atc)
api = tweepy.API(auth,wait_on_rate_limit=True)


with open('realdonaldtrump2.csv', 'a', encoding='utf-8', newline='') as csvFile:
    csvWriter = csv.writer(csvFile)
    for tweet in tweepy.Cursor(api.user_timeline,id='realdonaldtrump',
                            lang="en", include_rts = False).items(3000):
        print (tweet.created_at, tweet.text)
        csvWriter.writerow([tweet.created_at, tweet.text])


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




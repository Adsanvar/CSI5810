import tweepy
import csv
import pandas as pd
key = 'OdrgZP76yhFmUE13v4DZlr5SG'
sec = '9dhATYiSQQeKuODYZSXlKzKiOkb2n1XhnqHlnbqpN0sm6s2CBB'
at = '935321954638184449-EClvjsAyfxZRof3LbxvYQHwvBBX3gAT'
atc = 'AsmdQwSVOWuyINLu2HDRs8QuyiiYU9FBsL9AHtUrAXWU9'

auth = tweepy.OAuthHandler(key, sec)
auth.set_access_token(at, atc)
api = tweepy.API(auth,proxy='https://ep.threatpulse.net:80',wait_on_rate_limit=True)

timeLine = api.home_timeline()

for tweet in timeLine:
    print(tweet)

# #####United Airlines
# # Open/Create a file to append data
# csvFile = open('ua.csv', 'a')
# #Use csv Writer
# csvWriter = csv.writer(csvFile)

# for tweet in tweepy.Cursor(api.search,q="#unitedAIRLINES",count=100,
#                            lang="en",
#                            since="2017-04-03").items():
#     print (tweet.created_at, tweet.text)
#     csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
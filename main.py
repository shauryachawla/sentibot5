import sys
import tweepy
from pprint import pprint
import csv
import re
from keys import consumerKey, consumerSecret, accessToken, accessTokenSecret
# from textblob import TextBlob
# import matplotlib.pyplot as plt

reload(sys)
sys.setdefaultencoding('utf8')

# authenticating
# consumerKey = 'VFxtQvRfgst3f9aPyFTy7wR8A'
# consumerSecret = '44pQWeZr6Ifmj7OaaVfWSACesaxKnJNouwqom9mMJ3UhqKaxNA'
# accessToken = '1093171008154923009-QsKJwczSgeT3wb1PGc0nI9D1TGaHiN'
# accessTokenSecret = 'ysRDaRdYXkaIxcci2NJiRfHvCyO6vMMLnWF0aYLtXVOWb'
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

# input for term to be searched and how many tweets to search
# searchTerm = input("Enter Keyword/Tag to search about: ")
# NoOfTerms = int(input("Enter how many tweets to search: "))

usrnm = "sentibot5"
psw = "oreganooregano"
# trends = []
# jdata = api.trends_place(23424848)
# # pprint(jdata[0]["trends"])
# trend_arr = jdata[0]["trends"][:5]
# # pprint(trend_arr)


# for trend in trend_arr:
#     if(trend['name'][0] == "#"):
#         try:
#             cleaned_name = trend['name'][1:]
#             trends.append(cleaned_name)
#             i += 1
#         except:
#             continue
#     else:
#         trends.append(trend['name'])
#         i += 1

# updating a status
api.update_status('Updating again 2')

# to follow every user back
for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
    print follower.screen_name
# for trend in trends:
#     print trend.encode('utf-8')

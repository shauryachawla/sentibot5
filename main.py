from time import gmtime, strftime, sleep
import sys
import tweepy
from textblob import TextBlob
import re
# from keys import consumerKey, consumerSecret, accessToken, accessTokenSecret

# from textblob import TextBlob
# import matplotlib.pyplot as plt

# reload(sys)
# sys.setdefaultencoding('utf8')


def cleanTweet(tweet):
    # Remove Links, Special Characters etc from tweet
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ / \ / \S +)", " ", tweet).split())


# authenticating
consumerKey = 'VFxtQvRfgst3f9aPyFTy7wR8A'
consumerSecret = '44pQWeZr6Ifmj7OaaVfWSACesaxKnJNouwqom9mMJ3UhqKaxNA'
accessToken = '1093171008154923009-QsKJwczSgeT3wb1PGc0nI9D1TGaHiN'
accessTokenSecret = 'ysRDaRdYXkaIxcci2NJiRfHvCyO6vMMLnWF0aYLtXVOWb'
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)


def doTheThing():
    trends = []
    jdata = api.trends_place(23424848)
    # # pprint(jdata[0]["trends"])
    trends_arr = jdata[0]["trends"][:9]
    # # pprint(trend_arr)

    for trend in trends_arr:
        if(trend['name'][0] == "#"):
            try:
                cleaned_name = trend['name'][1:]
                trends.append(cleaned_name)
                # i += 1
            except:
                continue
        else:
            trends.append(trend['name'])
            # i += 1

    # print(trends)

    NoOfTerms = 25
    pos = []
    i = 0
    for trend in trends:
        polarity = 0
        tweets = []
        tweetText = []
        tweets = tweepy.Cursor(api.search, q=trend, lang="en").items(NoOfTerms)
        for tweet in tweets:
            tweetText.append(cleanTweet(tweet.text).encode('utf-8'))
            analysis = TextBlob(tweet.text)
            polarity += analysis.sentiment.polarity
        pos.append(polarity)
        # print(tweetText)

    print(trends)
    print(pos)
    positive_trend_polarity = max(pos)
    print(positive_trend_polarity)
    trend_location = -1
    j = 0
    for i in pos:
        if(i == positive_trend_polarity):
            trend_location = j
        else:
            j += 1
    print("The most positive tweets are associated with " +
          trends[trend_location] + " hashtag")
    try:
        api.update_status("The most positive tweets are associated with " +
                          trends[trend_location] + " hashtag. " + strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    except:
        print("duplicate status")

# to follow every user back


def followBack():
    for follower in tweepy.Cursor(api.followers).items():
        follower.follow()
        print(follower.screen_name)


while True:
    followBack()
    doTheThing()
    print("i'm working")
    sleep(3600)

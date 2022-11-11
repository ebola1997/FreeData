import tweepy
import csv
import datetime
from tweepy import OAuthHandler
from datetime import date

consumer_key = "EY8IRAZnn7Tlejv9ppxmGeJwH"
consumer_secret = "OP0neJHeUl3wQsUqrBE3xZR3JY71xlMILih4fV2aqnMRCca5HT"
access_token = "1635682130-tUaBntA15MIrC3VkrUjIm96uJXkoDussNAFmmip"
access_secret = "gnLkQkZG9M1HMfz2M2DQwC9wupeSxyAYnc3AcqWCeiLzh"
tweetsPerQry = 100
maxTweets = 1000
search_key = "pemilu"
maxId = -1
tweetCount = 0
today = date.today()

authentication = tweepy.OAuthHandler(consumer_key, consumer_secret)
authentication.set_access_token(access_token, access_secret)
api = tweepy.API(authentication, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

while tweetCount < maxTweets:
    if maxId <= 0 :
        newTweets = api.search(q=search_key, count=tweetsPerQry, result_type="recent", tweet_mode = "extended")
    
    newTweets = api.search(q=search_key, count=tweetsPerQry, result_type="recent", tweet_mode = "extended", max_id=str(maxId-1))

    if not newTweets :
        print("Tweet Habis")
        break

    for tweet in newTweets:
        dictTweet = {
            "username" : tweet.user.name,
            "tweet" : tweet.full_text.encode('utf-8')
        }
        print("Username {username} : {tweet}".format(username=dictTweet["username"], tweet=dictTweet["tweet"]))
        with open("pemilu_"+today.strftime('%m_%d_%Y')+".csv", 'a+', newline='') as csv_file:
            fieldNames = ["username", "tweet"]
            writer = csv.DictWriter(csv_file, fieldnames = fieldNames, delimiter=",",)
            writer.writerow(dictTweet)

    tweetCount += len(newTweets)	
    maxId = newTweets[-1].id

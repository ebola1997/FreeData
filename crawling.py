import tweepy
import csv

consumer_key = "k0iL0GZoHnGSfXoeHoNjAz20T"
consumer_secret = "hzh5mBGHdDd9Ci1rNW5WIFr4zdtHt5CiL4hDeXNmscfz3904cp"
access_token = "821731748-kAk1xTZLTAc1upSBptUYMW7qmiNquq8Rw6n9KOa1"
access_secret = "mQ7oEZpzYw0PTb2kIArb3dWEDbFGwgmEKTFA6nNSGO2YW"
tweetsPerQry = 100
maxTweets = 1000
search_key = "pemilu"
maxId = -1
tweetCount = 0

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
        with open(today.strftime('%m_%d_%Y')+".csv", 'a+', newline='') as csv_file:
            fieldNames = ["username", "tweet"]
            writer = csv.DictWriter(csv_file, fieldnames = fieldNames, delimiter=";",)
            writer.writerow(dictTweet)

    tweetCount += len(newTweets)	
    maxId = newTweets[-1].id

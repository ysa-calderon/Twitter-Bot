import tweepy

# keys from twitter API
consumer_key = ''
consumer_secret = ''

# access tokens
key = ''
secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

# update status live
api = tweepy.API(auth)
api.update_status('I am now active!')

# return all mentions in bot timeline
tweets = api.mentions_timeline()
# print(tweets[0].text) # retrieves text of tweet mentioned in

# cycle through all mentioned tweets
for tweet in tweets:
    # grab id's and texts and print
        print(str(tweet.id) + ' - ' + tweet.text)
    # checks if specific hashtag (no matter the upper or lower case) and prints id and text
""" if '#anafebot' in tweet.text.lower():
        print(str(tweet.id) + ' - ' + tweet.text) """
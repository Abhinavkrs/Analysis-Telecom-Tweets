import tweepy

consumer_key = raw_input('Enter your consumer key :')
consumer_secret = raw_input('Enter your consumer secret :')

access_token = raw_input('Enter your access token :')
access_token_secret = raw_input('Enter your access token secret :')
def authentication():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)

api = authentication()

def retrive_tweets(telecom):
     public_tweets = api.search(str(telecom), count = 200)
     return public_tweets,telecom
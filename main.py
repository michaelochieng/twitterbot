#pip install tweepy
from itertools import count
import tweepy

API_KEY = 'JVVoxLtWmqoCFO3KBjlCwwVWR'
API_KEY_SECRET = 'rccJgW6rI2Ml68ZZYRr1Y4oBBCfSVoBJ0k4vhL7EoYbofVpwuS'
ACCESS_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAHrOdgEAAAAAIBkFR0XQ5ZFzi8rr8odJMoQP1eo%3DZeJE3Ivw3Qk7r5tqAFP6w8vJcljTbriX6Gor9wz0p8uas2fwUx'
ACCESS_TOKEN_SECRET = ''

auth = tweepy.OAuthHander(API_KEY, API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

while True:
    for tweet in api.search_tweets("rongai OR sakaja lang:en -is:retweet -is:reply -is:quote -is:nullcast"):
        print(f"Tweet id : {tweet.id}")
        print(tweet.text)
        print(tweet.author.screen_name)
        print("===================================")
        api.retweet(tweet.id)
        api.create_favourite(tweet.id)
        count +=1
        print(f"Total retweet so far {count}")
import tweepy
import time

# Twitter App Credentials
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# Authorize App
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Search Information
search = "Brian is Awesome"
numberOfTweets = 1
reply = "lol thanks!"

# Loop Through Tweets
for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
	   # Retweet the tweet
        tweet.retweet()

        # Reply to Tweet
        tweetId = tweet.user.id
        username = tweet.user.screen_name
        api.update_status("@" + username + " " + reply, in_reply_to_status_id = tweetId)

        print('Retweeted and Replied to the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break


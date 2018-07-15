import tweepy

# Twitter App Credentials
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# Authorize App
print('Loading twitter...')
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Search Information
search = input('What keywords would you like to search?')
reply = input('What would you like to reply?')

# Loop Through Tweets
for tweet in tweepy.Cursor(api.search, search).items(1):
    try:
	   # Retweet the tweet
        tweet.retweet()

        # Reply to Tweet
        tweetId = tweet.user.id
        username = tweet.user.screen_name
        api.update_status("@" + username + " " + reply, in_reply_to_status_id = tweetId)

        print('Retweeted and Replied to the tweet from ' + username)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        print('No tweets found matching your keywords')
        break


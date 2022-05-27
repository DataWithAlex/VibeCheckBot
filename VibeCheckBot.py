## THIS CODE WORKS TO RESPOND TO TWEET 

import tweepy
import json
import requests
import logging
import time
import VibeModel


# This creates a tweepy object which accesses the Twitter V2 API. Authorization is done by passing the tokens & keys.
client = tweepy.Client(consumer_key="YUwWeeXzpnQaYQYYXbISj7SRx",
                       consumer_secret="8mGpxCb2SSJSELk3OrUWO2oOh78JqnhGJ1rVIW20QFEW5m0DaQ",
                       access_token="1519770072142827525-ocVARinf1ccoz5GFMTfrUgqMGxY422",
                       access_token_secret="vrZQimplvz6SCOMDMQcVmHQ6nTY3dm4pH28RsA0JdcyWS",
                       bearer_token='AAAAAAAAAAAAAAAAAAAAAF2JcgEAAAAAapxT45Goa6gNW8ZhwE2Mi2Bztik%3DcdRisSszsBs7zCnTBP90JwPIoxcN4pRymLTcnRQE5NS5Hbh8SJ')


# This initializes the user @VibeCheckBot
user = client.get_user(username='VibeCheckBot')
user_id = user.data.id


# This creates a trained Bayes Classifier Model that is able to categorize text (e.g., tweets) into two binary choices:
# (1) Pass the vibe check or (2) Don't Pass the vibe check.
vibe = VibeModel.create_vibe_model()

# application.py calls this function every 60s to check if someone mentioned @VibeCheckBot. 
# If yes, it will respond to the target user's tweet with a vibe check.
def respondToTweet():
    
    # This obtains user's most recent mentions
    mentions = client.get_users_mentions(user_id)
    # This places all mentions in a dictionary
    tweets = mentions.data
    
    # This for-loop iterates through all mentioned tweets, and reply's to each of them.
    for tweet in reversed(tweets):
        
        # This sets the id for the current tweet.
        new_id = tweet.id

        # if this phrase is in tweet, respond with a vibe check.
        if 'vibe check:' in tweet.text:

            # This prints out tweet in terminal to view how it works.
            print(tweet.text)
            # This prints the vibe of the tweet.
            print(VibeModel.get_vibe(tweet.text, vibe=vibe))
            
            try:

                x = VibeModel.get_vibe(tweet.text, vibe=vibe)
                client.create_tweet(in_reply_to_tweet_id = new_id, text = x)

            except:
                print("failed")
                #logger.info("Already replied to {}".format(mention.id))


def main():
    respondToTweet()


# __name__
if __name__=="__main__":
    main()
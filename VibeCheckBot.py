## THIS CODE WORKS TO RESPOND TO TWEET 

import tweepy
import json
import requests
import logging
import time
import VibeModel





open(r'C:\Users\alexs\DataWithAlex_Github\Twitter\VibeCheckBot\tweet_ID.txt')




client = tweepy.Client(consumer_key="YUwWeeXzpnQaYQYYXbISj7SRx",
                       consumer_secret="8mGpxCb2SSJSELk3OrUWO2oOh78JqnhGJ1rVIW20QFEW5m0DaQ",
                       access_token="1519770072142827525-ocVARinf1ccoz5GFMTfrUgqMGxY422",
                       access_token_secret="vrZQimplvz6SCOMDMQcVmHQ6nTY3dm4pH28RsA0JdcyWS",
                       bearer_token='AAAAAAAAAAAAAAAAAAAAAF2JcgEAAAAAapxT45Goa6gNW8ZhwE2Mi2Bztik%3DcdRisSszsBs7zCnTBP90JwPIoxcN4pRymLTcnRQE5NS5Hbh8SJ')


vibe = VibeModel.create_vibe_model()


def respondToTweet():
    
    alex = client.get_user(username='VibeCheckBot')
    alex_id = alex.data.id

    #client.get_users_followers(alex_id)
    mentions = client.get_users_mentions(alex_id)
    tweets = mentions.data
    
    
    for tweet in reversed(tweets):
        
        new_id = tweet.id
        #user_id = tweet.

        #  user = client.get_user(author_id=user_id)
        # screen_name = user.data.username

        if 'vibe check' in tweet.text:
            # logger.info("Responding back with QOD to -{}".format(mention.id))
            print(tweet.text)
            print(VibeModel.get_vibe(tweet.text, vibe=vibe))
            
            try:
                #tweet = get_quote()

                # media = api.media_upload("created_image.png")
                #logger.info("liking and replying to tweet")

                #reply to tweet
                x = VibeModel.get_vibe(tweet.text, vibe=vibe)
                client.create_tweet(in_reply_to_tweet_id = new_id, text = x)
                #client.create_tweet(quote_tweet_id = new_id, text = x)

                # api.create_favorite(mention.id)
                #api.update_status('@' + mention.user.screen_name + " Here's your Quote", mention.id,
                                 # media_ids=[media.media_id])
            except:
                print("failed")
                #logger.info("Already replied to {}".format(mention.id))


def main():
    respondToTweet()

    

# __name__
if __name__=="__main__":
    main()
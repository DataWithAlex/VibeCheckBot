## THIS CODE WORKS TO RESPOND TO TWEET 

from doctest import DocFileTest
import tweepy
import json
import requests
import logging
import time
import VibeModel
import tweepy
import numpy as np 
import pandas
import pygsheets
import pandas as pd
import pygsheets



# This creates a tweepy object which accesses the Twitter V2 API. Authorization is done by passing the tokens & keys.
client = tweepy.Client(consumer_key="YUwWeeXzpnQaYQYYXbISj7SRx",
                       consumer_secret="8mGpxCb2SSJSELk3OrUWO2oOh78JqnhGJ1rVIW20QFEW5m0DaQ",
                       access_token="1519770072142827525-ocVARinf1ccoz5GFMTfrUgqMGxY422",
                       access_token_secret="vrZQimplvz6SCOMDMQcVmHQ6nTY3dm4pH28RsA0JdcyWS",
                       bearer_token='AAAAAAAAAAAAAAAAAAAAAF2JcgEAAAAAapxT45Goa6gNW8ZhwE2Mi2Bztik%3DcdRisSszsBs7zCnTBP90JwPIoxcN4pRymLTcnRQE5NS5Hbh8SJ')


# This initializes the user @VibeCheckBot

user = client.get_user(username='VibeCheckBot')
user_id = user.data.id
# df = pd.DataFrame(columns=[['tweets', 'tweet_id', 'author_id', 'ref_tweet', 'responded']])
# gc = pygsheets.authorize(service_file='/Users/alexs/DataWithAlex_Github/VibeCheckBot_Final/vibecheckbot-351521-6255c4712ef6.json')
# sh = gc.open('VibeCheckBot')
# select the first sheet 
# # wks = sh[0]

# MASTER_DF = wks.get_as_df()
#update the first sheet with df, starting at cell B2. 




# This creates a trained Bayes Classifier Model that is able to categorize text (e.g., tweets) into two binary choices:
# (1) Pass the vibe check or (2) Don't Pass the vibe check.
vibe = VibeModel.create_vibe_model()

# application.py calls this function every 60s to check if someone mentioned @VibeCheckBot. 
# If yes, it will respond to the target user's tweet with a vibe check.
def respondToTweet(df):
    
    # This obtains user's most recent mentions
    mentions = client.get_users_mentions(id=user_id, expansions=['referenced_tweets.id', 'author_id'], max_results=100)
    print("we just got a list of all mentions for user @VibeCheckBot")
    #mentions = client.get_users_mentions(user_id)

    # This places all mentions in a dictionary
    tweets = mentions.data
    
    # This for-loop iterates through all mentioned tweets, and reply's to each of them.
    for tweet in reversed(tweets):

        print('Iterating through tweet: ' + tweet.text)

        # This sets the id for the current tweet.
        new_id = tweet.id
        first_row = df.loc[df['tweets'] == tweet.text]
        print(first_row)

        # print ('created dataframe DF with Gsheets: ' + first_row.tail(1))
        # first_row = df_test.iloc[0].tolist()
        # first_row[1]

        # if this phrase is in tweet, respond with a vibe check.
        if 'vibe check' in tweet.text and (first_row['responded']=='no').any():

            # This prints out tweet in terminal to view how it works.
            print('tweet: ' + tweet.text + ' - has not been responded to. Lets get the vibes! :)')
            #print(tweet.text)
            
            # This prints the vibe of the tweet.
            print(VibeModel.get_vibe(tweet.text, vibe=vibe))
            
            try:

                x = VibeModel.get_vibe(tweet.text, vibe=vibe)
                
                client.create_tweet(in_reply_to_tweet_id = new_id, text = x)
                print("Posted Tweet" + x)
                
                df.loc[(df.tweets == tweet.text),'responded']='yes'
                print("tweet marked as responded")


            except:
                print("failed")
                #logger.info("Already replied to {}".format(mention.id))
                
    return df


def test():
    mentions = client.get_users_mentions(id=user_id, expansions=['referenced_tweets.id', 'author_id'] )
    print(mentions)


def get_referenced_tweets(tweets, data_frame):

    length = len(tweets)

    for i in range(length):
    
        tweet = tweets.data[i-1]

        if tweet.referenced_tweets is None:
            print("Nonetype Object: " + tweet.text + ' | ' + 'id Nonetype' + "---- tweet id = " + str(tweet.id))
        
        else:
            tweet_t = tweet.referenced_tweets
            values = np.array([[tweet.id],[tweet_t[i-1]['id']]])
            columns = ['tweet_id', 'ref_tweet']
            temporary_df = pd.DataFrame({'tweet_id': [str(tweet.id)], 'ref_tweet': [str(tweet_t[i-1]['id'])], 'tweets': [str(tweet.text)], 'author_id': [str(tweet.author_id)], 'responded': 'no'})
            data_frame = pd.concat([data_frame, temporary_df], sort=False)
            print("Type Object: " + tweet.text + ' | ' + str(tweet_t[i-1]['id']) + "---- tweet id = " + str(tweet.id))
            temporary_df.tail(10)

    return data_frame

def update_sheets(df_final, wks):
    wks.set_dataframe(df_final,(1,1))





def main():
    
    # tweets = client.get_users_mentions(id=user_id, expansions=['referenced_tweets.id', 'author_id'] )
    # tweets_d = tweets.data

    # df_referenced =  get_referenced_tweets(tweets, df_referenced)
    # mentions = client.get_users_mentions(user_id)

    # df_tweets = pd.DataFrame(data=[[tweet.text, tweet.id, tweet.author_id, 'none', 'no'] for tweet in tweets_d], columns=['tweets', 'tweet_id', 'author_id', 'ref_tweet', 'responded'])
    # df_tweets['author_id'] = df_tweets['author_id'].apply(str)
    # df_tweets['tweet_id'] = df_tweets['tweet_id'].apply(str)
    # df_tweets = df_tweets.append(df_referenced, ignore_index=True)
    # df_tweets = df_tweets.drop_duplicates(subset=["tweet_id"], keep='last')
    print("main just ran")
    # respondToTweet()
    # update_sheets(df_final, wks)



# __name__
if __name__=="__main__":
    main()


    ### THIS IS HOW TO GET ORIGINAL TWEET THAT VIBE BOT REPLIED TO
    # alex = client.get_user(username='VibeCheckBot')
   #  alex_id = alex.data.id

    # tweets = client.get_users_mentions(id=alex_id, expansions=['referenced_tweets.id'] )

    # tweet = tweets.data[0]
    # tweet_tiny = tweet.referenced_tweets

    # tweet_tiny[0]["id"]
import flask
from flask import Flask
import VibeCheckBot
import os
import pygsheets
import pandas
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

import atexit
from apscheduler.schedulers.background import BackgroundScheduler



def job():

    gc = pygsheets.authorize(service_file='/Users/alexs/DataWithAlex_Github/VibeCheckBot_Final/vibecheckbot-351521-6255c4712ef6.json')
    sh = gc.open('VibeCheckBot')
    wks = sh[0]
    df = wks.get_as_df()

    df['author_id'] = df['author_id'].apply(str)
    df['tweet_id'] = df['tweet_id'].apply(str)
    df['tweets'] = df['tweets'].apply(str)
    df['ref_tweet'] = df['ref_tweet'].apply(str)
    df['responded'] = df['responded'].apply(str)

    print("just got google sheet")

    #VibeCheckBot.test()

    df1 = VibeCheckBot.respondToTweet(df)
    wks.set_dataframe(df1,(1,1))

    # VibeCheckBot.update_sheets()
    # print("Success")


scheduler = BackgroundScheduler()
scheduler.add_job(func=job, trigger="interval", seconds=60)
scheduler.start()

application = Flask(__name__)


@application.route("/")
def index():
    return "Follow @vibecheckbot"


atexit.register(lambda: scheduler.shutdown())

if __name__ == "__main__":
    application.run(port=5000, debug=True)
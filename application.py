
# %pip install flask
import flask
from flask import Flask
import VibeCheckBot
import os

import atexit
from apscheduler.schedulers.background import BackgroundScheduler

# data = open("C:\Users\alexs\DataWithAlex_Github\Twitter\VibeCheckBot\tweet_ID.txt","r")

#open(r'C:\Users\alexs\DataWithAlex_Github\Twitter\VibeCheckBot\tweet_ID.txt')


def job():
    VibeCheckBot.respondToTweet()
    print("Success")


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
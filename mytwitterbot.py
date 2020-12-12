# mytwitterbot.py
# IAE 101, Fall 2020
# Project 04 - Building a Twitterbot
# Name:       
# netid:      
# Student ID:
import datetime
import sys
import time
import simple_twit
import random


def main():
    api = simple_twit.create_api()
    simple_twit.version()
    tweets = simple_twit.get_home_timeline(api, 20)
    key_word = "the"
    morning = "Good morning"
    afternoon = "Good afternoon"
    while True:
        for tweet in tweets:
            word_arr = tweet.full_text.split(" ")
            if len(word_arr) > 25:
                words = word_arr
                random.shuffle(words)
                new_sentence = ' '.join(words)
                username = "@" + tweet.user.name + " "
                simple_twit.send_reply_tweet(api, username + new_sentence, tweet.id)
                time.sleep(15)
        time.sleep(300)
        # Sleep 5 minutes
        for tweet in tweets:
            if key_word in tweet.full_text.split(" "):
                datetime_object = datetime.datetime.now()
                username = "@" + tweet.user.name + " "
                if int(datetime_object.hour) > 12:
                    simple_twit.send_reply_tweet(api, username + afternoon, tweet.id)
                else:
                    simple_twit.send_reply_tweet(api, username + morning, tweet.id)
                break
        time.sleep(3600)


if __name__ == "__main__":
    main()

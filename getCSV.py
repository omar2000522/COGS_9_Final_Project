import os
import json
import numpy as np
import pandas as pd

def getTweetText(result):
    if result['truncated']:
        return result['extended_tweet']['full_text']
    else:
        return result['text']

files = os.listdir('data/')
tweet_text = np.array([])
followers_count = np.array([])
favorites = np.array([])
retweets = np.array([])
replies = np.array([])
date = np.array([])

for name in files:
    f = open('data/' + name)
    data = json.load(f)

    for result in data['results']:
        tweet_text = np.append(tweet_text, getTweetText(result))
        followers_count = np.append(followers_count, result['user']['followers_count'])
        favorites = np.append(favorites, result['favorite_count'])
        retweets = np.append(retweets, result['retweet_count'])
        replies = np.append(replies, result['reply_count'])
        date = np.append(date, name[8:-4])

all_tweets = pd.DataFrame().assign(
    ID = np.arange(len(tweet_text)),
    Tweet_text = tweet_text,
    Followers = followers_count,
    Likes = favorites,
    Retweets = retweets,
    Replies = replies,
    Date = date 
)

all_tweets.to_csv('All_Tweets.csv')
all_tweets.groupby('Date').sum().to_csv('Tweets_each_day.csv')


# print(len(followers_count), len(tweet_text), len(date))
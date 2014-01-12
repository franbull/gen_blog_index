import os

import tweepy

def photos(tweet):
    photos = []
    if 'media' in tweet.entities:
        for media in tweet.entities['media']:
            if media['type'] == 'photo':
                photos.append(media['media_url'])
    return photos

def authorize():
    auth = tweepy.OAuthHandler(
            os.environ['TWITTER_CONSUMER_KEY'],
            os.environ['TWITTER_CONSUMER_SECRET']
            )
    auth.set_access_token(
            os.environ['TWITTER_ACCESS_TOKEN'],
            os.environ['TWITTER_ACCESS_TOKEN_SECRET']
            )
    return tweepy.API(auth)

def get_my_tweets():
    return [(t.created_at, t.text, photos(t)) for t in authorize().user_timeline() if not
            t.text.startswith('@') and not t.text.startswith('RT')]

if __name__ == '__main__':
    for t in get_my_tweets():
        print t

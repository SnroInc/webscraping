import tweepy


def twitter_bot() -> None:
    # XXXXXXXXXXXXXXXXXXには自分のコードを設定してください
    ck = 'XXXXXXXXXXXXXXXXXX'
    cs = 'XXXXXXXXXXXXXXXXXX'
    at = 'XXXXXXXXXXXXXXXXXX'
    ats = 'XXXXXXXXXXXXXXXXXX'

    client = tweepy.Client(consumer_key=ck, consumer_secret=cs,
                           access_token=at, access_token_secret=ats)

    client.create_tweet(text='ツイート文 #test #漫画')


if __name__ == '__main__':
    twitter_bot()

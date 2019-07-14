from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sqlite3
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from unidecode import unidecode
import time
import os
os.chdir('C:/Users/muham/Documents/CSC 4309_Natural Language Processing/')



analyzer = SentimentIntensityAnalyzer()

#consumer key, consumer secret, access token, access secret.
ckey="Th9hRu1Nxhsu6JV2hY8iG13NF"
csecret="9FJmHiLhAwsyPPVr35rN3YWAsNqF3sGT8EgIoVESG3sV5ridN9"
atoken='3152933640-A0GZMYt5zOYsE3WlTCwHPhAqq2tLEVkS3MMqDBZ'
asecret='jyqyNDd3qYbCpgENSfNqymvaPBqZjHpyEzAsvyI0E4GeY'

conn = sqlite3.connect('twitter.db')
c = conn.cursor()

def create_table():
    try:
        c.execute("CREATE TABLE IF NOT EXISTS sentiment(unix REAL, tweet TEXT, sentiment REAL)")
        c.execute("CREATE INDEX fast_unix ON sentiment(unix)")
        c.execute("CREATE INDEX fast_tweet ON sentiment(tweet)")
        c.execute("CREATE INDEX fast_sentiment ON sentiment(sentiment)")
        conn.commit()
    except Exception as e:
        print(str(e))
create_table()



class listener(StreamListener):

    def on_data(self, data):
        try:
            data = json.loads(data)
            tweet = unidecode(data['text'])
            time_ms = data['timestamp_ms']
            vs = analyzer.polarity_scores(tweet)
            sentiment = vs['compound']
            a1 = str(time_ms)
            a2 = str(tweet)
            a3 = str(sentiment)
            print(time_ms, tweet, sentiment)
            z = open("Cat.dat", "a+")
            z.write("%-10s" % str("Sentiment: "))
            z.write("%-10s" % a3)
            z.write("%-10s" % str("Timestamp: "))
            z.write("%-15s" % a1)
            z.write("%-10s" % str(" Tweet: "))
            z.write("%-10.100s" % a2)
            z.write("\n")
            #z.write(str("sentiment: ") + a3 + "%-30s" % str(" timestamp: ") + a1 + "%-30s" % str("tweet: ") + a2 + str("\n"))
         
            c.execute("INSERT INTO sentiment (unix, tweet, sentiment) VALUES (?, ?, ?)",
                  (time_ms, tweet, sentiment))
            conn.commit()

        except KeyError as e:
            print(str(e))
        return(True)

    def on_error(self, status):
        print(status)


while True:

    try:
        auth = OAuthHandler(ckey, csecret)
        auth.set_access_token(atoken, asecret)
        twitterStream = Stream(auth, listener())
        twitterStream.filter(track=["#Cat","Kitty","Cat","#Kitty","Kitten","#Kitten"])
      
    except Exception as e:
        print(str(e))
        time.sleep(5)

#Muhamad Arif Lutfi bin Aziz        1315791
#Tun Muhammad Zaim bin Aminuddin    1629501
#Mohd Faris Fitri bin Mohd Hanafi   1614839
#Muhammad Zharif bin Msduki         1611777

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sqlite3
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from unidecode import unidecode
import time

analyzer = SentimentIntensityAnalyzer()

ckey="MVxlYWo3CHfveBrak8cXGn7cS"
csecret="DR7MKOCAaFNIaWid8wHBp90XEllTTEjZOkRLrytkZeCURres8l"
atoken="714513048-qEOFE1GxgcbrthNzcUZOW3u78xqq0OwjrHKfmjBh"
asecret="s5GUNJHZAirJXtVzfGBY6XL2jzYHV25BwYOi5COSUvZ9H"

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
            z = open("Vaccine.dat", "a")
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
        #twitterStream.filter(track=['#NZMosqueShooting', '#ChristchurchMosqueAttack', '#ChristchurchShootings', 'Christchurch Shootings'])
        #twitterStream.filter(track=['#dog', 'dog', 'puppy', '#puppy', 'doggy', '#doggy'])
        twitterStream.filter(track=['pro choice', 'proChoice', '#proChoice', '#antivax', '#antivaccine', 'anti vaccine', 'anti vax', '#vaccine', '#vaccination', '#herdImmunity', 'vaccine', 'vacination', 'herd immunity'])
      
    except Exception as e:
        print(str(e))
        time.sleep(5)

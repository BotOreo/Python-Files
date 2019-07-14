import re 
import tweepy 
from tweepy import OAuthHandler 
from textblob import TextBlob
import sys
import json


  
class TwitterClient(object): 
    ''' 
    Generic Twitter Class for sentiment analysis. 
    '''
    def __init__(self): 
        ''' 
        Class constructor or initialization method. 
        '''
        # keys and tokens from the Twitter Dev Console 
        consumer_key = 'MVxlYWo3CHfveBrak8cXGn7cS'
        consumer_secret = 'DR7MKOCAaFNIaWid8wHBp90XEllTTEjZOkRLrytkZeCURres8l'
        access_token = '714513048-qEOFE1GxgcbrthNzcUZOW3u78xqq0OwjrHKfmjBh'
        access_token_secret = 's5GUNJHZAirJXtVzfGBY6XL2jzYHV25BwYOi5COSUvZ9H'
  
        # attempt authentication 
        try: 
            # create OAuthHandler object 
            self.auth = OAuthHandler(consumer_key, consumer_secret) 
            # set access token and secret 
            self.auth.set_access_token(access_token, access_token_secret) 
            # create tweepy API object to fetch tweets 
            self.api = tweepy.API(self.auth) 
        except: 
            print("Error: Authentication Failed") 
  
    def clean_tweet(self, tweet): 
        ''' 
        Utility function to clean tweet text by removing links, special characters 
        using simple regex statements. 
        '''
        #print("This is without regular expression")
        #non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
        #print(tweet.translate(non_bmp_map))
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split()) 
  
    def get_tweet_sentiment(self, tweet): 
        ''' 
        Utility function to classify sentiment of passed tweet 
        using textblob's sentiment method 
        '''
        # create TextBlob object of passed tweet text 
        analysis = TextBlob(self.clean_tweet(tweet)) 
        # set sentiment 
        if analysis.sentiment.polarity > 0: 
            return 'positive'
        elif analysis.sentiment.polarity == 0: 
            return 'neutral'
        else: 
            return 'negative'
  
    def get_tweets(self, query, count = 1): 
        ''' 
        Main function to fetch tweets and parse them. 
        '''
        # empty list to store parsed tweets 
        tweets = [] 
  
        try: 
            # call twitter api to fetch tweets
            fetched_tweets = open("Christchurch_shooting.dat",'r')
            #fetched_tweets = self.api.search(q = query, count = count)
            '''print("----------------Line 69-----------------------------")
            non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
            print(fetched_tweets.translate(non_bmp_map))
           
            print("----------------Line 69-----------------------------")'''
                
  
            # parsing tweets one by one 
            for tweet in fetched_tweets: 
                # empty dictionary to store required params of a tweet 
                parsed_tweet = {}
                print("----------------Line 69-----------------------------")
                #non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
                print(tweet)
                print("----------------Line 69-----------------------------")
  
                # saving text of tweet 
                parsed_tweet["text"] = tweet.text 
                # saving sentiment of tweet 
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text) 
  
                # appending parsed tweet to tweets list 
                if tweet.retweet_count > 0: 
                    # if tweet has retweets, ensure that it is appended only once 
                    if parsed_tweet not in tweets: 
                        tweets.append(parsed_tweet) 
                else: 
                    tweets.append(parsed_tweet) 
  
            # return parsed tweets 
            return tweets
         
        except tweepy.TweepError as e: 
            # print error (if any) 
            print("Error : " + str(e))
 
  
def main(): 
    # creating object of TwitterClient Class 
    api = TwitterClient() 
    # calling function to get tweets
    tweets = api.get_tweets(query = '#Endgame')
      
    # picking positive tweets from tweets 
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive'] 
    # percentage of positive tweets 
    print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets))) 
    # picking negative tweets from tweets 
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative'] 
    # percentage of negative tweets 
    print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets))) 
    # percentage of neutral tweets
    a1 = len(tweets)
    a2 = len(ntweets)
    a3 = len(ptweets)
    print("a1 is",a1)
    
    print(a2)
    print(a3)
    neutral_tweets = ((a1-a2-a3)/a1)*100
    print("Neutral tweets percentage:"+ str(neutral_tweets) + " %")
    #print("Neutral tweets percentage: {} %\ ".format(100 *((len(tweets) - len(ntweets) - len(ptweets))/len(tweets)))
          #(((len(tweets) - len(ntweets) - len(ptweets))/len(tweets))*100) 
  
    # printing first 5 positive tweets
    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
    print("\n\nPositive tweets:") 
    for tweet in ptweets[:10]: 
        print(tweet['text'].translate(non_bmp_map)) 
   # print(tweets.translate(non_bmp_map))) 
  
    # printing first 5 negative tweets
    
    print("\n\nNegative tweets:") 
    for tweet in ntweets[:10]: 
        print(tweet['text'].translate(non_bmp_map)) 
  
if __name__ == "__main__": 
    # calling main function 
    main() 

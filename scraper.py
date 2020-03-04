import GetOldTweets3 as got
import pandas as pd
import tweepy
import sys


#CONSUMER_KEY = <your consumer key>
#CONSUMER_SECRET = <your consumer secret>
#ACCESS_TOKEN = <your access token>
#ACCESS_TOKEN_SECRET = <your access token secret>

api_key = "zMTZIUjRYv6iwoM9ePbZBbZ9F"
api_secret = "yIkvt5zzbjyXAmhPKV7o2nEQU3mCnHmSL8pjRAfrBSe51z4koY"
access_token_key = "4882418077-H17IYcDzcREjz2pEtuse1d5spmpWxFLETtteQyE"
access_token_secret = "0ikHwuh3Zq6WKMi0LyONvexVYnn2C8Lwjf2GnM1RkFxC3"

auth = tweepy.OAuthHandler(api_key,api_secret)
auth.set_access_token(access_token_key,access_token_secret)

api = tweepy.API(auth)

def username_tweets_to_csv(username,count,date_since,date_until):
    tweetCriteria = got.manager.TweetCriteria().setUsername(username).setMaxTweets(count).setSince(date_since).setUntil(date_until)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    user_tweets = [[tweet.username,tweet.date,tweet.text,tweet.retweets,tweet.favorites,tweet.hashtags] for tweet in tweets]
    tweets_df = pd.DataFrame(user_tweets, columns = ['Username','Date-Time','Text','Retweets','Favorites','Hashtags'])
    tweets_df.to_csv('{}-{}k-tweets.csv'.format(username, int(count/1000)), sep=',')

def text_query_to_csv(text_query,count,date_since,date_until):
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(text_query).setMaxTweets(count).setSince(date_since).setUntil(date_until)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    text_tweets = [[tweet.username,tweet.date,tweet.text,tweet.retweets,tweet.favorites,tweet.hashtags] for tweet in tweets]
    tweets_df = pd.DataFrame(text_tweets, columns = ['Username','Date-Time','Text','Retweets','Favorites','Hashtags'])
    tweets_df.to_csv('{}-{}k-tweets.csv'.format(text_query, int(count/1000)), sep=',')

print("1. Search by account")
print("2. Search by keyword")
ch=int(input("enter your choice: "))
if ch==1:
	username=input("enter username: ")
	count=int(input("enter the number of tweets to be scraped: "))
	date_since=input("enter the date since when the data has to be scraped: ")
	date_until=input("enter the date till which the data has to be scraped: ")
	username_tweets_to_csv(username,count,date_since,date_until)
	print("data scraping completed")
if ch==2:
	text_query=input("enter keyword: ")
	count=int(input("enter no. of tweets to be scraped: "))
	date_since=input("enter the date since when the data has to be scraped: ")
	date_until=input("enter the date till which the data has to be scraped: ")
	text_query_to_csv(text_query,count,date_since,date_until)
	print("data scraping completed")


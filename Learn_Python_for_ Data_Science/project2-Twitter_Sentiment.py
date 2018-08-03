import tweepy
from textblob import textblob
import csv


consumer_key = key1
consumer_secret = key2


access_token = token1
access_token_secret = token2

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api.tweepy.API(auth)

outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)

public_tweets = api.search('Trump')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)

	if analysis.sentiment.polarity >= 0:
		label = 'Positive'
	else:
		label = 'Negative'
	outputWriter.writerow([label, tweet.text])


outputFile.close()
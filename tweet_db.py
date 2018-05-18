
import csv
import accessing_tweets
telecom = raw_input('Enter the telecom company name : ')

tweet_data = open('tweet_data.csv','a')
t = accessing_tweets.retrive_tweets(telecom)
for tweets in t[0]:
    tweet_data.write((str(tweets.created_at).encode('utf-8')).replace(',','-')+','+t[1]+','+((tweets.text.encode('utf-8')).replace(',','')).replace('\n','')+'\n')
tweet_data.close()

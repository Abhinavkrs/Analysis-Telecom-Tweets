import csv
import matplotlib
import matplotlib.pyplot as plt
import numpy
import numpy as np
import textblob
from textblob import TextBlob
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


tweet_dbw = open('tweet_data.csv','a')
tweet_dbr = open('tweet_data.csv','r')


pos = 0
neg = 0
neut = 0  
for tweet in tweet_dbr:
    sc = TextBlob((tweet.split(','))[2])
    score = sc.sentiment.polarity
        
    if(score>0):
        pos=pos+1
        i = 'Postive'
    elif (score<0):
        neg=neg+1
        i = 'Negative'
    else:
        neut=neut+1
        i = 'Neutral'
        
        
    tweet_dbw.write(','+','+','+str(score)+','+ i+'\n')
  
tweet_dbr.close()
tweet_dbw.close()
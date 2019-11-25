import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.utils.extmath import randomized_svd
import pandas as pd
import numpy as np
import json
import sys
import re
import os

directory = '/Users/bharatsuri/Github/CS_5243/project/data/'
review = directory + 'review.json'
restaurants = directory + 'restaurants.pkl'
restaurants_review_json = directory + 'restaurants_review.json'
restaurants_review_pkl = directory + 'restaurants_review.pkl'

ps = PorterStemmer()
stop_words = set(stopwords.words('english'))
tk = RegexpTokenizer(r'\w+')

def clean_text(s):
    tokens = tk.tokenize(s.lower())
    text = nltk.Text(tokens)
    words_raw = [w.lower() for w in text.tokens]
    words_raw = [ps.stem(w) for w in words_raw if w not in stop_words and len(w) > 1]
    words_raw = [w for w in words_raw if re.compile('^[a-z]+$').match(w)]

    return ' '.join(words_raw)

reviews = []

restaurants_df = pd.read_pickle(restaurants)
restaurants_id = set(restaurants_df['business_id'].unique())

c = 0
with open(review, 'r') as f:
    with open(restaurants_review_json, 'w+') as out_file:
        for line in f:
            c += 1
            print ('At review # {}'.format(c), end='\r')
            b_id = json.loads(line)['business_id']
            if b_id in restaurants_id:
                d = json.loads(line)
                d['date'] = pd.to_datetime(d['date'])
                d['year'] = d['date'].year
                if d['year'] == 2018:
                    d['stemmed_text'] = clean_text(d['text'])
                    if d['stemmed_text'] != None:
                        reviews.append(d)
                        out_file.write(line)

print (c, ' reviews')
reviews = pd.DataFrame(reviews)
print (reviews.head(10))
reviews = reviews[reviews['year'] == 2018]
reviews.to_pickle(restaurants_review_pkl)

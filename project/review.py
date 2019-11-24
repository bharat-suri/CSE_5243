import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import RegexpTokenizer
import pandas as pd
import numpy as np
import json
import sys
import os

directory = '/Users/bharatsuri/Github/CS_5243/project/data/'
review = directory + 'review.json'
restaurants = directory + 'restaurants.pkl'
restaurants_review_json = directory + 'restaurants_review.json'
restaurants_review_pkl = directory + 'restaurants_review.pkl'

stop_words = set(stopwords.words('english'))
tokenizer = RegexpTokenizer(r'\w+')

def clean_text(text):
    tokens = tokenizer.tokenize(text.lower())
    return [w for w in tokens if w not in stop_words and len(w) > 1]

reviews = []

restaurants_df = pd.read_pickle(restaurants)
restaurants_id = set(restaurants_df['business_id'].unique())

c = 0
with open(review, 'r') as f:
    with open(restaurants_review_json, 'w+') as out_file:
        for line in f:
            b_id = json.loads(line)['business_id']
            if b_id in restaurants_id:
                c += 1
                d = json.loads(line)
                d['text'] = clean_text(d['text'])
                d['date'] = pd.to_datetime(d['date'])
                reviews.append(d)
                out_file.write(line)
                print ('At review # {}'.format(c), end='\r')

print (c, ' reviews')
reviews = pd.DataFrame(reviews)
print (reviews.head(10))
reviews = reviews[reviews['year'] == 2018]
reviews.to_pickle(restaurants_review_pkl)

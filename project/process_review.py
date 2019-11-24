import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.utils.extmath import randomized_svd
import pandas as pd
from pandas.io.json import json_normalize
import numpy as np
import json
import sys
import re
import os

directory = '/Users/bharatsuri/Github/CS_5243/project/data/'
restaurants = directory + 'restaurants.pkl'
restaurants_review_json = directory + 'restaurants_review.json'
restaurants_review_pkl = directory + 'restaurants_review.pkl'

review_df = pd.read_pickle(restaurants_review_pkl)
review_df = review_df.set_index('review_id')

restaurant_df = pd.read_pickle(restaurants)
restaurant_df = restaurant_df.set_index('business_id')

print (review_df.head(5))
print (review_df.shape)
print (restaurant_df.head(5))
print (restaurant_df.shape)

corpus = review_df['stemmed_text'].values
vocab = set()
for s in corpus:
    vocab.update(s.split())
print (len(vocab))
groups = review_df.groupby(review_df['date'].dt.to_period('Q'))

for idx, group in groups:
    print (group.shape)

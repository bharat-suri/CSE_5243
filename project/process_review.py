import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import RegexpTokenizer
import pandas as pd
import numpy as np
import json
import sys
import os

directory = '/Users/bharatsuri/Github/CS_5243/project/data/'
restaurants = directory + 'restaurants.pkl'
restaurants_review_json = directory + 'restaurants_review.json'
restaurants_review_pkl = directory + 'restaurants_review.pkl'

df = pd.read_pickle(restaurants_review_pkl)

print (df.head(5))

vocab = set()
for s in df['text'].values:
    vocab.update(s)

print (len(vocab))

groups = df.groupby(df['date'].dt.to_period('Q'))

for idx, group in groups:
    print (group.shape)

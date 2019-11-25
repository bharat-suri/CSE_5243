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
restaurants = directory + 'restaurants.pkl'
restaurants_review_json = directory + 'restaurants_review.json'
restaurants_review_pkl = directory + 'restaurants_review.pkl'

review_df = pd.read_pickle(restaurants_review_pkl)
review_df = review_df.set_index('review_id')

# restaurant_df = pd.read_pickle(restaurants)
# restaurant_df = restaurant_df.set_index('business_id')

print (review_df.head(5))
# print (restaurant_df.head(5))

corpus = review_df['text'].values
stemmed_corpus = review_df['stemmed_text'].values
vocab = set()
for s in stemmed_corpus:
    vocab.update(s.split())

vect = CountVectorizer()
vect.fit(stemmed_corpus)
X = vect.transform(stemmed_corpus).toarray()

tf_idf = pd.DataFrame(
    X.transpose(),
    index=vect.get_feature_names(),
    columns=review_df.index
)

n_concepts = 15
concepts = [(lambda x: 'concept{:d}'.format(x))(i) for i in range(1,n_concepts+1)]
U, Sigma, VT = randomized_svd(X, n_components=n_concepts)

U_df = pd.DataFrame(
    U,
    index=review_df.index,
    columns=concepts
)
U_df['content'] = corpus

Sigma_df = pd.DataFrame(
    np.diag(Sigma),
    index=concepts,
    columns=concepts
)

VT_df = pd.DataFrame(
    VT,
    index=concepts,
    columns=vocab
)

print (U_df)
print (Sigma_df)
print (VT_df.T)


# groups = review_df.groupby(review_df['date'].dt.to_period('Q'))

# restaurant_features = [
#     'name',
#     'latitude',
#     'longitude',
#     'stars',
#     'review_count',
# ]

# expanded_restaurant = restaurant_df['categories'].str.split(', ', expand=True).stack().str.get_dummies().sum(level=0)


# r = 0
# for idx, row in review_df.iterrows():
#     b_id = row['business_id']
#     for c in restaurant_features:
#         review_df.loc[idx, c] = restaurant_df[c][b_id]
#     for c in expanded_restaurant:
#         review_df.loc[idx, c] = expanded_restaurant[c][b_id]
#     r += 1
#     print ('At review ', r, end='\r')

# review_df.to_pickle(restaurants_review_pkl)

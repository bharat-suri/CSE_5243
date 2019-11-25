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

def run_svd(df):
    corpus = df['text'].values
    stemmed_corpus = df['stemmed_text'].values
    vocab = set()
    for s in stemmed_corpus:
        vocab.update(s.split())

    vect = CountVectorizer()
    vect.fit(stemmed_corpus)
    X = vect.transform(stemmed_corpus).toarray()

    # tf_idf = pd.DataFrame(
    #     X.transpose(),
    #     index=vect.get_feature_names(),
    #     columns=df.index
    # )

    # print (tf_idf)

    n_concepts = 5
    concepts = [(lambda x: 'concept{:d}'.format(x))(i) for i in range(1,n_concepts+1)]
    U, Sigma, VT = randomized_svd(X, n_components=n_concepts)

    U_df = pd.DataFrame(
        U,
        index=df.index,
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

print ('SVD for 2018...')
run_svd(review_df)


groups = review_df.groupby(review_df['date'].dt.to_period('Q'))

for idx, group in groups:
    print (idx)
    run_svd(group)

# expanded_restaurant = restaurant_df['categories'].str.split(', ', expand=True).stack().str.get_dummies().sum(level=0)

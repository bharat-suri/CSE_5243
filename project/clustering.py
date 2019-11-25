import pandas as pd
import numpy as np
from sklearn.cluster import SpectralClustering

directory = '/Users/bharatsuri/Github/CS_5243/project/data/'
restaurants_review_pkl = directory + 'restaurants_review.pkl'
review_df = pd.read_pickle(restaurants_review_pkl)

groups = review_df.groupby(review_df['date'].dt.to_period('Q'))

features = [
    'stars',
    'useful',
    'concept1',
    'concept2',
    'concept3',
    'concept4',
    'concept5'
]

for idx, group in groups:
    print ('Running clustering for ', idx)
    X = group[features].values
    clustering = SpectralClustering(n_clusters=2).fit(X)
    df = pd.DataFrame(
        clustering.labels_,
        index=group.index
    )
    df.to_pickle(idx + '.pkl')
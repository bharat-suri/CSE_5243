import pandas as pd
import numpy as np

directory = '/Users/bharatsuri/Github/CS_5243/project/data/'
business = 'business_df.pkl'


df = pd.read_pickle(directory + business)
print (df.head(10))

categories = {}
r = 0
for idx, row in df.iterrows():
    print ('At row # {}'.format(r), end='\r')
    r += 1
    if row['categories'] != None:
        category = row['categories'].split(', ')
        for c in category:
            if c not in categories:
                categories[c] = 1
            else:
                categories[c] += 1

categories = sorted(categories.items(), key=lambda x: x[1], reverse=True)

print ('Number of unique categories: ', len(categories))
print ('Top 10 most frequent categories')
print (categories[:10])
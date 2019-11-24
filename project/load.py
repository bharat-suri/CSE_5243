import pandas as pd
import numpy as np

directory = '/Users/bharatsuri/Github/CS_5243/project/data/'
business = directory + 'business.pkl'


df = pd.read_pickle(business)
print (df.head(10))

categories = {}
r = 0
for idx, row in df.iterrows():
    print ('At row # {}'.format(r), end='\r')
    r += 1
    if row['categories'] != None:
        for c in row['categories'].split(', '):
            if c not in categories:
                categories[c] = 1
            else:
                categories[c] += 1

categories = sorted(categories.items(), key=lambda x: x[1], reverse=True)

print ('Number of unique categories: ', len(categories))
print ('Top 50 most frequent categories')
for x in categories[:50]:
    print (x[0], ': ', x[1])
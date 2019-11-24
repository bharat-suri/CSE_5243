import pandas as pd
import json
import sys

directory = '/Users/bharatsuri/Github/CS_5243/project/data/'
review = 'review.json'
restaurants = 'restaurants_df.pkl'
restaurants_review_json = directory + 'restaurants_review.json'

restaurants_df = pd.read_pickle(directory + restaurants)
restaurants_id = set(restaurants_df['business_id'].unique())

filename = directory + review

c = 0
with open(filename, 'r') as f:
    with open(restaurants_review_json, 'w+') as out_file:
        for line in f:
            b_id = json.loads(line)['business_id']
            if b_id in restaurants_id:
                c += 1
                out_file.write(line)

print (c, ' reviews')
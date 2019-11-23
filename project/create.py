#!/usr/bin/env python
# coding: utf-8

import time
import json
import pandas as pd
import numpy as np


directory = 'data/'
review = directory + 'review.json'
user = directory + 'user.json'
business = directory + 'business.json'


# Business
start = time.time()
c = 0
b = []
categories = {}
with open(business, 'r') as f:
    for line in f:
        json_line = json.loads(line)
        b.append(json_line)
        c += 1


df = pd.DataFrame(b)
del b

print ('Business file')
print (time.time() - start, ' s')
print (c)
print (df.head())
df.to_pickle(directory + 'business_df.pkl')
del df


# User
# start = time.time()
# c = 0
# b = []
# with open(user, 'r') as f:
#     for line in f:
#         json_line = json.loads(line)
#         b.append(json_line)
#         c += 1

# df = pd.DataFrame(b)
# del b

# print ('User file')
# print (time.time() - start, ' s')
# print (c)
# print (df.head())
# df.to_pickle(directory + 'user_df.pkl')
# del df


# Review
# start = time.time()
# c = 0
# b = []
# with open(review, 'r') as f:
#     for line in f:
#         json_line = json.loads(line)
#         b.append(json_line)
#         c += 1

# df = pd.DataFrame(b)
# del b


# print ('Review file')
# print (time.time() - start, ' s')
# print (c)
# print (df.head())
# df.to_pickle(directory + 'review_df.pkl')
# del df

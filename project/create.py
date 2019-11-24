#!/usr/bin/env python
# coding: utf-8

import time
import json
import pandas as pd
import numpy as np


directory = '/Users/bharatsuri/Github/CS_5243/project/data/'
business = directory + 'business.json'
business_df = directory + 'business.pkl'


# Business
start = time.time()
c = 0
b = []
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
df.to_pickle(business_df)
del df

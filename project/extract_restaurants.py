import pandas as pd

directory = '/Users/bharatsuri/Github/CS_5243/project/data/'
business = 'business_df.pkl'
restaurants = 'restaurants_df.pkl'
filename = directory + business

df = pd.read_pickle(filename)
category = 'Restaurants'
features = [
    'business_id',
    'name',
    'city',
    'state',
    'latitude',
    'longitude',
    'stars',
    'review_count',
    'is_open',
    'attributes',
    'categories'
]
print (df.head(10), '\n')
print ('Total number of rows: {}'.format(df.shape[0]), '\n')
df = df[features]
df = df.dropna()
print ('Total number of rows after removing missing values: {}'.format(df.shape[0]), '\n')
category = 'Restaurants'
r = 0

df = df[df['categories'].str.contains(category)]

print ('Total number of Restaurants: {}'.format(df.shape[0]))
df.to_pickle(directory + restaurants)

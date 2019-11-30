import pandas as pd
import json

with open('business.json', encoding="utf8") as json_file:
    data = json_file.readlines()
    data = list(map(json.loads, data))


from pandas.io.json import json_normalize

df = json_normalize(data)

df1=(df.categories.str.split('\s*,\s*', expand=True)
   .stack()
   .str.get_dummies()
   .sum(level=0))
#df=df.join(df1)
df1.head()
#print(df.astype(bool).sum(axis=0))
#df.to_pickle('business.pkl')

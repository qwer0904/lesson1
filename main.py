import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

one_hot_data = pd.DataFrame()

for unique_value in data['whoAmI'].unique():
    one_hot_data[f'{unique_value}_indicator'] = (data['whoAmI'] == unique_value).astype(int)

data = pd.concat([data, one_hot_data], axis=1)

print(data.head())

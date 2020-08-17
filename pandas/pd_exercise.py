#  https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html

import numpy as np
import pandas as pd

# series = one-dimensional labeled array, can convert dictionary to series

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])

print(s)
print(s.index)
print(s['a'])

d = {'b': 1, 'c': 2, 'd': 3}
s2 = pd.Series(d)
print(s2)
print(s2.dtype)

# series  can  also  include name attribute
s3 =  pd.Series(np.random.randn(5), name='something')
print(s3.name)
s3 = s3.rename('different')
print(s3.name)

### Data Frame --> 2-dimensional labeled structure with columns of differrent types ... almost like SQL table

# iputs Dict of 1D ndarrays, lists, dicts, series
#  2d numpy.ndarray 
# Series, Dataframe 

# Dicts of Series 
d = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
    'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df)

print(df.index)
print(df.columns)

# dicts of ndarrays / lists 
d = {'one': [1., 2., 3., 4.],
    'two': [4., 3., 2., 1.]}

df = pd.DataFrame(d)
print(df)

# change index name
df = pd.DataFrame(d, index=['a','b','c','d'])
print(df)

# from structured or record array
data = np.zeros((2, ), dtype=[('A', 'i4'), ('B', 'f4'), ('C', 'a10')])
data[:] = [(1, 2., 'Hello'), (2, 3., "World")]
d = pd.DataFrame(data)
print(d)

#  from a list of dics 
data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
d2 = pd.DataFrame(data2)
print(d2)
# rename index
d2 = pd.DataFrame(data2, index=['first', 'second'])
print(d2)

############https://realpython.com/pandas-dataframe/#:~:text=DataFrames%20are%20similar%20to%20SQL,the%20Python%20and%20NumPy%20ecosystems. 

data = {
    'name': ['Xavier', 'Ann', 'Jana', 'Yi', 'Robin', 'Amal', 'Nori'],
    'city': ['Mexico City', 'Toronto', 'Prague', 'Shanghai', 'Manchester', 'Cairo', 'Osaka'],
    'age': [41, 28, 33, 34, 38, 31, 37],
    'py-score': [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0]
}

row_labels = [101, 102, 103, 104, 105, 106, 107]

df = pd.DataFrame(data, index=row_labels)
print(df)

# print head, and first 2 records 
print(df.head(n=2))
# print last 2 
print(df.tail(n=2))

# access column 
cities =  df['city']
print(cities)
print(cities[102])

# access whole row 
print(df.loc[103])




















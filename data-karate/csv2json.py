import pandas as pd

df = pd.read_csv('weather_2012.csv')
df.to_json('weather_2012.json')
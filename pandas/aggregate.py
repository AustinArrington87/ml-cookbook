import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.mpl_style', 'default') # Make the graphs a bit prettier
plt.rcParams['figure.figsize'] = (15, 5)
plt.rcParams['font.family'] = 'sans-serif'

# This is necessary to show lots of columns in pandas 0.12. 
# Not necessary in pandas 0.13.
pd.set_option('display.width', 5000) 
pd.set_option('display.max_columns', 60)

bikes = pd.read_csv('bikes.csv', sep=';', encoding='latin-1', parse_dates=['Date'], dayfirst=True, index_col='Date')
# get names of columns
data_top = bikes.head()
#print(data_top)
#plt.show(bikes['Berri 1'].plot())

# create data frame with just Berri path
berri_bikes = bikes['Berri 1'].copy()
#print(berri_bikes[:5])

# get weekday
#print(berri_bikes.index)
#print(berri_bikes.index.day)

#  change to DF 
berri_bikes = pd.DataFrame(berri_bikes)
#print(berri_bikes)
weekday  = berri_bikes.index.weekday

berri_bikes['weekday'] = weekday
print(berri_bikes[:5])

# now aggregate by weekday using groupby
weekday_counts = berri_bikes.groupby('weekday').aggregate(sum)
print(weekday_counts)

# change numbers to  days of week  
weekday_counts.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(weekday_counts)

plt.show(weekday_counts.plot(kind='bar'))

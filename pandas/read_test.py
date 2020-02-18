#%matplotlib inline

import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.mpl_style', 'default') # Make the graphs a bit prettier
plt.rcParams['figure.figsize'] = (15, 5)

fixed_df = pd.read_csv('bikes.csv', sep=';', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')

#print(fixed_df[:3])

fixed_df_graph = fixed_df.plot(figsize=(15, 10))
plt.show(fixed_df_graph)

#  selecting column 
#print(fixed_df['Berri 1'])
# plot column
plot1 = fixed_df['Berri 1'].plot()

## dealing w larger datasets  
complaints = pd.read_csv('311-service-requests.csv')
#print(complaints)

# print whole column
complaintType = complaints['Complaint Type']
#print(complaintType)

# print first 5 rows using slice 
complaintSample = complaints[:5]
#print(complaintSample)

# combine to get firstt 5 rows of a  column 
complaintSample2 = complaints['Complaint Type'][:5]
#print(complaintSample2)

# subset multiple columns  (first 10 rows)
complaintSample3 = complaints[['Complaint Type', 'Borough'][:10]]
#print(complaintSample3)

# what is the most common complaint? 
commonComplaint = complaints['Complaint Type'].value_counts()
#print(commonComplaint)

# 10 most common complaints
top10Com = commonComplaint[:10]
print(top10Com)
top10ComGraph = commonComplaint[:10].plot(kind='bar')
#print(top10ComGraph)
# show graph
#plt.show(top10ComGraph)

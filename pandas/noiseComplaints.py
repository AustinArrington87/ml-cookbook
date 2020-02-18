import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#   make graphs bigger
pd.set_option('display.mpl_style', 'default')
plt.rcParams['figure.figsize'] = (15, 5)

# show alot of columns
pd.set_option('display.width', 5000)
pd.set_option('display.max_columns', 60)

complaints = pd.read_csv('311-service-requests.csv')

#print(complaints[:5])
# to get noise  complaints, need to set complaint type column equal to

noise_complaints = complaints[complaints['Complaint Type'] == "Noise - Street/Sidewalk"]
#print(noise_complaints[:3])
#boolean
#print(complaints['Complaint Type'] == "Noise - Street/Sidewalk")

#  combine conditions
is_noise = complaints['Complaint Type'] == "Noise - Street/Sidewalk"
in_brooklyn = complaints['Borough'] == "BROOKLYN"
#print(complaints[is_noise & in_brooklyn][:5])

# multiple columns
#print(complaints[is_noise & in_brooklyn][['Complaint Type', 'Borough', 'Created Date', 'Descriptor']][:10])

# which borough has most noise complaints
noise_complaints = complaints[is_noise]
#print(noise_complaints['Borough'].value_counts())

# look at ratio 
noise_complaint_counts = noise_complaints['Borough'].value_counts()
complaint_counts = complaints['Borough'].value_counts()

noiseComplaintRat = noise_complaint_counts / complaint_counts.astype(float)
print(noiseComplaintRat)
plt.show(noiseComplaintRat.plot(kind='bar'))


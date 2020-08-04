import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
import statistics

x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([5, 20, 14, 32, 22, 38])

print(x)
print(y)

model = LinearRegression().fit(x,y)

r_sq = model.score(x,y)
print("coefficient of determination:", r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)

y_pred = model.intercept_ + model.coef_ * x
print('predicted response: ', y_pred, sep='\n')

### different model
x_new = np.arange(5).reshape((-1,1))
print(x_new)
y_new = model.predict(x_new)
print(y_new)

###########INGEST Data

data = pd.read_csv('weather_2012.csv')
print(data.head())

# define independent variable - temp C
temp = data['Temp (C)'].values
print("ST DEV:", statistics.stdev(temp))
print("Mean:", statistics.mean(temp))
print("ST DEV:", np.std(temp))
print("Mean:", np.mean(temp))

# define dependent variable - humidity
relHum = data['Rel Hum (%)'].values
#print(relHum)

# reshape 
temp = np.array(temp).reshape((-1, 1))
humModel = LinearRegression().fit(temp,relHum)

print(humModel)

humModel_pred = humModel.intercept_ + humModel.coef_ * temp
print('predicted Hum response: ', humModel_pred, sep='\n')

dewPoint = data['Dew Point Temp (C)'].values
dewPoint = np.array(dewPoint).reshape((-1, 1))
dewPointPred = humModel.predict(dewPoint)
print(dewPointPred)


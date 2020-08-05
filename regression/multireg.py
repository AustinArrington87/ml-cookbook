import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
import statistics

# Multiple Regression
#  multi-dimension array for dependent variables
x = np.array([[0, 1], [5, 1], [15, 2], [25, 5], [35, 11], [45, 15], [55, 34], [60, 35]])
y = np.array([4, 5, 20, 14, 32, 22, 38, 43])

print(x)
print(y)

model = LinearRegression().fit(x,y)

r_sq = model.score(x,y)
print("R2:", r_sq)
print("intercept:", model.intercept_)
print('slope:', model.coef_)

y_pred = model.predict(x)
print('predicted response:', y_pred, sep='\n')

### Ingest Data
data = pd.read_csv('weather_2012.csv')
print(data.head())

# define independent variable - temp C
temp = data['Temp (C)'].values
#temp = np.array(temp).reshape((-1, 1))
dewPoint = data['Dew Point Temp (C)'].values
#dewPoint = np.array(dewPoint).reshape((-1, 1))
# define dependent variable - humidity
relHum = data['Rel Hum (%)'].values

# convert independent vars into two-dimensional list
tempList = list(temp)
dewPointList = list(dewPoint)

indVars = [list(x) for x in zip(tempList, dewPointList)]
#print(indVars)

indVars = np.array(indVars)

humModel = LinearRegression().fit(indVars, relHum)
print("R2:", humModel.score(indVars, relHum))
print("intercept:", humModel.intercept_)
print('slope:', humModel.coef_)





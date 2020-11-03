import numpy as np
from sklearn.linear_model import LinearRegression
from numpy import genfromtxt

my_data = genfromtxt('rs-01.csv', delimiter=',')

#extracts data from sensors, comparing each sensor to the previous
x = np.array(my_data[:,1]).reshape(-1,1)
y = np.array(my_data[:,2])

x2 = np.array(my_data[:,2]).reshape(-1,1)
y2 = np.array(my_data[:,3])

x3 = np.array(my_data[:,3]).reshape(-1,1)
y3 = np.array(my_data[:,4])

#Creates Linear Regression model for each sensor 
model = LinearRegression().fit(x,y)

sensor2 = LinearRegression().fit(x2,y2)

sensor3 = LinearRegression().fit(x3,y3)


#scores model, intercept, coefficient, and prediction
r_sq = model.score(x,y)

print('coefficient of determination', r_sq)

print('intercept:', model.intercept_)

print('slope:', model.coef_)

y_pred = model.predict(x)

print('predicted response:', y_pred, sep='\n')

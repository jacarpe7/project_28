import numpy as np
from sklearn.linear_model import LinearRegression
from numpy import genfromtxt

my_data = genfromtxt('rs-01.csv', delimiter=',')

x = np.array(my_data[:,1]).reshape(-1,1)
y = np.array(my_data[:,2])

#print(x)
#print(y)

model = LinearRegression().fit(x,y)

r_sq = model.score(x,y)

print('coefficient of determination', r_sq)

print('intercept:', model.intercept_)

print('slope:', model.coef_)

y_pred = model.predict(x)

print('predicted response:', y_pred, sep='\n')

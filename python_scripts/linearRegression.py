import pandas
import matplotlib.pyplot as plt
import numpy as np
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from numpy import genfromtxt

my_data = genfromtxt('rs-01.csv', delimiter=',')

#extracts data from sensors, comparing each sensor to the previous
x = np.array(my_data[:,1]).reshape(-1,1)
y = np.array(my_data[:,2])

x2 = np.array(my_data[:,2]).reshape(-1,1)
y2 = np.array(my_data[:,3])

x3 = np.array(my_data[:,3]).reshape(-1,1)
y3 = np.array(my_data[:,4])

seed = 7

#prepare models
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))

# evaluate each model in turn
results = []
names = []
scoring = 'accuracy'
for name, model in models:
	kfold = model_selection.KFold(n_splits=10, random_state=seed)
	cv_results = model_selection.cross_val_score(model, x, y, cv=kfold, scoring=scoring)
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)
# boxplot algorithm comparison
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()



'''
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
'''

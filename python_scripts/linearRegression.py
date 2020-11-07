import pandas as pd 
import numpy as np 
import pickle 
import matplotlib.pyplot as plt 
from scipy import stats 
import tensorflow as tf 
import seaborn as sns 
from sklearn import metrics 
from sklearn.model_selection import train_test_split
from numpy import genfromtxt

my_data = genfromtxt('rs-01.csv', delimiter=',')

np.random.seed(42)

#extracts data from sensors, comparing each sensor to the previous
X = np.array(my_data[:,1]).reshape(-1,1)
y = np.array(my_data[:,2])

df = pd.read_csv('rs-01.csv')

df.head(5)

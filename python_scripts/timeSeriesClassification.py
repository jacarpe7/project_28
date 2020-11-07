import pandas as pd
import numpy as np
%matplotlib inline
import matplotlib.pyplot as plt
from os import listdir
from keras.preprocessing import sequence
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM

from keras.optimizers import Adam
from keras.models import load_model
from keras.callbacks import ModelCheckpoint

df1 = pd.read_csv(‘/MovementAAL/dataset/MovementAAL_RSS_1.csv')
df2 = pd.read_csv('/MovementAAL/dataset/MovementAAL_RSS_2.csv')

df1.head()
df2.head()

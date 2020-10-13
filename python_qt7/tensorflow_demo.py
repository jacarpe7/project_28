# -*- coding: utf-8 -*-
"""
This is file demos running basic normalization of data on a NumPy object
that is created from a Pandas DataFrame object in TensorFlow.  It's primary
purpose is to confirm that TensorFlow is setup on a developer environment. 
If this file compiles and executes you are properly configured.

Created on Fri Oct  9 07:09:29 2020

@author: Josh Carpenter, with excerpts taken from tensorflow.org tutorials:
    https://www.tensorflow.org/tutorials/load_data/csv
"""

import pandas as pd
import numpy as np

import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.layers.experimental import preprocessing

# Import into TensorFlow from a Pandas DataFrame
data = pd.read_csv(r'data/sample_qt7_data.csv')

# Filter only rows which have Delta0 value > 2
data = data.loc[data['Delta0'] > 2]

# Gets column 'Delta0'
delta_col = pd.DataFrame(data, columns = ['Delta0'])

# Put data into a NumPy array
array = np.array(delta_col)

# Print the data object before normalization
print(array)

# Some basic preprocessing with TensorFlow
normalize = preprocessing.Normalization()
normalize.adapt(array)

# Print the data object after normalization
print(array)
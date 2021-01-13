#needed imports from Pandas, Numpy, Pickle, Matplot, Keras
import pandas as pd
import numpy as np
import pickle
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

#loading the exported pkl model and testing the accuracy score
model = load_model('best_model.pkl')


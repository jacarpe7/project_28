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

#loading raw data
path = 'new_model/dataset-new/Null/stream_'
sequences = list()
cols_to_use = [0,1,2,3]
for i in range (200):
    file_path = path + str(i) + '.csv'
    print(file_path)
    df = pd.read_csv(file_path, usecols=cols_to_use , header=0, index_col=None)
    values = df.values
    sequences.append(values)

path = 'new_model/dataset-new/LeftSwipe/stream_'
for i in range (200):
    file_path = path + str(i) + '.csv'
    print(file_path)
    df = pd.read_csv(file_path, usecols=cols_to_use , header=0, index_col=None)
    values = df.values
    sequences.append(values)

path = 'new_model/dataset-new/RightSwipe/stream_'
for i in range (200):
    file_path = path + str(i) + '.csv'
    print(file_path)
    df = pd.read_csv(file_path, usecols=cols_to_use , header=0, index_col=None)
    values = df.values
    sequences.append(values)

path = 'new_model/dataset-new/FullActivity/stream_'
for i in range (200):
    file_path = path + str(i) + '.csv'
    print(file_path)
    df = pd.read_csv(file_path, usecols=cols_to_use , header=0, index_col=None)
    values = df.values
    sequences.append(values)

#target values
targets = pd.read_csv('new_model/dataset-new/Movement_target.csv')
targets = targets.values[:,1]

print(targets)

#Loading grouping
groups = pd.read_csv('new_model/dataset-new/groups/Movement_DatasetGroup.csv', header=0)
groups = groups.values[:,1]

print(groups)

#truncate the sequence to length 30
from keras.preprocessing import sequence
seq_len = 30

print(sequences[1])

#Training data based on group 2
train = [sequences[i] for i in range(len(groups)) if (groups[i]==2)]
validation = [sequences[i] for i in range(len(groups)) if groups[i]==1]
test = [sequences[i] for i in range(len(groups)) if groups[i]==3]

#train target based on group 2
train_target = [targets[i] for i in range(len(groups)) if (groups[i]==2)]
validation_target = [targets[i] for i in range(len(groups)) if groups[i]==1]
test_target = [targets[i] for i in range(len(groups)) if groups[i]==3]

#creating np.arrays for each dataset
train = np.array(train)
validation = np.array(validation)
test = np.array(test)

#training target data
train_target = np.array(train_target)
train_target = (train_target+1)/2

#validation target
validation_target = np.array(validation_target)
validation_target = (validation_target+1)/2

#test data and target test
test_target = np.array(test_target)
test_target = (test_target+1)/2

#adding the LSTM to the model and printing the summary
model = Sequential()
model.add(LSTM(800, input_shape=(seq_len, 4)))
model.add(Dense(1, activation='sigmoid'))
model.summary()
print(model.summary())


adam = Adam(lr=0.001)
chk = ModelCheckpoint('best_model.pkl', monitor='val_accuracy', save_best_only=True, mode='max', verbose=1)
model.compile(loss='binary_crossentropy', optimizer=adam, metrics=['accuracy'])
model.fit(train, train_target, epochs=5, batch_size=800, callbacks=[chk], validation_data=(validation,validation_target))

#loading the exported pkl model and testing the accuracy score
model = load_model('best_model.pkl')
from sklearn.metrics import accuracy_score
test_preds = model.predict(test)
accuracy_score(test_target, test_preds)
print(accuracy_score(test_target, test_preds))

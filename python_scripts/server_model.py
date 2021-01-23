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
import os

os.environ['KMP_DUPLICATE_LIB_OK']='True'

#loading raw data
path = 'MovementAAL/new_dataset/stream_'
sequences = list()
for i in range (1,120):
    file_path = path + str(i) + '.csv'
    df = pd.read_csv(file_path, header=0)
    values = df.values
    sequences.append(values)

#target values
targets = pd.read_csv('MovementAAL/new_dataset/MovementAAL_target.csv')
targets = targets.values[:,1]

#Loading grouping
groups = pd.read_csv('MovementAAL/newgroups/MovementAAL_DatasetGroup.csv', header=0)
groups = groups.values[:,1]

len_sequences = []
for one_seq in sequences:
    len_sequences.append(len(one_seq))


#Padding the sequence with the values in last row to max length
to_pad = 119
new_seq = []
for one_seq in sequences:
    len_one_seq = len(one_seq)
    last_val = one_seq[-1]
    n = to_pad - len_one_seq
   
    to_concat = np.repeat(one_seq[-1], n).reshape(4, n).transpose()
    new_one_seq = np.concatenate([one_seq, to_concat])
    new_seq.append(new_one_seq)
final_seq = np.stack(new_seq)

#truncate the sequence to length 60
from keras.preprocessing import sequence
seq_len = 75
final_seq=sequence.pad_sequences(final_seq, maxlen=seq_len, padding='post', dtype='float', truncating='post')

#Training data based on group 2
train = [final_seq[i] for i in range(len(groups)) if (groups[i]==2)]
#validation data based on group 1
validation = [final_seq[i] for i in range(len(groups)) if groups[i]==1]
#test data based on group 3
test = [final_seq[i] for i in range(len(groups)) if groups[i]==3]

#train target based on group 2
train_target = [targets[i] for i in range(len(groups)) if (groups[i]==2)]
#validation target based on group 1
validation_target = [targets[i] for i in range(len(groups)) if groups[i]==1]
#test target based on group 3
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
model.add(LSTM(120, input_shape=(seq_len, 4)))
model.add(Dense(1, activation='sigmoid'))
model.summary()


#loading the exported pkl model and testing the accuracy score
model = load_model('best_model.pkl')
from sklearn.metrics import accuracy_score
test_preds = model.predict_classes(test)
print(test)
print(test_preds)
print(test_target)
accuracy_score(test_target, test_preds)
print(accuracy_score(test_target, test_preds))

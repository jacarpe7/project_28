import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from os import listdir

label = "null"
filename = "output-" + label + ".txt"
f = open(filename, "w")

#loading raw data
path = 'new_model/dataset-new/Null/stream_'
cols_to_use = [0,1,2,3]
for i in range (200):
    file_path = path + str(i) + '.csv'
    # print(file_path)
    df = pd.read_csv(file_path, usecols=cols_to_use , header=0, index_col=None)
    values = df.values
    for n in range (4):
        f.write(str(values[:,n]).replace("\n",""))
        f.write("\n")

    # print(values[:,1])
    # sequences.append(values)
    # print(sequences[0][1][1])

f.close()
label = "leftswipe"
filename = "output-" + label + ".txt"
f = open(filename, "w")

path = 'new_model/dataset-new/LeftSwipe/stream_'
cols_to_use = [0,1,2,3]
for i in range (200):
    file_path = path + str(i) + '.csv'
    # print(file_path)
    df = pd.read_csv(file_path, usecols=cols_to_use , header=0, index_col=None)
    values = df.values
    for n in range (4):
        f.write(str(values[:,n]).replace("\n",""))
        f.write("\n")

f.close()
label = "rightswipe"
filename = "output-" + label + ".txt"
f = open(filename, "w")

path = 'new_model/dataset-new/RightSwipe/stream_'
cols_to_use = [0,1,2,3]
for i in range (200):
    file_path = path + str(i) + '.csv'
    # print(file_path)
    df = pd.read_csv(file_path, usecols=cols_to_use , header=0, index_col=None)
    values = df.values
    for n in range (4):
        f.write(str(values[:,n]).replace("\n",""))
        f.write("\n")

f.close()
label = "fullactivity"
filename = "output-" + label + ".txt"
f = open(filename, "w")

path = 'new_model/dataset-new/FullActivity/stream_'
cols_to_use = [0,1,2,3]
for i in range (200):
    file_path = path + str(i) + '.csv'
    # print(file_path)
    df = pd.read_csv(file_path, usecols=cols_to_use , header=0, index_col=None)
    values = df.values
    for n in range (4):
        f.write(str(values[:,n]).replace("\n",""))
        f.write("\n")

f.close()

# #target values
# targets = pd.read_csv('new_model/dataset-new/Movement_target.csv')
# targets = targets.values[:,1]

# print(targets)

# #Loading grouping
# groups = pd.read_csv('new_model/dataset-new/groups/Movement_DatasetGroup.csv', header=0)
# groups = groups.values[:,1]

# print(groups)

import pandas as pd
import numpy as np

directory = 'regular_'
# can make directories to add 'variance_'

labels = list()
labels += ['selection','swipe_left','swipe_right','swipe_up']

for label in labels:
    newfile = "output-" + label + ".txt"
    f = open(newfile, "w")
    path = directory + label + '/stream_'
    for i in range (100):
        file_path = path + str(i) + '.csv'
        # print(file_path)
        df = pd.read_csv(file_path, header=0, index_col=None)
        values = df.values
        for n in range (9):
            f.write(str(values[:,n]).replace("\n",""))
            f.write("\n")

    f.close()
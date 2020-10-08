# -*- coding: utf-8 -*-
"""
This is file demos importing a .csv file generated from Atmel
into a Pandas DataFramework data structure, and basic methods for
filtering the data.

Created on Thu Oct  8 10:22:58 2020
@author: Josh Carpenter
"""

import pandas as pd

# This reads in the CSV file located in the data folder
# the 'r' before the path address special chars in the path, including '/'T
data = pd.read_csv(r'data/sample_qt7_data.csv')

# this will select a subset of columns of needed
data2 = pd.DataFrame(data, columns = [
    'Time',
    'FrameCounter',
    'Signal0',
    'Reference0',
    'Delta0',
    'Compensation0',
    'State0',
    'Threshold0'])

# Prints all rows which have a FrameCounter value less than 37
data3 = data.loc[data['FrameCounter'] < 37]

# Prints all rows which have FrameCounter value less than 37 AND
# exlcudes the value of '511' in the Delta0 column
data4 = data.loc[(data'FrameCounter'] < 37) & () 

# prints all the various samples above
print(data)
print(data2)
print(data3)
print(data4)



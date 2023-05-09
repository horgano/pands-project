
#import csv

#with open ('irisdata.csv') as csv_file:
#    print (csv_file)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import time

# https://blog.finxter.com/how-to-convert-a-csv-to-numpy-array-in-python/#:~:text=A%20quick%20and%20efficient%20way,DataFrame%20to%20a%20NumPy%20array.
# arrange data in numpy array
df = pd.read_csv('iris.csv', header = None)
array = df.to_numpy()
#print (df)

# https://stackoverflow.com/questions/34091877/how-to-add-header-row-to-a-pandas-dataframe
titled_df = pd.read_csv('iris.csv', names = ["Sepal Length(cm)","Sepal Width(cm)","Petal Length(cm)","Petal Width(cm)","Class"])
#print (titled_df)

correlation = titled_df.corr()
print (correlation)
time.sleep(2)

mean_values = titled_df.groupby('Class').mean()
print (f'\nMean values:\n {mean_values}')
time.sleep(2)

# https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html
sepal_length_mean_full = titled_df["Sepal Length(cm)"].mean()
sepal_length_max_full = titled_df["Sepal Length(cm)"].max()
sepal_length_min_full = titled_df["Sepal Length(cm)"].min()
print (f'Overall Sepal length mean is: {sepal_length_mean_full}')
#print (sepal_length_max_full)
#print (sepal_length_min_full)

sepal_width_mean_full = titled_df["Sepal Width(cm)"].mean()
print (sepal_width_mean_full)

petal_length_mean_full = titled_df["Petal Length(cm)"].mean()
petal_width_mean_full = titled_df["Petal Width(cm)"].mean()
print (petal_length_mean_full)
print (petal_width_mean_full)

# Groups the max values by Iris type
max_values = titled_df.groupby('Class').max()
print (f'\nMax values:\n {max_values}')
time.sleep(2)

min_values = titled_df.groupby('Class').min()
print (f'\nMin values: \n{min_values}')
time.sleep(2)

standard_dev = titled_df.groupby('Class').std()
print (f'\nStd Dev: \n{standard_dev}')
time.sleep(2)

# https://www.pythontutorial.net/python-basics/python-write-text-file/
FILENAME = 'analysis.txt'

with open(FILENAME, 'w') as f:
    f.write(f'Maximum values:\n {max_values}\n')
    f.write(f'\nMean values:\n {mean_values}\n')
    f.write(f'\nOverall Sepal length mean is: {round(sepal_length_mean_full, 2)}\n')
    f.write(f'\nMin values: \n{min_values}\n')
    f.write(f'\nStd Dev: \n{standard_dev}\n')
    print (f'\nMax values:\n {max_values}')
time.sleep(2)

print (f'\nMin values: \n{min_values}')
time.sleep(2)

print (f'\nStd Dev: \n{standard_dev}')
time.sleep(2)
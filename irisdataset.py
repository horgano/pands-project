
#import csv

#with open ('irisdata.csv') as csv_file:
#    print (csv_file)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# https://blog.finxter.com/how-to-convert-a-csv-to-numpy-array-in-python/#:~:text=A%20quick%20and%20efficient%20way,DataFrame%20to%20a%20NumPy%20array.
# arrange data in numpy array
df = pd.read_csv('iris.csv', header = None)
array = df.to_numpy()
#print (df)

# https://stackoverflow.com/questions/34091877/how-to-add-header-row-to-a-pandas-dataframe
titled_df = pd.read_csv('iris.csv', names = ["Sepal Length(cm)","Sepal Width(cm)","Petal Length(cm)","Petal Width(cm)","Class"])
print (titled_df)

correlation = titled_df.corr()
print (correlation)

sepal_length_mean_full = titled_df["Sepal Length(cm)"].mean()
sepal_length_max_full = titled_df["Sepal Length(cm)"].max()
sepal_length_min_full = titled_df["Sepal Length(cm)"].min()
print (f'Sepal length mean is: {sepal_length_mean_full}')
print (sepal_length_max_full)
print (sepal_length_min_full)
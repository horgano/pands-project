
import numpy as np
import pandas as pd

# https://blog.finxter.com/how-to-convert-a-csv-to-numpy-array-in-python/#:~:text=A%20quick%20and%20efficient%20way,DataFrame%20to%20a%20NumPy%20array.
# arrange data in numpy array
df = pd.read_csv('iris.csv', header = None)
array = df.to_numpy()

iris_setosa = array[0:50]
iris_versicolor = array[50:100]
iris_virginica = array[100:150]

number = 0

print (iris_setosa)
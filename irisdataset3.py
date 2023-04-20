import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import time
from irisdataset2.py import *


# https://blog.finxter.com/how-to-convert-a-csv-to-numpy-array-in-python/#:~:text=A%20quick%20and%20efficient%20way,DataFrame%20to%20a%20NumPy%20array.
# arrange data in numpy array
df = pd.read_csv('iris.csv', header = None)
array = df.to_numpy()

# separating the data by their Iris type
iris_setosa = array[0:50] # includes 1st to 49th column
iris_versicolor = array[50:100]
iris_virginica = array[100:150]

sepal_length = array[:,0]
sepal_width = array[:,1]
petal_length = array[:,2]
petal_width = array[:,3]
#print (f'Sepal Length: {sepal_length}')
#print (sepal_width)
#print (petal_length)
#print (petal_width)

plt.hist (sepal_length)
plt.title(' Sepal Length (cm)')
plt.axhline(y=sepal_length_mean_full, color = 'red')
plt.show()

plt.hist (sepal_width)
plt.title('Sepal_Width (cm)')
plt.show()

plt.hist (petal_length)
plt.title('Petal Length (cm)')
plt.show()

plt.hist (petal_width)
plt.title('Petal Width (cm)')
plt.show()

# all lengths in cm
# arrays of all data in 1st column Petal Length, 2nd column Petal Width,
# 3rd column Sepal Length, and 4th Sepal Width
iris_setosa_sepal_length = iris_setosa[:,0]
iris_setosa_sepal_width = iris_setosa[:,1]
iris_setosa_petal_lenght = iris_setosa[:,2]
iris_setosa_petal_width = iris_setosa[:,3]

iris_versicolor_sepal_length = iris_versicolor[:,0]
iris_versicolor_sepal_width = iris_versicolor[:,1]
iris_versicolor_petal_lenght = iris_versicolor[:,2]
iris_versicolor_petal_width = iris_versicolor[:,3]

iris_virginica_sepal_length = iris_virginica[:,0]
iris_virginica_sepal_width = iris_virginica[:,1]
iris_virginica_petal_lenght = iris_virginica[:,2]
iris_virginica_petal_width = iris_virginica[:,3]


plt.hist (iris_setosa_sepal_length)
plt.title('Iris Setosa Sepal Length (cm)')
#plt.show()

plt.hist (iris_versicolor_sepal_length, color = 'red')
plt.title('Iris Versicolor Sepal Length (cm)')
#plt.show()

plt.hist (iris_virginica_sepal_length, color = 'green')
plt.title('Iris Virginica Sepal Length (cm)')
#plt.show()
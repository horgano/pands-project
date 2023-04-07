# test.py
# my own testing to ensure each array had the correct amount of data

import numpy as np
import pandas as pd

df = pd.read_csv('iris.csv', header = None)
array = df.to_numpy()

iris_setosa = array[0:50]
iris_versicolor = array[50:100]
iris_virginica = array[100:150]

# printing and counting items in iris_setosa array
number = 0

for item in iris_setosa:
    number += 1
    
print (iris_setosa)
print (number)

# printing and counting items in iris_versicolor array
number2 = 0

for item in iris_versicolor:
    number2 += 1
    
print (iris_versicolor)
print (number)

# printing and counting items in iris_versicolor array
number3 = 0

for item in iris_virginica:
    number3 += 1
    
print (iris_virginica)
print (number)




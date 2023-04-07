
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# https://blog.finxter.com/how-to-convert-a-csv-to-numpy-array-in-python/#:~:text=A%20quick%20and%20efficient%20way,DataFrame%20to%20a%20NumPy%20array.
# arrange data in numpy array
df = pd.read_csv('iris.csv', header = None)
array = df.to_numpy()

iris_setosa = array[0:50]
iris_versicolor = array[50:100]
iris_virginica = array[100:150]

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

#print (iris_setosa_sepal_length)
#print (iris_setosa_sepal_width)
#print (iris_setosa_petal_lenght)
#print (iris_setosa_petal_width)

plt.scatter (iris_setosa_sepal_length,iris_setosa_sepal_width, label = 'Setosa')
plt.scatter (iris_versicolor_sepal_length,iris_versicolor_sepal_width, color = 'red', label = 'Versicolor')
plt.scatter (iris_virginica_sepal_length,iris_virginica_sepal_width, color = 'green', label = 'Virginica')
plt.title('Sepal Length x Sepal Width')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.legend()
plt.show()


plt.scatter (iris_setosa_petal_lenght, iris_setosa_petal_width, label = 'Setosa')
plt.scatter (iris_versicolor_petal_lenght, iris_versicolor_petal_width, color = 'red', label = 'Versicolor')
plt.scatter (iris_virginica_petal_lenght, iris_virginica_petal_width, color = 'green', label = 'Virginica')
plt.title('Petal Length x Petal Width')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.legend()
plt.show()

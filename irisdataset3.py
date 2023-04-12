import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# https://blog.finxter.com/how-to-convert-a-csv-to-numpy-array-in-python/#:~:text=A%20quick%20and%20efficient%20way,DataFrame%20to%20a%20NumPy%20array.
# arrange data in numpy array
df = pd.read_csv('iris.csv', header = None)
array = df.to_numpy()

# separating the data by their Iris type
iris_setosa = array[0:50] # includes 1st to 49th column
iris_versicolor = array[50:100]
iris_virginica = array[100:150]

# all lengths in cm
# arrayof all date in 1st column Petal Length
iris_setosa_sepal_length = iris_setosa[:,0]
# arrayof all date in 2nd column Petal Width
iris_setosa_sepal_width = iris_setosa[:,1]
# arrayof all date in 3rd column Sepal Length
iris_setosa_petal_lenght = iris_setosa[:,2]
# arrayof all date in 4th column Sepal Width
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
plt.show()

plt.hist (iris_versicolor_sepal_length, color = 'red')
plt.title('Iris Versicolor Sepal Length (cm)')
plt.show()

plt.hist (iris_virginica_sepal_length, color = 'green')
plt.title('Iris Virginica Sepal Length (cm)')
plt.show()
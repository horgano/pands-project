
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import time


# https://blog.finxter.com/how-to-convert-a-csv-to-numpy-array-in-python/#:~:text=A%20quick%20and%20efficient%20way,DataFrame%20to%20a%20NumPy%20array.
# arrange data in dataframe after reading from csv file without headings
# and arrange that data into an array
df = pd.read_csv('iris.csv', header = None)
array = df.to_numpy()

# https://stackoverflow.com/questions/34091877/how-to-add-header-row-to-a-pandas-dataframe
# add headers to that csv file and make new data frame
titled_df = pd.read_csv('iris.csv', names = ["Sepal Length(cm)","Sepal Width(cm)","Petal Length(cm)","Petal Width(cm)","Class"])

correlation = titled_df.corr()
print (f'Correlation data for Iris Data Set:\n{correlation}')
time.sleep(2)

# https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html
sepal_length_mean_full = titled_df["Sepal Length(cm)"].mean()
sepal_length_max_full = titled_df["Sepal Length(cm)"].max()
sepal_length_min_full = titled_df["Sepal Length(cm)"].min()
#print (f'Sepal length mean is: {sepal_length_mean_full}')
#print (sepal_length_max_full)
#print (sepal_length_min_full)

# separating the data by their Iris type
iris_setosa = array[0:50] # includes 1st to 49th column
iris_versicolor = array[50:100]
iris_virginica = array[100:150]

# all lengths in cm
# arrayof all date in 1st column Petal Length, 2nd column Petal Width,
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

#print (iris_setosa_sepal_length)
#print (iris_setosa_sepal_width)
#print (iris_setosa_petal_lenght)
#print (iris_setosa_petal_width)

plt.scatter (iris_setosa_sepal_length,iris_setosa_sepal_width, label = 'Setosa')
plt.scatter (iris_versicolor_sepal_length,iris_versicolor_sepal_width, color = 'red', label = 'Versicolor')
plt.scatter (iris_virginica_sepal_length,iris_virginica_sepal_width, color = 'green', label = 'Virginica')
plt.title('Sepal Length x Sepal Width')
plt.xlabel('Sepal Length cm')
plt.ylabel('Sepal Width cm')
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

# https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html
sepal_length_mean_full = titled_df["Sepal Length(cm)"].mean()
sepal_length_max_full = titled_df["Sepal Length(cm)"].max()
sepal_length_min_full = titled_df["Sepal Length(cm)"].min()
#print (f'Sepal length mean is: {sepal_length_mean_full}')
#print (sepal_length_max_full)
#print (sepal_length_min_full)

sepal_width_mean_full = titled_df["Sepal Width(cm)"].mean()
sepal_width_max_full = titled_df["Sepal Width(cm)"].max()
sepal_width_min_full = titled_df["Sepal Width(cm)"].min()

petal_length_mean_full = titled_df["Petal Length(cm)"].mean()
petal_length_max_full = titled_df["Petal Length(cm)"].max()
petal_length_min_full = titled_df["Petal Length(cm)"].min()

petal_width_mean_full = titled_df["Petal Width(cm)"].mean()
petal_width_max_full = titled_df["Petal Width(cm)"].max()
petal_width_min_full = titled_df["Petal Width(cm)"].min()

plt.hist (sepal_length)
plt.title(' Sepal Length (cm)', loc = 'left')
# add horizontal line at mean value of  https://www.statology.org/matplotlib-average-line/
# https://stackoverflow.com/questions/16930328/vertical-horizontal-lines-in-matplotlib
plt.axvline(x=sepal_length_mean_full, linestyle = 'dotted', color = 'red', label = 'Average' )
plt.savefig('Sepal_Length_Histogram.png')
plt.show()

plt.hist (sepal_width)
plt.title('Sepal Width (cm)', loc = 'left')
plt.axvline(x=sepal_width_mean_full, linestyle = 'dotted', color = 'red', label = 'Average' )
plt.savefig('Sepal_Width_Histogram.png')
plt.show()


plt.hist (petal_length)
plt.title('Petal Length (cm)', loc = 'left')
plt.axvline(x=petal_length_mean_full, linestyle = 'dotted', color = 'red', label = 'Average' )
plt.savefig('Petal_Length_Histogram.png')
plt.show()


plt.hist (petal_width)
plt.title('Petal Width (cm)', loc = 'left')
plt.axvline(x=petal_width_mean_full, linestyle = 'dotted', color = 'red', label = 'Average' )
plt.savefig('Petal_Width_Histogram.png')
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
plt.axvline(x=sepal_length_mean_full, linestyle = 'dotted', color = 'red', label = 'Average' )
plt.show()

plt.hist (iris_versicolor_sepal_length, color = 'red')
plt.title('Iris Versicolor Sepal Length (cm)')
plt.axvline(x=sepal_length_mean_full, linestyle = 'dotted', color = 'red', label = 'Average' )
plt.show()

plt.hist (iris_virginica_sepal_length, color = 'green')
plt.title('Iris Virginica Sepal Length (cm)')
plt.axvline(x=sepal_length_mean_full, linestyle = 'dotted', color = 'red', label = 'Average' )
plt.show()

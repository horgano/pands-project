# IRIS DATA SET OVERVIEW

- The Iris Data set or Fisher's Iris Data set is a multivariate data set introduce by British statitician, eugenicist, and biologist Ronald Fisher in 1936.

- It is a historical dataset and was one of the first of multivariate data analysis. 

- The dataset consists 50 samples each of (3 classes):
- - Iris Setosa
- - Iris Virginica
- - Iris Versicolor

- Four features were measured of each:
- - Sepal length
- - Sepal width
- - Petal length
- - Petal width

- Based on the combination of these 4 features, Fisher developed a linear discriminant model to distinguish the species from each other.

# _Instructions:_

analysis.py is code written in python programming language. Simply run analysis.py in your terminal with the command 'python analysis.py'

The program takes input from csv file iris.csv. This csv file has no headings so one of my first tasks was to add the Sepal length, Sepal width, Petal length, Petal width headings to the file.

Also firstly, I split the info from the csv file into arrays so that I could present the info in graphs and do analysis of each class array and variable arrays.

## _Scatterplots:_
- 1  Sepal length x Sepal width: 3 Classes
- 2  Petal length x Petal width: 3 Classes

## _Histograms (including average line):_
- 1 Sepal length (overall)
- 2 Sepal Width (overall)
- 3 Petal length (overall)
- 4 Petal Width (overall)
- 5 Sepal length (Setosa)
- 6 Sepal Width (Setosa)
- 7 Petal length (Setosa)
- 8 Petal Width (Setosa)
- 9 Sepal length (Versicolor)
- 10 Sepal Width (Versicolor)
- 11 Petal length (Versicolor)
- 12 Petal Width (Versicolor)
- 13 Sepal length (Virginica)
- 14 Sepal Width (Virginica)
- 15 Petal length (Virginica)
- 16 Petal Width (Virginica)

Lastly, analysis in the form of Iris data mean, min & max values as well as correlation an standard deviation values are out put to text file analysis.txt

# Summary of Data Analysis on Iris Data Set

### A.Scatter: Sepal length x Sepal Width:
 Here we see that the Setosa Sepal is clearly distinguished and stand out from Versicolor and Virginica. Its shorter and wider sepals makes it stand alone vs the others. There is alot of over lap between Versicolor and Virginica, with the formers shorter Sepal length making it more recognisable from the latters longer Sepals. Both their widths are similar.

### B.Scatter: Petal length x Petal Width:
If the first Scatter was in any doubt of the individualism of the Iris Setosa this scatter plot clearly shows how stand out the Setosa is asits Petal length and width are miniscule vs the others. And clearly so. In this scatter there is more clear divide between the 3. Setosa has smallest length and width by far, and with a big gap to Versicolor in the middle with length and width of its Petals. Witonly a tiny bit of over lap we have a clear winner for Petal length and width with Virginica.

### Histogram 1-4:
Whilst the overall Sepal length and Sepal width give us more of a standard distributon of the overall set, they are nothing like the distribution of Petal length and Petal width whch are totally skewed by the Setosa dimensions.

### Histogram 5-8:
All 4 graphs show a standard distribution fomr Setosa but all well below the average of the overall

### Histogram 9-12:
Versicolors data is a mix of above and below averages

### Histogram 13-16
Virginica is cleary well above average distributin for Petal dimensions

### analysis.txt:
The outstanding info from Mean values is not only the Setosa with its extremely small Petals, but also the fact that there is also a massive difference between its length and width. In contrast its Sepal width is above average having a higher mean than the other 2. This is the only factor that its has the larger value.

Versicolor and Virginica have more of a comparable relationship between Sepal length and width but there is a clearer difference in the overall size of their Petals with Virginica having the larger, while its mean for Sepal is only slightly larger.

Maximum values: Sepal length and Petal lengths show the bigger differences between Classes. On both types of width the max values are more similar.

Min Values: For the smaller values it is Petal length that we see the big difference. Also Setosa is an outlier in Petal width. The other 2 variables there is little difference.

Standard Deviation: This is the calculation of how a set is distributed in comparison to its mean.
This value for Sepal width is almost identical for each Class.
Virginica has the greatest for Sepal length.
While Versicolor and Virginica have similar for Petal length Setosas std dev is minimal.
For Petal width the deviatio for each Class is low.

Correlation: 
- 0 = having no correlation between 2 variables.
- 1 = extremely positive (1 increases, the other increases)
- -1 = extremely negative (1 increases, the otger decreases)
 

# _Interesting Analyses:_

- 1: British Statistician Ronald Fishers originally introduced by the Iris Data Set in his 1936 Paper "The use of multiple measurements in taxonomic problems". He used the dataset to demonstrate the effectiveness of Linear Discriminant Analysis for classifying the iris' based on the 4 Classes.
- 2: Sometimes called the Anderson dataset as DR Edgar Anderson is credited with collecting the majority of the data for the set.
- 3: In a 1953 paper Ronald Fisher and Michael Powell demonstrated the significant variation within each species of Iris but also that the differences were significant.
- 4: Robert Sokal and James Rolf in their 1956 book used the dataset to illustrate hierarchical clustering techniques. 
- 5: Modernly used in machine learning
- https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5

# REFERENCES:
 https://blog.finxter.com/how-to-convert-a-csv-to-numpy-array-in-python/#:~:text=A%20quick%20and%20efficient%20way,DataFrame%20to%20a%20NumPy%20array.

 https://stackoverflow.com/questions/34091877/how-to-add-header-row-to-a-pandas-dataframe

 https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html

 https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html

 https://www.statology.org/matplotlib-average-line/

 https://stackoverflow.com/questions/16930328/vertical-horizontal-lines-in-matplotlib

 https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html

 https://www.pythontutorial.net/python-basics/python-write-text-file/


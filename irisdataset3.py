
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# https://www.geeksforgeeks.org/visualize-data-from-csv-file-in-python/

x = []
y = []

with open('iris.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')

    for row in plots:
        x.append(row[0])
print (x)
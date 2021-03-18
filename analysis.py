# This program is a data analysis on the Iris dataset for programming & scripting module
# Author: Katie Mc Donald

# Importing libaries
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# Reading the Iris CSV file into a pandas DataFrame
df = pd.read_csv('iris.csv')
# Adding column titles to the data
df.columns = ['Sepal Lenght', 'Sepal Width', 'Petal Lenght', 'Petal Width', 'Species']
print(df)


#from sklearn.datasets import load_iris
#iris = load_iris()
#print(iris.DESCR)
#def load_data():
   # iris = pd.read_csv('iris.cvs')
    #iris.columns = ['Sepal Lenght', 'Sepal Width', 'Petal Lenght', 'Petal Width', 'Species']
    #return iris


#print(load_data)
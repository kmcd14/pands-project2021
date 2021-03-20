# This program is a data analysis on the Iris dataset for programming & scripting module
# Author: Katie Mc Donald

# Importing libaries
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import sys


# Reading the Iris CSV file into a pandas DataFrame
# Without the header parameter column names are inferred from the first file row
# The Names parameter adds column titles 
df = pd.read_csv('iris.csv', header=None, names=['Sepal Lenght(cm)', 'Sepal Width(cm)', 'Petal Lenght(cm)', 'Petal Width(cm)', 'Species']) 


# Creating text file called Comparison to print output results of comparing the species
sys.stdout = open("Comparison.txt", "w", newline='\r\n') # Adding a return and newline between each question

df.shape # Shape should return 150 rows x 5 columns
# Count of how many of each species
print(df['Species'].value_counts())

# Cleaning Data 
null_values = df.isnull().sum() # Checking for null values
print(null_values)
d = df.duplicated().sum() # Total no of duplicates in the dataset
f= df[df.duplicated()] #This shows the actual duplicate rows
print(d, f)

#Finding the average lenght and width of Sepal and Petal for each species
mean_values = df.groupby('Species').mean()
print('\t\t\t\t\t\t\tAVERAGE VALUES\n',mean_values)

df.info()
df.describe()

print(df.corr())
sns.heatmap(df.corr(), cmap='coolwarm', annot = True)
#closing text file
sys.stdout.close()




# Creating text file called Comparison to print output results of comparing the species
sys.stdout = open("Iris-setosa txt", "w", newline='\r\n') # Adding a return and newline between each question
setosadf = df[df['Species'] == 'Iris-setosa']
print(setosadf.value_counts())
#closing text file
sys.stdout.close()




# Creating text file called Iris-Versicolor to print output results of comparing the species
sys.stdout = open("Iris-versicolor txt", "w", newline='\r\n') # Adding a return and newline between each question
versicolordf = df[df['Species'] == 'Iris-versicolor']
print(versicolordf.value_counts())
#closing text file
sys.stdout.close()




# Creating text file called Iris-virginica to print output results of comparing the species
sys.stdout = open("Iris-virginica txt", "w", newline='\r\n') # Adding a return and newline between each question
virginicadf = df[df['Species'] == 'Iris-virginica']
print(virginicadf.count())
#closing text file
sys.stdout.close()
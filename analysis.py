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

# Creating text file called Iris Analysis to print output results of comparing the species
sys.stdout = open("Iris Analysis", "w", newline='\n') # Adding a return and newline between each question
print('******Iris Dataset Analysis********\n______________________________________________________________________________')
# An overview of the entire dataframe
print(df.info(),'\n______________________________________________________________________________')
# Returns the first 5 rows. Allows us to see a overview of the data
print('First 5 rows of data:\n',df.head(),'\n______________________________________________________________________________')
# Cleaning Data 
print('Checking for NULL values:\n',df.isnull().sum()) # Checking for null values
print('\rNumber of duplicates:\t', df.duplicated().sum()) # Total no of duplicates in the dataset
#This shows the actual duplicate rows
print('\rDuplicate rows:\n\t',df[df.duplicated()],'\n______________________________________________________________________________') 
# Count of how many of each species
print('Count of each unique species:\r',df['Species'].value_counts(),'\n______________________________________________________________________________')
# An summary of stats for each variable(count, mean, min, max, standard deviation, )
print('Stat Summary: \r')
print(df.describe(),'\n______________________________________________________________________________')

# Diving data into seprate dataframes to futher investigate each species by slicing
setosadf=df.loc[df["Species"]=="Iris-setosa"] # .loc gets the rows in Species == Iris-setosa
versicolordfa=df.loc[df["Species"]=="Iris-virginica"] # .loc gets the rows in Species == Iris-virginica
virginicadf=df.loc[df["Species"]=="Iris-versicolor"] # .loc gets the rows in Species == Iris-versicolor

# Creating a histogram for each variable 
sns.FacetGrid(df,hue='Species',height=5).map(sns.histplot,'Petal Lenght(cm)').add_legend().set_titles('Petal Lenght(cm)')
sns.FacetGrid(df,hue='Species',height=5).map(sns.histplot,'Petal Width(cm)').add_legend().set_titles('Petal Width(cm)')
sns.FacetGrid(df,hue='Species',height=5).map(sns.histplot,'Sepal Lenght(cm)').add_legend().set_titles('Sepal Lenght(cm)')
sns.FacetGrid(df,hue='Species',height=5).map(sns.histplot,'Sepal Width(cm)').add_legend().set_titles('Sepal Width(cm)')
plt.show()

# Closing Iris Analysis File
sys.stdout.close()

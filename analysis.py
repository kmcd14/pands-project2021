# This python script is a data analysis on the Iris dataset for programming & scripting module
# The output of this script is found in the text file names 'Iris Analysis'
# Markdown of the analysis is found in README.md
# All plots can be found in the image folder
# Author: Katie Mc Donald

# Importing libaries
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import sys

## LOADING DATA ##

# Reading the Iris CSV file into a pandas DataFrame
# Without the header parameter column names are inferred from the first file row
# The Names parameter adds column titles 
df = pd.read_csv('iris.csv', header=None, names=['Sepal Lenght(cm)', 'Sepal Width(cm)', 'Petal Lenght(cm)', 'Petal Width(cm)', 'Species']) 

# Diving data into separate dataframes using slicing
setosadf=df.loc[df["Species"]=="Iris-setosa"] # .loc gets the rows in Species == Iris-setosa
versicolordfa=df.loc[df["Species"]=="Iris-virginica"] # .loc gets the rows in Species == Iris-virginica
virginicadf=df.loc[df["Species"]=="Iris-versicolor"] # .loc gets the rows in Species == Iris-versicolor


## CREATING TEXT FILE ##

# Creating a text file called Iris Analysis to print output results of comparing the species
sys.stdout = open("Iris Analysis", "w", newline='\n') # Using 'w' for write mode. Adding a newline between each print statement 
print('******Iris Dataset Analysis********\n______________________________________________________________________________')


## DATA SUMMARY ##

# An overview of the dataframe. Shows the datatype, columns, count,  if null
print(df.info(),'\n______________________________________________________________________________')

# Returns the first 5 rows. Allows us to see a overview of the data
print('First 5 rows of data:\n')
print(df.head(),'\n______________________________________________________________________________')

# Cleaning Data 
print('Checking for NULL values:\n')
print(df.isnull().sum()) # Checking for null values
print('\rNumber of duplicates:\t', df.duplicated().sum()) # Total number of duplicates in the dataset
print('\rDuplicate rows:\n\t') 
# This shows the actual duplicate rows
print(df[df.duplicated()],'\n______________________________________________________________________________') 

# Returns a count of how many of each species
print('Count of each unique species:\r')
print(df['Species'].value_counts(),'\n______________________________________________________________________________')

# A summary of stats for each variable(count, mean, min, max, standard deviation, percentile )
print('Stat Summary: \r')
print(df.describe(),'\n______________________________________________________________________________')

# Grouping species by mean, max and min values To futher look at this data
mean_values = df.groupby('Species').mean() # Mean
print('Mean Values: \r\n', mean_values,'\n______________________________________________________________________________')
max_val = df.groupby('Species').max() # Max
print('Max Values: \r\n', max_val,'\n______________________________________________________________________________')
min_values = df.groupby('Species').min() #Min
print('Min Values: \r\n', min_values,'\n______________________________________________________________________________')

# Find the pairwise correlation of columns in the dataframe.
# Using the whole dataframe
print('\rCorrelations:\n\t',df.corr(),'\n______________________________________________________________________________') 
# Just iris-setosa dataframe
print('\riris-setosa:\n\t',setosadf.corr(),'\n______________________________________________________________________________')
# Just iris-veriscolour dataframe
print('\riris-versicolor:\n\t',versicolordfa.corr(),'\n______________________________________________________________________________')
# Just iris-virginica dataframe
print('\riris-virginica:\n\t',virginicadf.corr(),'\n______________________________________________________________________________')


## VISUALISING THE DATA ##

# Creating a countplot to show the number of instances of each species of iris
sns.set_theme(style="darkgrid") # Styling the grid
# Plotting on the X axes so it's a vertical countplot, using the df dataframe, choosing the colour palette
sns.countplot(x="Species", data=df, palette="Set3")
plt.title('Number of Occurances', color='indigo') # Adding a title 
plt.show() # Showing the plot




# Creating a histogram for each variable. 
# (dataframe used, the variable, variable that will produce points with different colors (species), colour palette, kde turned off) 
sns.displot(df, x='Petal Lenght(cm)', hue='Species', palette='Set3', kde=False)
sns.displot(df, x='Petal Width(cm)', hue='Species', palette='Set3', kde=False)
sns.displot(df, x='Sepal Lenght(cm)', hue='Species', palette='Set3', kde=False)
sns.displot(df, x='Sepal Width(cm)', hue='Species', palette='Set3', kde=False)
sns.set_theme(style="darkgrid") # Styling the grid
sns.set_style('ticks') # Adding ticks to axis
plt.show() # Showing the plot


# Creating a scatterplot for each pair of variables using seaborn
# (plotting variables on x and y axis, dataframe, variable that will produce points with different colors (species), colour palette)
sns.scatterplot(x = 'Sepal Width(cm)', y = 'Sepal Lenght(cm)',data=df, hue='Species', palette='plasma')
plt.title('Sepal Variables') # Adding a title
sns.set(style='darkgrid') # Grid style
plt.show() # Showing plot
# (plotting variables on x and y axis, dataframe, variable that will produce points with different colors (species), colour palette)
sns.scatterplot(x = 'Petal Width(cm)', y = 'Petal Lenght(cm)',data=df, hue='Species',palette='plasma')
plt.title('Petal Variables') # Adding a title
sns.set(style='darkgrid') # Grid style
plt.show() # Showing plot


# Boxplot
# (dataframe, colour palette, horizontal orientation)
sns.boxplot(data=df, palette='Set3', orient='h')
plt.title('Boxplot') # Adding a title
sns.set(style='darkgrid') # Grid style
plt.show() # Show plot


# Pairplot
# (dataframe, variable that will produce points with different colors (species), colour palette)
sns.pairplot(df, hue='Species', palette='plasma')
plt.show() # Showing plot


# Heatmap representation of the correlations 
# (correlation dataframe, colour map, line colour and width add lines to divide cells & their colour, annot shows the data value in each cell)
sns.heatmap(df.corr(), cmap='Set3',linecolor='white',linewidths=1, annot= True)
plt.title('Heat Map') # Adding title
plt.show() # Show plot


# Clustermap - another look at correlations and their relationships
# (cluster dataframe, colourmap)
cluster = sns.clustermap(df.corr(), cmap='plasma')
plt.show() # Showing plot

# Andrews Curve
# (dataframe, column containing the class name, colourmap)
andrews_curve = pd.plotting.andrews_curves(df,"Species",colormap='magma')
plt.title('Andrews Curve') # Adding title
plt.grid( color='black', lw=0.15, ls="--") # Styling grid
plt.show() # Showing plot

# Closing Iris Analysis File
sys.stdout.close()

# This python script is a data analysis on the Iris dataset for programming & scripting module
# The output of this script is found in the text file names 'Iris Analysis'
# Markdown of the analysis is found in README.md
# All plots can be found in the Plots folder
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
versicolordf=df.loc[df["Species"]=="Iris-virginica"] # .loc gets the rows in Species == Iris-virginica
virginicadf=df.loc[df["Species"]=="Iris-versicolor"] # .loc gets the rows in Species == Iris-versicolor


## CREATING TEXT FILE ##

# Creating a text file called Iris Analysis to print output results of comparing the species
sys.stdout = open("Iris Analysis", "w", newline='\n') # Using 'w' for write mode. Adding a newline between each print statement 
print('******Iris Dataset Analysis********\n______________________________________________________________________________')


## DATA SUMMARY ##

# An overview of the dataframe. Shows the datatype, columns, count,  if null
print(df.info(),'\n______________________________________________________________________________')

# Returns the first 5 rows by default. Allows us to see a overview of the data
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

# A summary of stats for each indivdual species(count, mean, min, max, standard deviation, percentile )
print('iris-setosa Summary: \r')
print(setosadf.describe(),'\n______________________________________________________________________________')

print('iris-versicolor Summary: \r')
print(versicolordf.describe(),'\n______________________________________________________________________________')

print('iris-virgina Summary: \r')
print(virginicadf.describe(),'\n______________________________________________________________________________')


# Creating a Pivot Table for Mean
pivot_mean = df.pivot_table(index='Species', values=['Sepal Lenght(cm)', 'Sepal Width(cm)', 'Petal Lenght(cm)', 'Petal Width(cm)'], aggfunc=np.mean)
print('Pivot Table Mean Values: \r\n', pivot_mean,'\n______________________________________________________________________________')
# Creating a Pivot Table for Max
pivot_max = df.pivot_table(index='Species', values=['Sepal Lenght(cm)', 'Sepal Width(cm)', 'Petal Lenght(cm)', 'Petal Width(cm)'], aggfunc=np.max)
print('Pivot Table Max Values: \r\n', pivot_max,'\n______________________________________________________________________________')
#Creating a Pivot Table for Min
pivot_min = df.pivot_table(index='Species', values=['Sepal Lenght(cm)', 'Sepal Width(cm)', 'Petal Lenght(cm)', 'Petal Width(cm)'], aggfunc=np.min)
print('Pivot Table Min Values: \r\n', pivot_min,'\n______________________________________________________________________________')


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
print('\riris-versicolor:\n\t',versicolordf.corr(),'\n______________________________________________________________________________')
# Just iris-virginica dataframe
print('\riris-virginica:\n\t',virginicadf.corr(),'\n______________________________________________________________________________')



## VISUALISING THE DATA ##

# Creating a countplot to show the number of instances of each species of iris
sns.set_theme(style="darkgrid") # Styling the grid
# Plotting on the X axes so it's a vertical countplot, using the df dataframe, choosing the colour palette
sns.countplot(x="Species", data=df, palette="Set3")
plt.title('Number of Occurances', color='indigo') # Adding a title 
plt.savefig('Plots\\Countplot') # Saving plot to Plots directory
plt.close() # Closes figure 



# Creating a histogram for each variable. 
# (dataframe used, the variable, variable that will produce points with different colors (species), colour palette, kde turned off) 
sns.displot(df, x='Petal Lenght(cm)', hue='Species', palette='Set3', kde=False)
sns.displot(df, x='Petal Width(cm)', hue='Species', palette='Set3', kde=False)
sns.displot(df, x='Sepal Lenght(cm)', hue='Species', palette='Set3', kde=False)
sns.displot(df, x='Sepal Width(cm)', hue='Species', palette='Set3', kde=False)
sns.set_theme(style="darkgrid") # Styling the grid
sns.set_style('ticks') # Adding ticks to axis
plt.savefig('Plots\\Displot') # Saving plot to Plot directory
plt.clf() # Clears figure with all its axes, but leaves the window opened, such that it may be reused for other plots. Plot's merged if close() was used.


# Creating a scatterplot for each pair of variables using seaborn
plt.figure(figsize=(10,10)) # Setting fig size
# (plotting variables on x and y axis, dataframe, variable that will produce points with different colors (species), colour palette)
sns.scatterplot(x = 'Sepal Width(cm)', y = 'Sepal Lenght(cm)',data=df, hue='Species', palette='plasma')
plt.title('Sepal Variables') # Adding a title
sns.set(style='darkgrid') # Grid style
plt.savefig('Plots\\Scatterplot Sepal Variables') # Save plot to Plots directory
plt.clf() # Clears figure with all its axes, but leaves the window opened, such that it may be reused for other plots.

plt.figure(figsize=(10,10)) # Setting fig size
# (plotting variables on x and y axis, dataframe, variable that will produce points with different colors (species), colour palette)
sns.scatterplot(x = 'Petal Width(cm)', y = 'Petal Lenght(cm)',data=df, hue='Species',palette='plasma')
plt.title('Petal Variables') # Adding a title
sns.set(style='darkgrid') # Grid style
plt.savefig('Plots\\Scatterplot Petal Variables') # Saving plot to Plots directory
plt.clf() # Clears figure with all its axes, but leaves the window opened, such that it may be reused for other plots. Plot's merged if close() was used.

# Boxplot
plt.figure(figsize=(15,10)) # Setting fig size
# (dataframe, colour palette, horizontal orientation)
sns.boxplot(data=df, palette='Set3', orient='h')
plt.title('Boxplot') # Adding a title
sns.set(style='darkgrid') # Grid style
plt.savefig('Plots\\Boxplot') # Save plot to Plots directory
plt.clf() # Clears figure with all its axes, but leaves the window opened, such that it may be reused for other plots. Plot's merged if close() was used.

# Pairplot
# (dataframe, variable that will produce points with different colors (species), colour palette)
sns.pairplot(df, hue='Species', palette='plasma')
plt.savefig('Plots\\Pairplot') # Save plot to Plots directory
plt.close() # Closes figure 


# Parallel Coordinates
from pandas.plotting import parallel_coordinates # Importing from pandas built in data visualisation tools
# (dataframe, column containing the class name)
parallel_coordinates(frame=df, class_column="Species")
plt.title('Parallel Coordinates') # Adding a title
plt.savefig('Plots\\Parallel Coordinates') # Save plot to Plots directory
plt.close() # Closes figure 


# Andrews Curve
plt.figure(figsize=(15,10)) # Setting fig size
# (dataframe, column containing the class name, colourmap)
andrews_curve = pd.plotting.andrews_curves(df,"Species",colormap='magma')
plt.title('Andrews Curve') # Adding title
plt.grid( color='black', lw=0.15, ls="--") # Styling grid
plt.savefig('Plots\\Andrews Curve') # Save plot to Plots directory
plt.close() # Closes figure 

# Heatmap representation of the correlations 
# (correlation dataframe, colour map, line colour and width add lines to divide cells & their colour, annot shows the data value in each cell)
sns.heatmap(df.corr(), cmap='Set3',linecolor='white',linewidths=1, annot= True)
plt.title('Heat Map') # Adding title
plt.savefig('Plots\\Heatmap') # Save plot to Plots directory
plt.close() # Closes figure 

# Clustermap - another look at correlations and their relationships
# (correlation dataframe, colour map, line colour and width add lines to divide cells & their colour, annot shows the data value in each cell)
cluster = sns.clustermap(df.corr(), cmap='Set3', linecolor='white',linewidths=0.5, annot=True)
plt.savefig('Plots\\Clustermap') # Save plot to Plots directory
plt.close() # Closes figure 

# Closing Iris Analysis File
sys.stdout.close()

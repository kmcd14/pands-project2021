<br>
<h1><b><u> pands-project2021</u></b></h1>



<br>
<h3 style=color:#DDA0DD><b><u>Table of Contents</b></u></h3></summary>
  <ol>
    <li><a href="#Overview"> Overview</a></li>
    <li><a href="#iris">What Is the Iris DataSet?</a></li>
    <li><a href="#modules used">Modules Used</a></li>
    <li><a href="#results">Results</a></li>
    <li><a href="#conclusion">Conclusion</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
    <li><a href="#References">References</a></li>
  </ol>
  
---
---
<br>
<h3><b><u>Description</u></b></h3>
This document is relating to pands-project2021 for programming and scripting module. The aim of this project is to research the well-know Fisher's Iris data set, doing so by writing documentation and python code to investigate the data. 
<br></br>

 <h4> To do list: </h4>
 <ul>
  <li>Research the dataset to get an understanding of the data recorded and decide what question I want to use the data to answer.</li>
  <li>Find the iris dataset, download it and convert it into a csv file. Import the dataset into visual studio code using the pandas module and load it into a pandas dataframe.</li>
  <li>Run a series of methods on the dataset to get a general overview of the data. Make sure there are missing values etc.</li>
  <li>Divide the iris dataframe into smaller data frames which consist of each species. To allow further investigation of the data to answer my question. </li>
  <li>Have all outputs generated to a summary text file.</li>
  <li>Visualise the data using matplotlib and seaborn.</li>
   <li>Write a readme file which details methods, modules, research and conclusions of my analysis.</li>
</ul>

-----
</br>
<br>
<h3><b><u>What Is The Iris DataSet?</u></b></h3>
<i>Fisher's Iris data</i> otherwise known as <i>The Iris flower data set</i> is a multivariate (more than one variable) data set  by the British statistician, eugenicist, and biologist Ronald Fisher in his 1936 paper <i>The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis</i> [1]. “Discriminant Analysis finds a set of prediction equations based on independent variables that are used to classify individuals into groups” 

The dataset contains 150 records with each row representing a species of iris flower. Each sample is divided under five columns. - Sepal Length, Sepal Width, Petal Length and Petal Width all in centimeters and the fifth column being the species of Iris. The three different species of iris recorded are; <b>Iris Setosa, Iris Versicolour and Iris Virginica.</b>

![Species of Iris](https://miro.medium.com/max/2000/1*nfK3vGZkTa4GrO7yWpcS-Q.png)

<h4>The goal of my analysis is to be able to identity each class of iris from the results I can do this by identifying how they differ from each other. To do this I will employ using a number of plots and graphs to help  identify variances within the species. 
The dataset has been downloaded from  the UCI repository.<h4>
----
</br>

<br>
<h3><b><u>Libraries Used</u></b></h3>

The below image demostrates how to import the libraries used:

![importing libraries](Images\importing_libraries.PNG)

<u><b>Numpy</b></u> is a Python library used for working with arrays. It produces a narray object. Numpy arrays are faster and more efficient than using python lists. It does this by storing arrays in one place in memory, so they can be accessed and manipulated quickly [ref]

<u><b>Pandas</b></u> is a data manipulation tool built on Numpy. It’s key structure is the dataframe. You can think of a dataframe as a spreadsheet or table but, dataframes as are more efficient and powerful and are an integral part of Python and Numpy [ref]. Pandas will allow us to select specific rows and columns within the dataframe.

<u><b>Mathplotlib</b></u> is a python library used to create plots, graphs, charts etc.

<u><b>Seaborn</b></u> is based on matplotlib and is also used to create data visualisations. “It provides a high-level interface for drawing attractive and informative statistical graphics.” [ref]

<u><b>sys</b></u> provides numerous variables and functions to manipulate the python environment. This particular project asks for the script to return the output to a text file and not the terminal. To do this we can use stdout. Stdout is “a built-in file object that is analogous to the interpreter’s standard output stream in Python” [ref]. This output can be in any form such as a print statement.  Output can be of any form, it can be output from a print statement.  
<br>

Now that the modules are imported we can import the dataset.

<br>
<h2><b><u>Import the dataset:</u></b></h2>
<ul>
  <li>Download the dataset from UCI repository.</li>
  <li>Import the dataset into python as a csv file using the pandas module. As the dataset contains no heading the name parameter can be used to include them. Without inserting column headings the data would only return 149 rows instead of 150 as pandas will automatically use the first row as a header if none is specified </li>
  
  ![importing data](Images\importing_data.PNG)
 
 <li>note: you could also use the .columns() method to do this.</li>
 </ul>
 
    
    df.columns(['Sepal Lenght(cm)', 'Sepal Width(cm)', 'Petal Lenght(cm)', 'Petal Width(cm)', 'Species'])

    


-----
</br>
<br>
<h3><b><u>Creating a text file for output</u></b></h3>
To create the text file for our analysis to be outputted to we do the following:

![creating a text file](Images\creating_text_file.PNG)
This automatically creates a new text file called Iris Analysis.
The 'w' means write to this file. When finished with the investigation I will change this to 'r' to read the file only.

![text file](Images\text_file.PNG)

The text file is now created and visable within the project folder in the lefthand sidepane.

![closing text file](Images\closing_text_file.PNG)

It is extremely important to close the file once finshed. Otherwise it will throw a host of problems. Make sure to put the above statement at the end of your code.

-----
</br>
<br>
<h3><b><u>Data Overview</u></b></h3>

![overview](Images\overview.PNG)

Getting an overview of the data using .info() to make sure it loaded correctly. This will return how many rows there are, column names, whether null and the type. We know there should be 150 rows and 5 columns from reseaching the data set.

By using .head() we can get a brief look at our data. It will automatically return the first 5 rows but, you can see more or less by passing a number to it.
*note: the '________' inculded in the print statement isn't part of the function. It's a personal decision tohelp make the formatting of the output to the text file clear by acting as a divider.

![cleaning data](Images\cleaning_data.PNG)

Checking the data for any null values
Checking for duplicates and if there are any, which rows. 
*note: by using .sum() will return the amount of null/duplicates.

*note: This returned three duplicates, as we know this is a balanced dataset On this occasion I decided against removing them.

![count](Images\count.PNG)

Using .count() we can see how many instances of each unique species the data contains. From research we know it ahould be 50 of each.

![stat overview](Images\describe.PNG)
Getting a summary of the dataframe values (count, mean,  standard deviation, min, percentile (25%, 50%, 75%), max).
Standard Deviation: is a measure of how spread out the data is spread out around the Standard Deviation: is a measure of how spread out the data is spread out around the mean (average).  

![mean groupby](Images\mean_groupby.PNG)

We can take closer look at the mean values for each variable with groupby. To filter by column, pass .groupby() the column you want to sort by (‘Species’ in this case) and follow it by the aggregate function - e.g. min, max, mean, count - you wish to perform. In the above picture mean is used.

<u>The following images are visualisations of the above findings:</u>

![countplot](Images\count_plot.png)
-----
</br>
<br>
<h2><b><u>Seperating the data:</u></b></h2>

![separating data](Images\separating_data.PNG)
Separating the iris data frame into smaller data frames comprising of each species. This will allow further investigation.
Now that we have separated the dataframe we can use seaborn and matplotlib to visualise each record to help make observations on.
- scatterplot, heatmap, violinplot, 
-----
</br>
<br>
<h2><b><u>Results</u></b></h2>

-----
</br>
<br>
<h2><b><u>Conclusions</u></b></h2>

-----
</br>

</br>

<br>
<h2><b><u>Acknowledgements</u></b></h2>

-----
</br>


<h2><b><u>References</u></b></h2>
https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
https://www.kite.com/python/answers/how-to-redirect-print-output-to-a-text-file-in-python
https://data36.com/plot-histogram-python-pandas/
https://miro.medium.com/max/2000/1*nfK3vGZkTa4GrO7yWpcS-Q.png
https://www.learnpython.org/en/Pandas_Basics
https://numpy.org/doc/stable/user/whatisnumpy.html
https://seaborn.pydata.org/#:~:text=Seaborn%20is%20a%20Python%20data,attractive%20and%20informative%20statistical%20graphics.
https://www.geeksforgeeks.org/python-sys-module/#:~:text=The%20sys%20module%20in%20Python,interact%20strongly%20with%20the%20interpreter.
https://realpython.com/pandas-groupby/
https://www.statisticshowto.com/probability-and-statistics/standard-deviation/#SDD
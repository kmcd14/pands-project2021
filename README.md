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
 
 <li>You could also use the .columns() method to do this.</li>
 </ul>
 
    ````
    df.columns(['Sepal Lenght(cm)', 'Sepal Width(cm)', 'Petal Lenght(cm)', 'Petal Width(cm)', 'Species'])

    ```


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
<br>
<h1><b><u> pands-project2021</u></b></h1>



<br>
<h3 style=color:#DDA0DD><b><u>Table of Contents</b></u></h3></summary>
  <ol>
    <li><a href='#Description'> Description</a></li>
    <li><a href='#Iris'> What Is the Iris DataSet?</a></li>
    
  <li><a href='#Technologies_Used'>Technologies Used</a></li>
    <li><a href="#Libraries_Used">Libraries Used</a></li>
    <li><a href="#Importing_Data">Importing The Data Set</a></li>
    <li><a href="#Text_File">Creating A Text File For Output</a></li>
    <li><a href="#Data_Analysis">Data Analysis</a></li>
      <ul>
        <li><a href="#Cleaning_Data">Cleaning Data</a></li>
        <li><a href="#Data_Summary">Data Summary</a></li>
        <li><a href="#Count">Count</a></li>
        <li><a href="#Stats">Stats</a></li>
        <li><a href="#Groupby">Groupby</a></li>
      </ul>

 <li><a href="#Visualisation">Data Visualisation</a></li>
  <ul>
      <li><a href="#Countplot">Countplot</a></li>
      <li><a href="#Histogram">Histogram</a></li>
      <li><a href="#Scatterplot">Scatterplot</a></li>
      <li><a href="#Boxplot">Boxplot</a></li>
      <li><a href="#Scatterplot">Scatterplot</a></li>
      <li><a href="#Pairplot">Pairplot</a></li>
      <li><a href="#Andrews_Curve">Andrews Curve</a></li>
      <li><a href="#Correlations">Correlations</a></li>
      <li><a href="#Clustermap">Clustermap</a></li>
    </ul>
    <li><a href="#Conclusion">Conclusion</a></li>  
    <li><a href="#References">References</a></li>
  </ol>
  
---
---
<br>
<b><u><p id='Description'> Description</b></u></p>
This document is relating to pands-project2021 for programming and scripting module. The aim of this project is to research and investigate the well-know Fisher's Iris data set, doing so by writing documentation and python script to investigate the data. This README contains the complete documentation for the project. The python script is saved as analysis.py. PLease note that the each bit of code is labelled in the script and what it outputs by use of comments. 
<br></br>

 <h4><u> Objectives and to do list: </u></h4>
 <ul>
  <li>Research the dataset to get an understanding of the data collected.</li>
  <li>Find the iris dataset and download it.</li>
  <li> Import the dataset into visual studio code using the pandas module and load it into a pandas dataframe.</li>
  <li> Cleaning the data; make sure there are no missing values etc.</li>
  <li>Run a series of data analysis methods on the data set to get a summary of the data such as, calculating the mean, maximum and minimum of each variable.</li>
  <li>Divide the iris dataframe into smaller data frames which consist of each species. To allow further investigation. </li>
  <li>Have all outputs generated to a summary text file.</li>
  <li>Visualise the data using matplotlib and seaborn.</li>
   <li>Write a readme file which details methods, modules, research and conclusions of my analysis.</li>
</ul>

-----
</br>
<br>
<b><u><p id='Iris'>What Is The Iris DataSet?</b></u></p>


The iris dataset is one of the most popular data sets in the world. A simple google alone generates almost 702,000 results. It is famous among scientists. It has been used to illustrate a variety of techniques such as pattern recongition, multivariate statistics, machine learning and data visualisation. 
1
<i>Fisher's Iris data</i> otherwise known as <i>The Iris flower data set</i> is a multivariate data set. This means the dataset involves more than one variable.[ref]  published by the British statistician, eugenicist, and biologist Ronald Fisher in his 1936 paper <i>The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis</i> [1].
<br>
</br>
Although published by Fisher, the data was orignally collected by American botanist, Edgar Anderson.
Anderson realised there was a <i>"great
amount of genetic variation exists within most natural populations of plants."</i> This realisation led him to conculde <i>""if we are to learn anything about the ultimate nature of species
we must reduce the problem to the simplest terms and study a few easily recognized, well differentiated species." </i>. [ref]. This led him to study the three species of iris.


The dataset contains 150 records with each row representing a species of iris flower. Each sample is divided under five columns. - Sepal Length, Sepal Width, Petal Length and Petal Width all in centimeters and the fifth column being the class/species of Iris. 
The samples where collected on the same day, in the same area, by the same person and measured with the sae appuratus at the same time to ensure justness. [ref wiki]. Fisher used a linear discriminant analysis (LDA) on the data set. That is <i>"...a dimension reduction method which finds an optimal linear transformation that maximizes the class separability."</i> [ref]i.e. be able to separate between the classes of iris'. 
<br>
The three different species of iris recorded are; <b>Iris Setosa, Iris Versicolour and Iris Virginica.</b>



![Species of Iris](https://miro.medium.com/max/2000/1*nfK3vGZkTa4GrO7yWpcS-Q.png)





----
</br>
<b><u><p id='Technologies_Used'> Technologies Used:</b></u></p>
 The data set was downloaded from the Center for Machine Learning and Intelligent Systems repository found here: https://archive.ics.uci.edu/ml/datasets/iris

<b><u>Google Docs:</u></b> an online word processor used to write my documentation before transfering into this README file. https://www.google.com/docs/about/

<b><u>Anaconda:</u></b> the easiest way to perfrom Python data science machine learning on Windows, Linux and Mac OS. This script was created using Version 4.9.2. https://www.anaconda.com/distribution/

<b><u>Python:</u></b> an interpreted, object-oriented, high-level programming language with dynamic semantics. This script was created using Version 3.8.5.  https://www.python.org/

<b><u>Visual Studio Code:</u></b> An open source coding editor. https://code.visualstudio.com/

---

<br>
<b><u><p id='Libraries_Used'>Libraries Used:</b></u></p>


The below image demostrates how to import the libraries used:

![importing libraries](Images\importing_libraries.PNG)

<u><b>Numpy</b></u> is a Python library used for working with arrays. It produces a narray object. Numpy arrays are faster and more efficient than using python lists. It does this by storing arrays in one place in memory, so they can be accessed and manipulated quickly http://www.numpy.org/

<u><b>Pandas</b></u> is a data manipulation tool built on Numpy. It’s key structure is the dataframe. You can think of a dataframe as a spreadsheet or table but, dataframes as are more efficient and powerful and are an integral part of Python and Numpy [ref]. Pandas will allow us to select specific rows and columns within the dataframe. https://pandas.pydata.org/

<u><b>Mathplotlib</b></u> is a python library used to create plots, graphs, charts etc. https://matplotlib.org/

<u><b>Seaborn</b></u> is based on matplotlib and is also used to create data visualisations. “It provides a high-level interface for drawing attractive and informative statistical graphics.” https://seaborn.pydata.org/

<u><b>sys</b></u> provides numerous variables and functions to manipulate the python environment. This particular project asks for the script to return the output to a text file and not the terminal. To do this we can use stdout. Stdout is “a built-in file object that is analogous to the interpreter’s standard output stream in Python” [ref]. This output can be in any form such as a print statement.  Output can be of any form, it can be output from a print statement.  https://docs.python.org/3/library/sys.html
<br>

Now that the modules are imported we can import the dataset.

<br>
<b><u><p id='Importing_Data'>Importing Data set:</b></u></p>

<ul>
  <li>Download the dataset from UCI repository.</li>
  <li>Import the dataset into python as a csv file using the pandas module. As the dataset contains no heading the name parameter can be used to include them. Without inserting column headings the data would only return 149 rows instead of 150 as pandas will automatically use the first row as a header if none is specified </li>
  
  ![importing data](Images\importing_data.PNG)
 
 <li>note: you could also use the .columns() method to do this.</li>
 </ul>
 
    
    df.columns(['Sepal Lenght(cm)', 'Sepal Width(cm)', 'Petal Lenght(cm)', 'Petal Width(cm)', 'Species'])

<b>Separating Data</b>

  ![separating data](Images\separating_data.PNG)
I have also decided to separating the iris data frame into smaller data frames comprising of each species. This will allow further investigation. 

-----
</br>
<b><u><p id='Text_File'>Creating A Text File For Output</b></u></p>

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
<b><u><p id='Data_Summary'>Data Summary:</b></u></p>

![overview](Images\overview.PNG)

![overview output](Images\overview_output.PNG)

Getting an overview of the data using .info() to make sure it loaded correctly. This will return how many rows there are, column names, whether null and the type. We know there should be 150 rows and 5 columns from reseaching the data set.

![header output](Images\header.PNG)

By using .head() we can get a brief look at our data. It will automatically return the first 5 rows but, you can see more or less by passing a number to it.

*note: the '________' inculded in the print statement isn't part of the function. It's a personal decision to help make the formatting of the output to the text file clear by acting as a divider.

---
<b><u><p id='Cleaning_Data'>Cleaning Data</b></u></p>


![cleaning data](Images\cleaning_data.PNG)

Here we are checking the data for any null values. We also can check for duplicates, and, if there are any, which rows.

![cleaning data output](Images\cleaning_data_output.PNG)

As we can see there is no null values in this dataset but there are 3 duplicates. 

*note: by using .sum() will return the amount of null/duplicates.

*note: This returned three duplicates, as we know this is a balanced dataset On this occasion I decided against removing them.

---
<b><u><p id='Count'>Count</b></u></p>


![count](Images\count.PNG)

![count](Images\count_output.PNG)

Using .count() we can see how many instances of each unique species the data contains. From research we know it ahould be 50 of each which there is.

---
<b><u><p id='Stats'>Stats</b></u></p>

![stat overview](Images\describe.PNG)
![stat overview](Images\stats.PNG)

Getting a summary of the dataframe values (count, mean,  standard deviation, min, percentile (25%, 50%, 75%), max).

*note: Standard Deviation: is a measure of how spread out the data is spread out around the mean (average).  

---

<b><u><p id='Groupby'>Groupby</b></u></p>


![mean groupby](Images\mean_groupby.PNG)

We can take closer look at these values for each species with groupby function. To filter by column, pass .groupby() the column you want to sort by (‘Species’ in this case) and follow it by the aggregate function - e.g. min, max, mean, count - you wish to perform. In the above code mean is used.

![mean](Images\mean.PNG)

![max](Images\max.PNG)

![min](Images\min.PNG)


<h4>Observations: 
From this we can see that iris-setosa varies a lot more than the other two when it comes to petal attributes. It also seems to on average have a wider sepal than iris-versicolour and iris-virginica.
It also looks like there may be a link between the sepal and petal lenght of the iris-virginica. <h4>

---
<b><u><p id='Data Visualisation'>Data Visualisation:</b></u></p>

We can use seaborn and matplotlib to visualise each record to help make observations on. Visualisation is important because it allows us to see pattens in the data which we may not have noticed otherwise. It is also allows for a far more digestible medium to relay findings to people than a speadsheet of numbers.

---
<b><u><p id='Countplot'>Countplot</b></u></p>

![countplot](Images\count_plot.png)

<h4>From the above countplot we can clearly see that there is an equal number of occurances of each species. 
<br>

-----
<br>
<b><u><p id='Histogram'>Histogram</b></u></p>

![hist](Images\hist_petal_lenght.png)
![hist](Images\hist_petal_width.png)
![hist](Images\hist_sepal_lenght.png)
![hist](Images\hist_sepal_width.png)


<h4>Above each variable is plotted on a histogram using seaborn. I used this to show how the three species differ in their anatomical features. These unique values are grouped into ranges whic are refered to as bins. KDE (kernel density estimation) can be turned on or off by passing kde='False'. KDE is used to estimate <i>the distribution of observations in a dataset, analagous to a histogram</i>


Some conclusions we can draw from this:
<li>The iris-virginica has the widest sepal width</li>
<li>The length of the iris-virginica sepal however is shorter than both the iris-setosa and versicolour which are both similar.</li>
 <li>The real telling difference comes from the petal measurements; 
 The iris-setosa is clearly distinguishable from the other two species. Being the outlier of the group and most likely to diverge from the average measurements.</li>

---
<b><u><p id='Scatterplot'>Scatterplot</b></u></p>

Using a scatterplot we can plot the variable pairs i.e. Petal Lenght and Width, and Sepal Lenght and Width to get a clearer view of how the species differ.

![scatter sepal](Images\scatter_sepal.png)
![scatter petal](Images\scatter_petal.png) 

<h4>The sepal scatterplot isn’t that distinguishable. We can see that the iris-setosa is more likely to be wider on average but there's a lot of crossover between iris-versicolour and iris-virginica meaning that distinguishing one from the other solely on sepal variables wouldn’t be conclusive enough as there is a lot of overlap. 
The Petal Scatterplot is a lot more conclusive and  tells us we can confidently identify the iris-setosa; it is more likely to be shorter in both petal length and width from the other two species. Although there is still some overlap, the iris-virginica is also more likely to have a wider and longer petal.
<br></br>

<b><u><p id='Boxplot'>Boxplot</b></u></p>
Another way we can view and visualise this distribution of data is by a using a boxplot


![boxplot](Images\boxplot.png) 

The box plot displays the distribution of quantitative data (Petal length, petal width, sepal length and width) which in turn allows us to make comparisons between the variables. The box shows the dataset and the whiskers (black markings) show the rest of the distribution.
Some observations:
- Sepal Width is comparatley short which suggests there is not much varient between species but the there is a lot of distribution.
- Petal lenght is the longest which suggests it is the main variable which differes between species. 
- The 4 sections of the box plot (lower quartile, upper quartile, inter quartile, whiskers) are uneven in size for each.  This shows that many flowers are similar but, vary much more in other areas such as the  upper whisker in both petal lenght and sepal lenght. 

----
<b><u><p id='Pairplot'>Pairplot</b></u></p>

It is possible to do an overview of all these plots on one grid by using a pairplot. A pairplot graphs the pairwise relationships of the numerical columns for the whole dataframe. The pairplot is a good way to get a visual overview of the data and can be used to make instant relationship connections.

![pairplot](Images\pairplot.png)

---
</br>
<b><u><p id='Andrews_Curve'>Andrews Curve</b></u></p>

While reseaching the various ways to visualise data. I came across Andrews curve and thought it could be an intresting addition to my analysis as it is a technique used for plotting multivariate data, which is what the iris data set is. Data with similar patterns will produce similar curves  and "...cases in a second group will have a different profile of values for the variables from those in the first group, and thus the curves produced for this second group will show a different pattern from those for the first group." [ref]. With this in mind, we can once again see how the iris-setosa is differs the most from the other two species.

![andrews curve](Images\andrews_curve.png)
</br>

---
<b><u><p id='Correlations'>Correlations</b></u></p>

Using .corr() we can further investigate the correlations between the four variables. 

![corr](Images\correlations.PNG)

To get a visual representation of these correlations we can use a matrix plots to create a heatmap. A matrix plots allows you to plot data as color-encoded matrices.
![heatmap](Images\heatmap.png)

From the heatmap we can conculde the there is a positive correlation between 
- petal width and sepal lenght 
- petal lenght and petal width
- sepal lenght and petal width
- longer petals seem to equate to wider petal width

We can investigate these correlations futher by using the individual dataframes for each species we created earlier. By using .corr() on each separately. 

![separate corr](Images\separate_correlations.PNG)

Looking at the species separately the correlation isn't as clear. 
The strongest correlation by far is the petal lenght and sepal lenght of the iris-versicolor. Otherwise, there isn't any major correlation when viewing each species individually.
___
<b><u><p id='Clustermap'>Clustermap:</b></u></p>


Another way we can visualise these correlation similarties is by using a clustermap. This is another matrix plot. A cluster map employs hierarchical clustering to cluster the rows and columns of the matrix. This means that it orders data by relationships and we can see where similarities lie.
I personally found this particular plot difficult to decipher at first but, we can see that iris-setosa has distinct charecteristics while Viriginica and Versicolor are harder to distngusish and are thus sorted into the same clusters.
![cluster map](Images\cluster_map.png)


</br>

-----
</br>
<br>
<h2><b><u>Conclusion</u></b></h2>
I approached the analysis with the same intention of its original purpose - to be able to identify the different species of iris by the variants in characteristics (Petal length, petal width, sepal length and sepal width). From this analysis I have concluded that the petal is the most important variable when classifying the species of iris. It is easier to distinguish its dimensions between the species than that of the sepal. 
<br></br>
Overall, I learnt a lot by doing this project. I had no previous experince with analysing data or much programming experience and was apprehensive about how to go about it. It is such a vast area and there are so many paths you could go with it, it can be overwhelming. I believe I have met the objectives of this project, which was to investigate the iris data set, analyse the data , create a python script to do this and document my findings in this README. 
I found using the data visualisation tools matplotlib and seaborn pivotal in helping me understand the data. It helped me see relationships between the data clearly. I can see why data visualisation is it’s own field and how important it is. I explored the styling libraries of these libraries to make visually pleasing plots, this is definitely an area I wish to explore more in the future. 
This README was also something that was new to me. Learning how to format and make it appealing was something that took a bit of time and again is something I would like to develop in future projects, as it’s often the first file that is seen when you click into the repository on github so its an important first impression. 
<br></br>
To conclude, while having met the objectives of this project there is a lot of room for improvement. I think this project was very much finding my feet and becoming comfortable with using python and how it can be used to explore data. My personal goal going forward is to build on the base that I have gained doing this project and get deeper into python's capabilities and core concepts of data analysis and science. This only scratches the surface of what can be achieved but acted as a strong building block for my knowledge and confidence in analysing data.

-----


---
<b><u><p id='References'>References</b></u></p>
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
https://books.google.ie/books?id=pQws07tdpjoC&printsec=frontcover&dq=what+is+hierarchical+clustering&hl=en&sa=X&ved=2ahUKEwiBspX3uNHvAhWMSxUIHW3UAoIQ6AEwBXoECAUQAg#v=onepage&q=what%20is%20hierarchical%20clustering&f=false
http://www.nasonline.org/publications/biographical-memoirs/memoir-pdfs/anderson-edgar.pdf
https://dl.acm.org/doi/10.1016/j.patcog.2007.07.022
https://www.researchgate.net/publication/237010807_What_should_we_know_about_the_famous_Iris_data
https://core.ac.uk/download/pdf/1636958.pdf
https://pandas.pydata.org/docs/reference/api/pandas.plotting.andrews_curves.html
<br>
<h1><b><u> pands-project2021</u></b></h1>



<br>
<h2 style=color:#DDA0DD><b><u>Table of Contents</b></u></h2></summary>
  <ol>
    <li><a href='#Description'> Description</a></li>
    <li><a href="#Script">How To Run analysis.py</a></li>
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
      <li><a href="#Parallel_Coordinates">Parallel Coordinates</a></li>
      <li><a href="#Correlations">Correlations</a></li>
      <li><a href="#Clustermap">Clustermap</a></li>
    </ul>
    <li><a href="#Conclusion">Conclusion</a></li>  
    <li><a href="#References">References</a></li>
  </ol>
  
---
---
<h2><b><u><p id='Description'> Description</b></u></p></h2>
This document is relating to pands-project2021 for programming and scripting module. The aim of this project is to research and investigate the well-know Fisher's Iris data set, doing so by writing documentation and python script to investigate the data. 

This README contains the complete documentation for the project. The python script is saved as analysis.py. PLease note that the each bit of code is labelled in the script and what it outputs by use of comments. 
Python script, documentation, cvs file and images can be found at https://github.com/kmcd14/pands-project2021.
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

---

<h3><b><u><p id='Script'> How To Run analysis.py</b></u></p></h3>

<ol>
<li>Create a folder on your desktop where you wish to store the code</li>
<li>Navigate to the repoistory https://github.com/kmcd14/pands-project2021.</il>
<br></br>

<img src='Images\git.PNG'>

<li>Copy the repository address, as seen in the above picture. Using either SSH or HTTPS</li>
<li>Open bash shell on your desktop and navigate to the folder you created earlier.</li>
<li>Once in the folder use 



    $git clone git@github.com:kmcd14/programming2021.git


</li>
<li>Set up pull mode and pull down the contents
</li>
<li>To run the code enter the below in the terminal</li></ol>

        $python .\analysis.py




</br>
<h3><b><u><p id='Iris'>What Is The Iris DataSet?</b></u></p></h3>

The iris dataset is one of the most popular data sets in the world. A simple google alone generates almost 702,000 results. It is famous among scientists. It has been used to illustrate a variety of techniques such as pattern recongition, multivariate statistics, machine learning and data visualisation. 

<i>Fisher's Iris data</i> otherwise known as <i>The Iris flower data set</i> is a multivariate data set. This means the dataset involves more than one variable (Wikipedia, 2021). It was published by the British statistician, eugenicist, and biologist Ronald Fisher in his 1936 paper <i>The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis</i> (Kozak, M. & Łotocka, B., 2013).
<br>
</br>
Although published by Fisher, the data was orignally collected by American botanist, Edgar Anderson.
Anderson realised there was a <i>"great
amount of genetic variation exists within most natural populations of plants" </i>(Stebbins, G. L., 1978). This realisation led him to conculde <i>""if we are to learn anything about the ultimate nature of species
we must reduce the problem to the simplest terms and study a few easily recognized, well differentiated species." </i>(Stebbins, G. L., 1978). This led him to study the three species of iris.


The dataset contains 150 records with each row representing a species of iris flower. Each sample is divided under five columns. - Sepal Length, Sepal Width, Petal Length and Petal Width all in centimeters and the fifth column being the class/species of Iris. 
The samples where collected on the same day, in the same area, by the same person and measured with the same appuratus at the same time to ensure justness (Wikipedia, 2021). Fisher used a linear discriminant analysis (LDA) on the data set. That is <i>"...a dimension reduction method which finds an optimal linear transformation that maximizes the class separability."</i> (Park, C.H., Park. H., 2008). i.e. be able to separate between the classes of iris'. 
<br></br>
The three different species of iris recorded are; <b>Iris Setosa, Iris Versicolour and Iris Virginica.</b>

![Species of Iris](https://miro.medium.com/max/2000/1*nfK3vGZkTa4GrO7yWpcS-Q.png)

(Medium, Image ref)

----
</br>

<h3><b><u><p id='Technologies_Used'> Technologies Used:</b></u></p></h3>

 The <b><u>data set</b></u> was downloaded from the Center for Machine Learning and Intelligent Systems repository found here: https://archive.ics.uci.edu/ml/datasets/iris

<b><u>Google Docs:</u></b> an online word processor used to write my documentation before transfering into this README file. https://www.google.com/docs/about/

<b><u>Anaconda:</u></b> the easiest way to perfrom Python data science machine learning on Windows, Linux and Mac OS. This script was created using Version 4.9.2. https://www.anaconda.com/distribution/

<b><u>Python:</u></b> an interpreted, object-oriented, high-level programming language with dynamic semantics. This script was created using Version 3.8.5.  https://www.python.org/

<b><u>Visual Studio Code:</u></b> An open source coding editor. https://code.visualstudio.com/

<b><u>GitHub:</u></b> is a code hosting platform for collaboration and version control. https://github.com/

---
---

<h3><b><u><p id='Libraries_Used'>Libraries Used:</b></u></p></h3>

<i>“Python is a widely-used, interpreted, object-oriented, and high-level programming language with dynamic semantics, used for general-purpose programming. It was created by Guido van Rossum, and first released on February 20, 1991”</i> (Python Institute, 2021). It is suitable for research, prototyping and building production systems, which eliminates the need for using different languages for both. Python has a vast and continuously growing library to choose from which makes it perfect for data analysis, such as Numpy and Pandas. It is a robust, flexible and efficient language which provides many solutions and avenues to approach and solve problems.

The below image demostrates how to import the libraries used for this project:

<img src='Images\importing_libraries.PNG'>


<u><b>Numpy</b></u> is a Python library used for working with arrays. It produces a narray object. Numpy arrays are faster and more efficient than using python lists. It does this by storing arrays in one place in memory, so they can be accessed and manipulated quickly http://www.numpy.org/

<u><b>Pandas</b></u> is a data manipulation tool built on Numpy. It’s key structure is the dataframe. You can think of a dataframe as a spreadsheet or table but, dataframes as are more efficient and powerful and are an integral part of Python and Numpy. Pandas will allow us to select specific rows and columns within the dataframe. https://pandas.pydata.org/

<u><b>Mathplotlib</b></u> is a python library used to create plots, graphs, charts etc. https://matplotlib.org/

<u><b>Seaborn</b></u> is based on matplotlib and is also used to create data visualisations. “It provides a high-level interface for drawing attractive and informative statistical graphics.” https://seaborn.pydata.org/

<u><b>sys</b></u> provides numerous variables and functions to manipulate the python environment. This particular project asks for the script to return the output to a text file and not the terminal. To do this we can use stdout. Stdout is “a built-in file object that is analogous to the interpreter’s standard output stream in Python”. This output can be in any form such as a print statement.  Output can be of any form, it can be output from a print statement.  https://docs.python.org/3/library/sys.html
<br>
<br>
<b>If your system does not have these libaries installed enter the below command from the command line: </b>

```
    $pip install <library name>
```
---
---
<h3><b><u><p id='Importing_Data'>Importing Data Set:</b></u></p></h3>

Now that the modules are imported we can import the dataset.
<ul>
  <li>Download the dataset from UCI repository.</li>
  <li>Import the dataset into python as a csv file using the pandas module. As the dataset contains no heading the name parameter can be used to include them. Without inserting column headings the data would only return 149 rows instead of 150 as pandas will automatically use the first row as a header if none is specified (pandas.org, 2021).
  </li>
  
  <img src='Images\importing_data.PNG'>
  
  
 
 <li>note: you could also use the .columns() method to do this.</li>
 </ul>
 
    
    df.columns(['Sepal Lenght(cm)', 'Sepal Width(cm)', 'Petal Lenght(cm)', 'Petal Width(cm)', 'Species'])
---
<h3><u><b>Separating Data</b></u></h3>

  <img src='Images\separating_data.PNG'>


I have also decided to separating the iris data frame into smaller data frames comprising of each species. This will allow for further opportunties investigation (learnpython.org, 2021)

---
-----
</br>
<h3><b><u><p id='Text_File'>Creating A Text File For Output</b></u></p></h3>

To create the text file for our analysis to be outputted to we do the following (GeeksforGeeks, 2021):

<img src='Images\creating_text_file.PNG'>

This automatically creates a new text file called Iris Analysis.
The 'w' means write to this file.

<img src='Images\text_file.PNG'>

The text file is now created and visable within the project folder in the lefthand sidepane.

<img src='Images\closing_text_file.PNG'>

It is extremely important to close the file once finshed. Otherwise it will throw a host of problems. Make sure to put the above statement at the end of your code (kite.com, 2021).

-----
---
<h2><b><u><p id='Data_Summary'>Data Summary</b></u></p></h2>
<br>

<img src='Images\overview.PNG'>

<br>

<img src='Images\overview_output.PNG'>

Getting an overview of the data using .info() to make sure it loaded correctly. This will return how many rows there are, column names, whether null and the type. We know there should be 150 rows and 5 columns from reseaching the data set.

<img src='Images\header.PNG'>

By using .head() we can get a brief look at our data. It will automatically return the first 5 rows but, you can see more or less by passing a number to it.

*note: the '________' inculded in the print statement isn't part of the function. It's a personal decision to help make the formatting of the output to the text file clear by acting as a divider.

---
<h3><b><u><p id='Cleaning_Data'>Cleaning Data</b></u></p></h3>

<img src='Images\cleaning_data.PNG'>

Here we are checking the data for any null values. We also can check for duplicates, and, if there are any, which rows.

<img src='Images\cleaning_data_output.PNG'>

As we can see there is no null values in this dataset but there are 3 duplicates. 

*note: by using .sum() will return the amount of null/duplicates.

*note: This returned three duplicates, as we know this is a balanced dataset, so on this occasion I decided against removing them.

---
<h3><b><u><p id='Count'>Count</b></u></p></h3>

<img src='Images\count.PNG'>
<img src='Images\count_output.PNG'>

Using .count() we can see how many instances of each unique species the data contains. From research we know it ahould be 50 of each which there is.

---
<h3><b><u><p id='Stats'>Stats</b></u></p></h3>

<img src='Images\describe.PNG'>
<img src='Images\stats.PNG'>

Getting a summary of the dataframe values (count, mean,  standard deviation, min, percentile (25%, 50%, 75%), max).

*note: Standard Deviation: is a measure of how spread out the data is spread out around the mean (average). (Glen, S., 2021). 

Using the data we separated earlier into smaller dataframes we can do the same for each species
 <img src='Images\indivdual_summary().PNG'>
 <img src='Images\indivdual_summary.PNG'>

---

<h3><b><u><p id='Groupby'>Groupby</b></u></p></h3>

<img src='Images\mean_groupby.PNG'>

We can take closer look at these values for each species with groupby function. To filter by column, pass .groupby() the column you want to sort by (‘Species’ in this case) and follow it by the aggregate function - e.g. min, max, mean, count - you wish to perform. In the above code mean is used. (Solomon, B., 2021)

<img src='Images\mean.PNG'>
<img src='Images\max.PNG'>
<img src='Images\min.PNG'>

<h4>Observations: 
From this we can see that iris-setosa varies a lot more than the other two when it comes to petal attributes. It also seems to on average have a wider sepal than iris-versicolour and iris-virginica.
It also looks like there may be a link between the sepal and petal lenght of the iris-virginica. <h4>

---
<h2><b><u><p id='Data Visualisation'>Data Visualisation:</b></u></p></h2>

We can use seaborn and matplotlib to visualise each record to help make observations on. Visualisation is important because it allows us to see pattens in the data which we may not have noticed otherwise. It is also allows for a far more digestible medium to relay findings to people than a speadsheet of numbers.

---
<h3><b><u><p id='Countplot'>Countplot</b></u></p></h3>

<img src='Images\count_plot.png'>

<h4>From the above countplot we can clearly see that there is an equal number of occurances of each species. 
<br>

-----
<h3><b><u><p id='Histogram'>Histogram</b></u></p></h3>

<img src='Images\hist_petal_lenght.png'>
<img src='Images\hist_petal_width.png'>
<img src='Images\hist_sepal_lenght.png'>
<img src='Images\hist_sepal_width.png'>

<h4>Above each variable is plotted on a histogram using seaborn. I used this to show how the three species differ in their anatomical features. These unique values are grouped into ranges whic are refered to as bins. KDE (kernel density estimation) can be turned on or off by passing kde='False'. KDE is used to estimate <i>the distribution of observations in a dataset, analagous to a histogram</i> (Seaborn.org, 2021)


Some conclusions we can draw from this:
<li>The iris-virginica has the widest sepal width</li>
<li>The length of the iris-virginica sepal however is shorter than both the iris-setosa and versicolour which are both similar.</li>
 <li>The real telling difference comes from the petal measurements; 
 The iris-setosa is clearly distinguishable from the other two species. Being the outlier of the group and most likely to diverge from the average measurements.</li>

---
<h3><b><u><p id='Scatterplot'>Scatterplot</b></u></p></h3>

Using a scatterplot we can plot the variable pairs i.e. Petal Lenght and Width, and Sepal Lenght and Width to get a clearer view of how the species differ.

<img src='Images\scatter_sepal.png'>
<img src='Images\scatter_petal.png'>
<h4>The sepal scatterplot isn’t that distinguishable. We can see that the iris-setosa is more likely to be wider on average but there's a lot of crossover between iris-versicolour and iris-virginica meaning that distinguishing one from the other solely on sepal variables wouldn’t be conclusive enough as there is a lot of overlap. 
The Petal Scatterplot is a lot more conclusive and  tells us we can confidently identify the iris-setosa; it is more likely to be shorter in both petal length and width from the other two species. Although there is still some overlap, the iris-virginica is also more likely to have a wider and longer petal.
<br></br>

---

<h3><b><u><p id='Boxplot'>Boxplot</b></u></p></h3>
Another way we can view and visualise this distribution of data is by a using a boxplot

<img src='Images\boxplot.png'>

The box plot displays the distribution of quantitative data (Petal length, petal width, sepal length and width) which in turn allows us to make comparisons between the variables. The box shows the dataset and the whiskers (black markings) show the rest of the distribution.
Some observations:
- Sepal Width is comparatley short which suggests there is not much varient between species but the there is a lot of distribution.
- Petal lenght is the longest which suggests it is the main variable which differes between species. 
- The 4 sections of the box plot (lower quartile, upper quartile, inter quartile, whiskers) are uneven in size for each.  This shows that many flowers are similar but, vary much more in other areas such as the  upper whisker in both petal lenght and sepal lenght. 

----
<h3><b><u><p id='Pairplot'>Pairplot</b></u></p></h3>

It is possible to do an overview of all these plots on one grid by using a pairplot. A pairplot graphs the pairwise relationships of the numerical columns for the whole dataframe. The pairplot is a good way to get a visual overview of the data and can be used to make instant relationship connections.

<img src='Images\pairplot.png'>

---

<h3><b><u><p id='Andrews_Curve'>Andrews Curve</b></u></p></h3>

While reseaching the various ways to visualise data. I came across Andrews curve and thought it could be an intresting addition to my analysis as it is a technique used for plotting multivariate data, which is what the iris data set is. Data with similar patterns will produce similar curves  and "...cases in a second group will have a different profile of values for the variables from those in the first group, and thus the curves produced for this second group will show a different pattern from those for the first group" (Spencer, N.H., 2003). With this in mind, we can once again see how the iris-setosa is differs the most from the other two species (pandas.org, 2021).

<img src='Images\andrews_curve.png'>
<br>
</br>
<h3><b><u><p id='Parallel_Coordinates'>Parallel Coordinates</b></u></p></h3>
Another way to compare features of a multivariate data is by using a parallel coordinate plot. For this particular plot I used pandas built in data visualisation tool. See below on how to import.

<img src='Images\parallell coord import.PNG'>

<img src='Plots\Parallel Coordinates.png'>


A parallel coordinate plot<i>“... allows to compare the feature of several individual observations (series) on a set of numeric variables. Each vertical bar represents a variable and often has its own scale. (The units can even be different). Values are then plotted as series of lines connected across each axis”</i> (Data to Viz, 2021).

From looking at this plot we can once again see that it is the petal variables where there are the most variations between the species, with the iris-setosa most distinguishable differences.

---
<h3><b><u><p id='Correlations'>Correlations</b></u></p></h3>

Using .corr() we can further investigate the correlations between the four variables. 

<img src='Images\correlations.PNG'>

To get a visual representation of these correlations we can use a matrix plots to create a heatmap. A matrix plots allows you to plot data as color-encoded matrices (seaborn.org, 2021).

<img src='Images\heatmap.png'>

From the heatmap we can conculde the there is a positive correlation between 
- petal width and sepal lenght 
- petal lenght and petal width
- sepal lenght and petal width
- longer petals seem to equate to wider petal width

We can investigate these correlations futher by using the individual dataframes for each species we created earlier. By using .corr() on each separately. 

<img src='Images\separate_correlations.PNG'>

Looking at the species separately the correlation isn't as clear. 
The strongest correlation by far is the petal lenght and sepal lenght of the iris-versicolor. Otherwise, there isn't any major correlation when viewing each species individually.
___
<h3><b><u><p id='Clustermap'>Clustermap:</b></u></p></h3>


Another way we can visualise these correlation similarties is by using a clustermap. This is another matrix plot. A cluster map employs hierarchical clustering to cluster the rows and columns of the matrix. This means that it orders data by relationships and we can see where similarities lie (Han, J., Pei, J., Kamber, M., 2011). 
I personally found this particular plot difficult to decipher at first but, we can see that iris-setosa has distinct charecteristics while Viriginica and Versicolor are harder to distngusish and are thus sorted into the same clusters.

<img src='Images\cluster_map.png'>


</br>

-----
----
</br>
<h2><b><u>Conclusion</u></b></h2>
I approached the analysis with the same intention of its original purpose - to be able to identify the different species of iris by the variants in characteristics (Petal length, petal width, sepal length and sepal width). From this analysis I have concluded that the petal is the most important variable when classifying the species of iris. It is easier to distinguish its dimensions between the species than that of the sepal. 
<br></br>

Although, interestingly in my research, I came across a journal article which states that some botanists disagree about whether or not an iris actually has a sepal. It is amusing to think that such a famous and pivotal data set could potentially have contain such a large flaw. 
Both petals and sepals are leaves which have adapted. 
The debate lies in the fact that <i>“...the morphological distinction of perianthium and perigo-nium, or sepaloid and petaloid perigon is not clear”</i> (Kozak, M. & Łotocka, B., 2013). This is their molecular makeup. So while the iris data set is widely used in data science, statistics and machine learning it is nowhere near as important or impactful in the world of biotomy. 
<br></br>
Overall, I learnt a lot by doing this project. I had no previous experince with analysing data or much programming experience and was apprehensive about how to go about it. It is such a vast area and there are so many paths you could go with it, it can be overwhelming. This project also introduced me to new concepts such as KDE, linear discriminant analysis, clustering, Andews Curve and by way an introduction to algorithms and machine learning, all of which I had no previous experience and knowledge of. I look forward to continued learning and improving and building my experince knowledge in these areas as the course progresses. I believe I have met the objectives of this project, which was to investigate the iris data set, analyse the data , create a python script to do this and document investigation.
I found using the data visualisation tools matplotlib and seaborn pivotal in helping me understand the data. It helped me see relationships between the data clearly. I can see why data visualisation is it’s own field and how important it is. I explored the styling libraries of these libraries to make visually pleasing plots, this is definitely an area I wish to explore more in the future. 

Documenting a project of this nature was also something  new to me. Learning how to format and make it appealing was something that took a bit of time and again is something I would like to develop for future projects, as it’s often the first file that is seen when you click into the repository on github, so its an important first impression. Time management was an important factor for me too. Currently, I am working fulltime and have a number of other projects/assignments so setting my own deadlines and working towards them was vital to managing the workload.
<br></br>
To conclude, while having met the objectives of this project there is a lot of room for improvement. I think this project was very much finding my feet and becoming comfortable with using python and how it can be used to explore data. My personal goal going forward is to build on the base that I have gained doing this project and get deeper into python's capabilities and core concepts of data analysis and science. This only scratches the surface of what can be achieved but acted as a soild building block for my knowledge and confidence in analysing data.

-----


---
<h2><b><u><p id='References'>References</b></u></p></h2>

Data to Viz. (2021). PARALLEL COORDINATES PLOT. Available: https://www.data-to-viz.com/graph/parallel.html. Last accessed 21st April 2021.

GeeksforGeeks. (2021). Python sys Module. Available: https://www.geeksforgeeks.org/python-sys-module/#:~:text=The%20sys%20module%20in%20Python,interact%20strongly%20with%20the%20interpreter. Last accessed 15th March 2021.

Han, J., Pei, J., Kamber, M (2011). Data Mining: Concepts and Techniques. 3rd ed. Massachusetts: Elsevier. 457-458.

kite.com. (2021). How to redirect print output to a text file in Python. Available: https://www.kite.com/python/answers/how-to-redirect-print-output-to-a-text-file-in-python. Last accessed 16th March 2021.

Kozak, M. & Łotocka, B. (2013). What should we know about the famous Iris data?. Current Science. 104 (5), p579-580.

learnpython.org. (2021). Pandas Basics. Available: https://www.learnpython.org/en/Pandas_Basics. Last accessed 17th March 2021.

Medium, Image ref: https://miro.medium.com/max/2000/1*nfK3vGZkTa4GrO7yWpcS-Q.png

Park, C.H., Park. H. (2008). A comparison of generalized linear discriminant analysis algorithms. Pattern Recognition. 41 (3), 1083-1097.

pandas.org. (2021). pandas.read_csv. Available: https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html. Last accessed 16th March 2021.

pandas.org. (2021). pandas.plotting.andrews_curves. Available: https://pandas.pydata.org/docs/reference/api/pandas.plotting.andrews_curves.html. Last accessed 28th March 2021.

Python Institute. (2021). What is Python?. Available: https://pythoninstitute.org/what-is-python/. Last accessed 21st April 2021.

seaborn.org. (2021). Visualizing distributions of data. Available: https://seaborn.pydata.org/tutorial/distributions.html. Last accessed 20th March 2021.

seaborn.org. (2021). seaborn.heatmap. Available: https://seaborn.pydata.org/generated/seaborn.heatmap.html. Last accessed 25th March 2021.

Solomon, B. (2021). Pandas GroupBy: Your Guide to Grouping Data in Python. Available: https://realpython.com/pandas-groupby/. Last accessed 24th March 2021.

Spencer, N.H. (2003). Investigating Data With Andrews Plots. Social Science Computer Review. 21 (2), p244-249.

Stebbins, G. L. (1978). Edgar Anderson: November 9, 1897-June 18, 1969. Washington D.C.: National Academy of Sciences. 5.

Wikipedia. (2021). Iris Flower Data Set. Available: https://en.wikipedia.org/wiki/Iris_flower_data_set. Last accessed 15th March 2021.
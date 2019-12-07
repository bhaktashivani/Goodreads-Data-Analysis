# Goodreads-Data-Analysis

### Project Overview
In this project, we will be analyzing data from a book review website called Goodreads in order to analyze types of books and popular books based on reviews, ratings, and number of pages.
We answered several questions about our dataset, including:
1. What languages are most common?
2. What kinds of ratings do users give books in our dataset?
3. What relationship is there between rating and rating count/number of text reviews/number of pages?
4. What are the individual books with the highest number of ratings?
5. What are the individual books with the highest number of reviews?
6. How many books did the top 5 rated authors in our dataset write?
7. Do people prefer dead authors to authors that are alive?

### How to run the code:
1. Put all the files (datav4.csv, Final_code.ipynb, Lang_vs_num.py, Top_10_books.py, etc.) in one folder.
2. Open Final_code.ipynb and run to see all the plots.
3. Add your own dataset to this folder and replace the dataset name in Final_code.ipynb to make new plots.

### Third-party modules being used
numpy, pandas, os, seaborn, matplotlib, pylab
 
## File Structure

### Goodreads folder
The API we used to gain data.

### datav4.csv
THe dataset we used.

### ratingalive.txt
We use this file to record the dead and live author ratings.

### Final_code.ipynb
This file call all functions in .py files and show the plots.

### ECE143_Group22_Goodreads_Data_Analysis.pdf
Our slides for presentation.

##  There are six .py files
### Lang_vs_num.py
This file has a function lan_vs_num(data), which takes the dataset and gets the column of the languages and plots a bar plot with languages and number of books, excluding all types of english books.
It alsp plots a pie chart with English and other languages percentage.  

### Top_10_books.py
This file has three functions highest_reviews_books(data), highest_ratings_count_books(data) and highest_num_pages_books(data). They plot the the books with the highest number of reviews, the books with the highest number of ratings and the books with the highest number of pages.

### Rating_distribution.py
This file has a function rate_distribution(data), which plots a histogram to show the rating distribution for the books. 

### deadAuthor.py
This file has a function deadAuthors() which plots the garph whether dead or live author has higher rating

### plot_books_written.py
This file has a function plot_books_written() which plots the garoh of top author books count

### triPlot.py
This file has a function rating_distribution(path) which plots rating versus 1.ratings count 2.text reviews count 3.pages count.

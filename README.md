# Goodreads-Data-Analysis



### How to run the code:
1. Put all the files (datav4.csv, Final_calls.ipynb, Lang_vs_num.py, Top_10_books.py, etc.) in one folder.
2. Open Final_calls.ipynb and run to see all the plots.
3. Add your own dataset to this folder and replace the dataset name in Final_calls.ipynb to make new plots.

### Lang_vs_num.py
This file has a function lan_vs_num(data), which takes the dataset and gets the column of the languages and plots a bar plot with languages and number of books, excluding all types of english books.
It alsp plots a pie chart with English and other Languages percentage.  

### Top_10_books.py
This file has three functions highest_reviews_books(data), highest_ratings_count_books(data) and highest_num_pages_books(data). They plot the the books with the highest number of reviews, the books with the highest number of ratings and the books with the highest number of pages.

### Rating_distribution.py
This file has a function rate_distribution(data), which plots a histogram to show the rating distribution for the books. 

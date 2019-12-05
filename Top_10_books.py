get_ipython().run_line_magic('matplotlib', 'inline') 
import numpy as np 
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
from pylab import plot, show
from matplotlib.lines import Line2D
import matplotlib.colors as mcolors

def highest_reviews_books(data):
    '''
    Checking for the books with the highest reviews.
    '''
    most_text = data.sort_values('text_reviews_count', ascending = False).head(10).set_index('title')
    plt.figure(figsize=(20,15))
    #sns.set(font_scale=2.5)
    #sns.set_style('white')
    ls=sns.barplot(most_text['text_reviews_count'], most_text.index,color='saddlebrown')
    ls.set_xlabel("Num of Reviews",fontsize=30,fontweight='bold')
    ls.set_ylabel("",fontsize=30)
    plt.xticks(fontsize=30,fontweight='bold')
    plt.yticks(fontsize=30,fontweight='bold')
    plt.show()
    #ls.set_title("Top 10 Books with the Highest Number of Reviews",fontsize=40)

def highest_ratings_count_books(data):
    '''
    Checking for the books with the highest ratings count.
    '''
    most_text = data.sort_values('ratings_count', ascending = False).head(10).set_index('title')
    plt.figure(figsize=(20,15))
    #sns.set(font_scale=2.5)
    #sns.set_style('white')
    ls=sns.barplot(most_text['ratings_count'], most_text.index,color='saddlebrown')
    ls.set_xlabel("Num of Ratings",fontsize=30,fontweight='bold')
    ls.set_ylabel("",fontsize=30)
    plt.xticks(fontsize=30,fontweight='bold')
    plt.yticks(fontsize=30,fontweight='bold')
    plt.show()
    #ls.set_title("Top 10 Books with the Highest Number of Ratings",fontsize=40) 

def highest_num_pages_books(data):
    '''
    Checking for the books with the highest number of pages.
    '''
    most_text = data.sort_values('num_pages', ascending = False).head(10).set_index('title')
    plt.figure(figsize=(20,15))
    sns.set(font_scale=2.5)
    sns.set_style('white')
    ls=sns.barplot(most_text['num_pages'], most_text.index,color='saddlebrown')
    ls.set_xlabel("Num of Pages",fontsize=30,fontweight='bold')
    ls.set_ylabel("",fontsize=30)
    #ls.set_title("Top 10 Books with the Highest Number of Pages",fontsize=40) 
    plt.show()


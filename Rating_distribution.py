import numpy as np 
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
from pylab import plot, show
from matplotlib.lines import Line2D
import matplotlib.colors as mcolors

def rate_distribution(data):
    '''
    purpose: plots a histogram to show the rating distribution for the books. 
    :param x: input average rating of the books 
    :type x: data
    '''
    sns.set() 
    plt.figure(figsize=(15,10))
    sns.set_style('white')
    sns.set_context('poster')
    ls=sns.distplot(data['rating'],color="darkred",kde=False)
    ls.set_xlabel('Ratings',fontweight='bold',fontsize=20)
    ls.set_ylabel('Num of Ratings',fontweight='bold',fontsize=20)
    plt.xticks(fontsize=20,fontweight='bold')
    plt.yticks(fontsize=20,fontweight='bold')
    #plt.title('Rating Distribution for the Books')
    plt.show()

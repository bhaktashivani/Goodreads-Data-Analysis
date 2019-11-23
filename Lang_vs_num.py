import pandas as pd
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
from heapq import nlargest
from operator import itemgetter

def lan_vs_num(data):
    '''
    purpose: Takes the dataset and gets the column of the languages and plots a bar plot with languages and 
    number of books, excluding english and plot a pie chart with english and other languages percentage.  

    :param x: input pd.series object 
    :type x: pd.core.series.Series

    return: None
    '''
    
    x = data['language']
    language_list = list(', '.join(x.array).split(','))
    language_list = list(set(language_list))

    counters  = []
    dic = {}
    for lan in language_list: 
        counters.append(', '.join(x.array).split(',').count(lan))

    
    Summ = 0
    for i in range(len(counters)-1):
        Summ  = Summ + counters[i]

    #remove eng from the list.
    nSum = 0
     
    for i in range(len(language_list)-6):
        if language_list[i] == ' eng' or language_list[i] == 'eng' or language_list[i] == ' en-US' or language_list[i] == 'en-US' or language_list[i] == ' en-GB' or language_list[i] == 'en-GB':
            m = language_list.pop(i) #m = eng 
            n = counters.pop(i)  #n = # of eng books 
            Summ = Summ - n #subtract Summ of all books with number of eng books
            nSum = nSum + n
        
    sizes = [nSum, Summ] #suzesfor pie chart
    
    # Plot the pie chart English VS Other Languages
    fig = plt.figure()
    labels=['English', 'Other Languages']
    plt.pie(sizes, explode = (0, 0.1), labels=['English', 'Other Languages'], colors=['DarkRed', 'indianred'],
         autopct='%1.1f%%', shadow=False, startangle=220, textprops=dict(color="black"))
    #plt.legend(labels,loc=3)
    plt.axis('equal')
    fig.savefig('PieChart1.png', transparent = True)
    
    
    
    tupList= [] #make a list of tuples such that list = [(lan1, count1), (lan2, count2), ....]
    for i in range(len(language_list)): 
        tupList.append((language_list[i], counters[i]))
    
    #Now sort the tuple so we can get the top 5. 
    
    Len_tuple = len(tupList)  
    for i in range(0,len(tupList)):   
        for j in range(0, Len_tuple-i-1):  
            if (tupList[j][1] < tupList[j + 1][1]):  
                temp = tupList[j]  
                tupList[j]= tupList[j + 1]  
                tupList[j + 1]= temp 
    
    #get top 5 and remove other languages from the list of tuples
    tupList = nlargest(5, tupList, key=itemgetter(1)) #tupList now only has top 5 lan and count. 
    language_list = [x[0] for x in tupList]
    counters = [x[1] for x in tupList]
    
    
    #for i in range(len(tupList))
    #Plot the other top 5 languages. 
    fig = plt.figure()
    #graph the histogram without English
    y_pos = np.arange(len(language_list))
    #print("y_pos= ", y_pos)
    plt.bar(y_pos, counters, align='center', alpha=0.5, color= 'firebrick')
    plt.xticks(y_pos, language_list)
    plt.ylabel('Number of Books', fontweight= 'bold')
    plt.xlabel('Languages', fontweight= 'bold')
    #plt.title('Language vs Number of books', fontweight= 'bold')
    plt.show()
    fig.savefig('BarChart1.png', transparent = True)
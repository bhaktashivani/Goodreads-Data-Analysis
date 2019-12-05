#!/usr/bin/env python
# coding: utf-8

# In[5]:


import csv
from goodreads import client
gc = client.GoodreadsClient('pvr3ns4Le0DCqEpAG2jlQ', '4BM2D4d8ZvFcJNqRQ3OjQq1Qh3OrvMAvHiI0lTOUFE')

def takeSecond(elem):
    return elem[1]
def get_dead_Data():
    dsum=0
    dcnt=0
    asum=0
    acnt=0
    with open('datav3.csv','r',encoding="utf-8") as f:
        reader = csv.reader(f)
        fieldnames = next(reader)
        # print(fieldnames)
        csv_reader = csv.DictReader(f,fieldnames=fieldnames)
        cntAuthor={}
        authoridx={}
        anthortotalrating={}
        cntc=0
        for row in csv_reader:
            cntc+=1
            if cntc==3000:
                break
            d={}
            for k,v in row.items():
                d[k]=v
            bookidx=d['ID']
            author = gc.author(gc.book(bookidx).authors[0].gid)
            wk=author.died_at
            if wk==None:
                acnt+=1
                asum+=float(d['rating'])
            else:
                dcnt+=1
                dsum+=float(d['rating'])
            print("index:%s    acnt:%s dcnt:%s "%(cntc,acnt,dcnt))

    f=open('ratingalive.txt','w')
    f.write("acnt:%s dcnt:%s"%(acnt,dcnt))
    f.write("asum:%s dsum:%s"%(asum,dsum))
    f.close()
    print("dead author average rating:%s"%dsum/dcnt)
    print("live author average rating:%s"%asum/acnt)


# In[8]:


# In[2]:


def deadAuthors():
    '''
    plot the garph whether dead or live author has higher rating
    '''
    import seaborn as sns
    import matplotlib.pyplot as plt
    b=['dead author','live author']
    a=[3.893,3.827]
    sns.set(font_scale=5)
    sns.set_style("white")
    fig=plt.figure(figsize=(20,15))
    ls=sns.barplot(b,a,palette='dark')
    #ls.set_ylabel("Rating",fontsize=70,fontweight='bold')
    plt.xticks(fontweight='bold',fontsize=40)
    plt.yticks(fontweight='bold',fontsize=30)
    #ls.set_title("Author Live Ratings",fontsize=70)
    sns.set(style="whitegrid")
    fig.savefig('dieAuthor.png',transparent=True)
deadAuthors()


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def plot_books_written():
    '''
    plot the garoh of top author books count
    '''
    import seaborn as sns
    import matplotlib.pyplot as plt
    import numpy as np
    fl=open('tepTenAuthorRatingWork.txt','r')
    lines=fl.readlines()
    xx=[]
    yy=[]
    zz=[]
    #print(lines[0].split())
    a=lines[0].split()
    for i in range(1,6):
        ll=lines[len(lines)-i].split()
        aut=''
        for j in ll[0:len(ll)-2]:
            aut+=j
            aut+=' '
        if 'Magazin' in aut:
            continue
        if 'Hayao' in aut:
            aut='Hayao Miyazaki'
        if 'Feynman' in aut:
            aut='Richard P. Feynman'
        if 'Conan Doyle' in aut:
            aut='Conan Doyle'
        if 'Christina Scull' in aut:
            aut='Christina Scull'
        xx.append(aut.rstrip())
        yy.append(int(ll[len(ll)-1]))
        zz.append(float(ll[len(ll)-2]))
    #print(xx)
    #print(yy)
    #print(zz)
    fig=plt.figure(figsize=(20,15))
    sns.set(font_scale=1.5)
    sns.set_style("white")
    ls=sns.barplot(yy,xx,color='saddlebrown')
    ls.set_xlabel("Books Written",fontsize=40,fontweight='bold')
    plt.xticks(fontsize=50,fontweight='bold')
    plt.yticks(fontsize=50,fontweight='bold')
    plt.tick_params(labelsize=30)
    #ls.set_ylabel("Author Name",fontsize=30,fontweight='bold')
    #ls.set_title("Top ten rated author books count",fontsize=50,fontweight='bold')
    ls.tick_params(labelsize=40)
    '''
    for i in ls.patches:
            ls.text(i.get_width()+2, i.get_y()+0.5,str(int(i.get_width())), fontsize=20,color='black')
            ls.text(i.get_width()+2, i.get_y()+0.5,str(int(i.get_width())), fontsize=20,color='black')
    '''
    fig.savefig('top10.png',transparent=True)
    fl.close()


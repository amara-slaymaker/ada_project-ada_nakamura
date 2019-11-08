# -*- coding: utf-8 -*-
"""Function used to perform Principal Component Analysis"""
import pandas as pd
import matplotlib.pyplot as plt
from random import randint

def PCA_viz(df):
    
    #configuration of the figure
    fig = plt.figure(figsize = (8,8))
    ax = fig.add_subplot(1,1,1) 
    ax.set_xlabel('Principal Component 1', fontsize = 15)
    ax.set_ylabel('Principal Component 2', fontsize = 15)
    ax.set_title('2 component PCA', fontsize = 20)
    
    #random generation of colors
    colors = []
    n = len(df[df.columns[-1]]) #size of the column containing the targets
    for i in range(n):
        colors.append('#%06X' % randint(0, 0xFFFFFF))
        
    #plot
    ax.scatter(df.loc[:, 'PC1']
                   , df.loc[:, 'PC2']
                   , c = colors
                   , s = 50)
    #ax.legend(areas)
    ax.grid()
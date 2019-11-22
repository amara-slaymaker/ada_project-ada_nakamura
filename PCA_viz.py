# -*- coding: utf-8 -*-
"""Function used to perform Principal Component Analysis"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from random import randint

def PCA_viz(df):
    
    #configuration of the figure
    fig = plt.figure(figsize = (8,8))
    ax = fig.add_subplot(1,1,1) 
    ax.set_xlabel('Principal Component 1', fontsize = 15)
    ax.set_ylabel('Principal Component 2', fontsize = 15)
    ax.set_title('2 component PCA', fontsize = 20)
    
    #plot
    ax.grid(alpha=0.5)
    ax = sns.scatterplot(x='PC1', y='PC2',data=df, s=80,edgecolor="black")
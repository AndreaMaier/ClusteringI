# -*- coding: utf-8 -*-
"""
Created on Thu May 17 15:36:35 2018

@author: Andrea
"""

import pandas as pd
import ClusteringI_C_DataCleaning as dataCleaning
import matplotlib.pyplot as plt

def data_Correlation():
    data = dataCleaning.data_Cleaning()
    
    corr_matrix = data.corr()
    print(corr_matrix)
    fig, ax = plt.subplots()
    cax = ax.imshow(corr_matrix, cmap='hot', interpolation='nearest')
    ax.set_xticklabels(corr_matrix.keys())
    ax.set_xticks(range(0, len(corr_matrix.keys())))
    ax.set_yticklabels(corr_matrix.keys())
    ax.set_yticks(range(0, len(corr_matrix.keys())))
    for p in ax.get_xmajorticklabels():
        p.set_rotation(90)
    fig.colorbar(cax)
    plt.subplots_adjust(left=0.3, right=0.9, bottom=0.3, top=0.9)
    ax.set_aspect("equal")
    fig.savefig('correlation_heatmap', bbox_inches="tight")

def data_Reduction():
    data = dataCleaning.data_Cleaning()
    data = data.drop(['displacement'], axis=1)
    data = data.drop(['carName'], axis=1)
    return data

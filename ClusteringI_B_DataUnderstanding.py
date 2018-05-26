# -*- coding: utf-8 -*-
"""
Created on Thu May 17 12:03:48 2018

@author: Andrea
"""

import pandas as pd
import ClusteringI_A_Import as importData
import matplotlib.pyplot as plt

data = importData.get_Data()

def data_Understanding():
    print(data.keys())
    print(data.describe())
    print(data.count())
    print(data.shape[0])
    print(data.index)
    print(data.info())
    
    print(data['carName'].describe())
    boxplot = data.boxplot(column=['MPG'])
    boxplot = data.boxplot(column=['cylinders'])
    boxplot = data.boxplot(column=['displacement'])
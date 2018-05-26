# -*- coding: utf-8 -*-
"""
Created on Thu May 17 13:33:16 2018

@author: Andrea
"""

import pandas as pd
import ClusteringI_A_Import as importData

def data_Cleaning():
    data = importData.get_Data()
    keys = data.keys()
    
    for key in keys:
        index = data[data[key].isnull()].index
        for i in index:
            data = data.drop([i])
            
    for i in data.index:
        if data['MPG'][i] < 9:
            data = data.drop([i]) 
        
    for i in data.index:
        if data['cylinders'][i] < 1:
            data = data.drop([i])
    
    for i in data.index:
        if data['displacement'][i] == 0:
             data = data.drop([i])

    #print(data.count())
    return data
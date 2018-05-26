# -*- coding: utf-8 -*-
"""
Created on Thu May 17 16:46:57 2018

@author: Andrea
"""
import pandas as pd
import ClusteringI_D_DataReduction as dataReduction
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = dataReduction.data_Reduction()

kMeans = KMeans(n_clusters=6, precompute_distances=True).fit(data)
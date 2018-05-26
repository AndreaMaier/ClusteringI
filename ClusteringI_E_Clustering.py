# -*- coding: utf-8 -*-
"""
Created on Thu May 17 16:46:57 2018

@author: Andrea
"""
import numpy as np
from sklearn.preprocessing import StandardScaler
import ClusteringI_D_DataReduction as dataReduction
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score

data = dataReduction.data_Reduction()
data = StandardScaler().fit_transform(data)

def kMeans():
    clusters = range(2,20)
    for c in clusters:
        kMeans = KMeans(n_clusters=c, precompute_distances=True).fit_predict(data)
        s = silhouette_score(data, kMeans)
        print('Cluster: ', c, '\t-->\tSilhouette: ', round(s,4))

def dbscan():
    eps = np.arange(0.5, 1.5, 0.1)
    min_samples = range(8,11)
    for e in eps:
        e = round(e,1)
        print('\n')
        for ms in min_samples:
            dbscan = DBSCAN(e, ms).fit_predict(data)
            s = silhouette_score(data, dbscan)
            print('Eps: ', e, '\tmin_samples:', '{:2}'.format(ms), '\t-->\tSilhouette: ', round(s,4))

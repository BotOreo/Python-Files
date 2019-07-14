# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 19:23:57 2018

@K means algorithm 

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

os.chdir('C:/Users/muham/Documents/CSC 3303_Big Data Analytics/Project/K-Means-clustering-master')

dataset=pd.read_csv('Training_set_2.csv')

X=dataset.iloc[1:,[4,2]].values #to choose row and column.

#Using the elbow method to find the optimal number of clusters

from sklearn.cluster import KMeans

wcss=[]
for i in range(1,11):
    kmeans=KMeans(n_clusters=i, init='k-means++',random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
'''
plt.plot(range(1,11),wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()
'''

#Fitting K-MEans to the dataset
k=3
kmeans=KMeans(n_clusters=k,init='k-means++',random_state=0)
y_kmeans=kmeans.fit_predict(X)

#Visualize the clusters

plt.scatter(X[y_kmeans==0,0],X[y_kmeans==0,1],s=3,c='red',label='Cluster1')
plt.scatter(X[y_kmeans==1,0],X[y_kmeans==1,1],s=3,c='blue',label='Cluster2')
plt.scatter(X[y_kmeans==2,0],X[y_kmeans==2,1],s=3,c='green',label='Cluster3')
plt.scatter(X[y_kmeans==3,0],X[y_kmeans==3,1],s=3,c='cyan',label='Cluster4')
plt.scatter(X[y_kmeans==4,0],X[y_kmeans==4,1],s=3,c='magenta',label='Cluster5')
'''
plt.scatter(X[y_kmeans==4,0],X[y_kmeans==4,1],s=10,c='black',label='Cluster6')
plt.scatter(X[y_kmeans==4,0],X[y_kmeans==4,1],s=10,c='yellow',label='Cluster7')
plt.scatter(X[y_kmeans==4,0],X[y_kmeans==4,1],s=10,c='indigo',label='Cluster8')
plt.scatter(X[y_kmeans==4,0],X[y_kmeans==4,1],s=10,c='grey',label='Cluster9')
'''
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=30,c='yellow',label='Centroids')

plt.title('K-Mean Clustering')
plt.xlabel('Number of Reviews')
plt.ylabel('Rating')
plt.legend()
plt.show()























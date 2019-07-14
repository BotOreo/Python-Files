import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from sklearn import cluster, datasets, preprocessing, metrics
from sklearn.metrics import pairwise_distances
import matplotlib
matplotlib.style.use('ggplot')
import seaborn as sns

os.chdir('C:/Users/muham/Documents/CSC 3303_Big Data Analytics/Project/K-Means-clustering-master')

apps = pd.read_csv("Training_set_2.csv")
print(apps.head())
#print(apps.Category.nunique())
#cols = apps.columns[:-1]
sns.set(style="ticks",color_codes=True)
sns.pairplot(apps, hue='Category',vars=['Rating','Reviews'])

#sns.pairplot(apps, hue='Genres',vars=['Annual Income (k$)','Spending Score (1-100)'])
#sns.pairplot(apps, hue='Genre',vars=['Annual Income (k$)','Age'])

plt.show()
#X = apps.drop("age", axis =1)
#X = apps.drop("sex", axis =1)
'''
X_scaled = preprocessing.normalize(X,axis=0)
J=apps.iloc[1:,[3,4]].values
k=5

kmeans = cluster.KMeans(n_clusters=k)
y_kmeans = kmeans.fit(X_scaled)
kmeans.fit(X_scaled)

plt.scatter(J[y_kmeans==0,0],J[y_kmeans==0,1],s=3,c='red',label='Cluster1')
plt.scatter(J[y_kmeans==1,0],J[y_kmeans==1,1],s=3,c='blue',label='Cluster2')
plt.scatter(J[y_kmeans==2,0],J[y_kmeans==2,1],s=3,c='green',label='Cluster3')
plt.scatter(J[y_kmeans==3,0],J[y_kmeans==3,1],s=3,c='cyan',label='Cluster4')
plt.scatter(J[y_kmeans==4,0],J[y_kmeans==4,1],s=3,c='magenta',label='Cluster5')

plt.scatter(X[y_kmeans==4,0],X[y_kmeans==4,1],s=10,c='black',label='Cluster6')
plt.scatter(X[y_kmeans==4,0],X[y_kmeans==4,1],s=10,c='yellow',label='Cluster7')
plt.scatter(X[y_kmeans==4,0],X[y_kmeans==4,1],s=10,c='indigo',label='Cluster8')
plt.scatter(X[y_kmeans==4,0],X[y_kmeans==4,1],s=10,c='grey',label='Cluster9')

plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=30,c='yellow',label='Centroids')
plt.show(kmeans)
inertia = kmeans.inertia_
print('Sillhouette Score: ')
#metrics.silhouette_score(X_scaled, labels=kmeans, metric='euclidean')
'''
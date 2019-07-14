#Muhammad Arif Lutfi Bin Aziz       1315791
#Tun Muhammad Zaim Bin Aminuddin    1629501
#Mohd Faris Fitri Bin Mohd Hanafi   1614839
#Muhammad Zharif Bin Msduki         1611777

import nltk
import string
import os
from collections import Counter
import math
import matplotlib.pyplot as plt
from nltk.stem.porter import *
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

article_count = 0   #to count how many article in a folder

list_test = ["win", "ringgit", "trade", "game", "killed"]
key_list =[]
value_list=[]

def idf(list_tf, list_test, w_count, article_count):
    for i in range(len(w_count)):
        print("This is idf")
        print(list_test[i])
        print(math.log(article_count/w_count[i]))
        print("\n")
    for keys,values in list_tf.items():
        print("This is tf-idf")
        print(keys)
        tf_idf=values*(math.log(article_count/w_count[i]))
        print(tf_idf)
        print("\n")
        return tf_idf
                      
def tf(key,value,y):
    key_list.append(key)
    list_tf = {}
    print(key)
    print("This is value of Y - %d" % y)  # Tengok dekat sini Zaimmmm
    print("This is value of x - %d" % value)  # Tengok dekat sini Zaimmmm
    tf = value/y
    print("Value of tf %f" %tf)
    value_list.append(tf)
    return tf

def get_tokens():
    os.chdir('C:/Users/muham/Documents/CSC 4309_Natural Language Processing/Article/')
    with open('art1.dat', 'r') as article:
        text = article.read()
        lowers = text.lower()
        no_punctuation = lowers.translate(string.punctuation)
        tokens = nltk.word_tokenize(no_punctuation)
        return tokens

tokens = get_tokens()
count = Counter(tokens)

path = 'C:/Users/muham/Documents/CSC 4309_Natural Language Processing/Article/'

value = 0
y = 0
w_count = [0] * len(list_test)

for z in range(len(list_test)):
    w_count[z] = 0
    

for subdir, dirs, files in os.walk(path):
    for file in files:
        file_path = subdir +os.path.sep + file
        article = open(file_path, 'r')
        text = article.read()
        lowers = text.lower().replace(","," ")
        create_list = lowers.split()
        tokens_tf = Counter(create_list)

        for i in range(len(list_test)):       #loop 5 times
            y = 0
            for keys, values in tokens_tf.items():
                y += tokens_tf.get(keys)  #And siniiiii
            #print("This is value of Y - %d" %y) # Tengok dekat sini Zaimmmm
            for keys, values in tokens_tf.items():
                if list_test[i] == keys:
                    value = tokens_tf[keys]
                    print("Article number %d" %int(article_count+1))
                    w_count[i] += 1
                    TF=tf(keys,value, y)
                    print("\n")
        article_count += 1

list_tf=dict(zip(key_list, value_list))
TF_IDF=idf(list_tf, list_test, w_count, article_count)

TF_IDF = TfidfVectorizer()
TF = TF_IDF.fit_transform(create_list)

print(TF_IDF)
print(TF)

def k_means(TF):
    true_k=2
    model = KMeans(n_clusters=true_k, init='k-means++', max_iter=50, n_init=1)
    model.fit(TF)
    print('Top terms per cluster: ')
    order_centroids = model.cluster_centers_.argsort()[:,::-1]
    terms=TF_IDF.get_feature_names()

    for i in range(true_k):
        #print("Cluster %d: " %i)
        for ind in order_centroids[i, :10]:
            print(' %s' % terms[ind])
k_means(TF)

plt.plot([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24],[71,41,55,75,27,52,82,14,87,68,93,35,92,44,11,35,19,68,34,78,95,81,11,83,26],'ro')
plt.show()

plt.plot([120,121,122,123,124,125,1256,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146],[63,28,51,70,4,69,94,21,15,30,1,73,7,11,49,22,3,10,9,86,90,47,60,83,17],'ro')
plt.show()
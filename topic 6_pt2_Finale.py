#Muhammad Arif Lutfi Bin Aziz       1315791
#Tun Muhammad Zaim Bin Aminuddin    1629501
#Mohd Faris Fitri Bin Mohd Hanafi   1614839
#Muhammad Zharif Bin Msduki         1611777

import nltk
import string
import os
from collections import Counter
import math
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
                      
def tf(key,value,y):
    key_list.append(key)
    list_tf = {}
    print(key)
    tf = value/y
    print("Value of tf %f" %tf)
    value_list.append(tf)

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
            print("This is value of Y - %d" %y) # Tengok dekat sini Zaimmmm
            for keys, values in tokens_tf.items():
                if list_test[i] == keys:
                    value = tokens_tf[keys]
                    print("Article number %d" %int(article_count+1))
                    w_count[i] += 1
                    tf(keys,value, y)
                    print("\n")
        article_count += 1

list_tf=dict(zip(key_list, value_list))
idf(list_tf, list_test, w_count, article_count)



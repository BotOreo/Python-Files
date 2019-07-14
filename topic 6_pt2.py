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

#nltk.download('punkt')     # first time je kene download
#nltk.download('stopwords')

article_count = 0   #to count how many article in a folder

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
print(count.most_common(10))


print(len(count.items()))
 

#step 2
tokens = get_tokens()
filtered = [w for w in tokens if not w in stopwords.words('english')]   #english sebab nak remove stopwords of english, boleh tukar ke bahasa lain
count = Counter(filtered)
print('\n')
print(count.most_common(10))


#step 3
def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
        return stemmed

stemmer = PorterStemmer()
stemmed = stem_tokens(filtered, stemmer)
count = Counter(stemmed)
print('\n')
print(count.most_common(10))

#step 4
token_dict = {}
stemmer = PorterStemmer()

#path = 'C:/Users/Asus.DESKTOP.ODK17EC/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/2 april topic 6 pt 2'
path = r'''E:\Zaim\3rd_Year_1st_Sem _2018_2019_sem_2\NLP\Topic NLP'''

'''
def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
        return stemmed
'''
def tokenize(text):
    tokens = nltk.word_tokenize(text)
    stems = stem_tokens(tokens, stemmer)
    return stems

for subdir, dirs, files in os.walk(path):
    print("Test1")
    for file in files:
        print("Test2")
        file_path = subdir +os.path.sep + file
        article = open(file_path, 'r')
        text = article.read()
        lowers = text.lower()
        no_punctuation = lowers.translate(string.punctuation)
        token_dict = no_punctuation
        article_count += 1

print("article count")
print(article_count)

print("-----------TOKENS-----------------")
print(tokens)
print("----------------------------")
tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
tfs = tfidf.fit_transform(tokens)
print("-----------TFS TFIDF------------------")
print(tfs)
print(tfidf)
print("----------------------------")
def k_means(tfs):
    true_k = 2
    model = KMeans(n_clusters = true_k, init='k-means++', max_iter=50, n_init=1)
    model.fit(tfs)
    print("Top terms per cluster:")
    order_centroids = model.cluster_centers_.argsort()[:, ::-1]
    terms = tfidf.get_feature_names()

    for i in range(true_k):
        print("Cluster %d:" % i)
        for ind in order_centroids[i, :10]:
            print(' %s' % terms[ind])


k_means(tfs)


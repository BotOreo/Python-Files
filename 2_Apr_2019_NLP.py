import nltk
import string
import os
import math
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem.porter import *
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
article_count=0 # this is z
list_test = ["win","ringgit","trade","game","killed"] #this is x
list_count = dict()

def get_Token():
    os.chdir('C:/Users/muham/Documents/CSC 4309_Natural Language Processing/Article/')
    with open('art1.dat','r') as article:
        text = article.read()
        lowers = text.lower()
        no_punctuation =  lowers.translate(string.punctuation)
        tokens = nltk.word_tokenize(no_punctuation)
        return tokens


def stem_tokens(tokens,stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed


tokens=get_Token()
filtered = [w for w in tokens if not w in stopwords.words('english')]
print("Tokens all ")
#print(tokens)
count=Counter(tokens)
count1=Counter(filtered)
#print(count.most_common(10))

#print(count1.most_common(10))

stemmer=PorterStemmer()
stemmed=stem_tokens(filtered,stemmer)
count2=Counter(stemmed)
#print(count2.most_common(10))
#print(len(count.items())) # this is for y

path = 'C:/Users/muham/Documents/CSC 4309_Natural Language Processing/Article/'

token_dict ={}
stemmer = PorterStemmer()

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    stems = stem_tokens(tokens,stemmer)
    return stems

value=[]


idf_count = 0 #counter untuk tf-idf (no of term x accross all document)
for subdir,dirs,files in os.walk(path):
    #print("Loop 1")
    for k in range(len(list_test)):
        w_count = 0
        for file in files:
            tokens_list = []
            if k == 0:
                article_count+=1 # this is going to be z
            #print("print %d" %w_count)
            #print("Lop2")
            file_path = subdir +os.path.sep + file
            article = open(file_path, 'r')
            text = article.read()
            lowers = text.lower().replace(","," ")
            create_list = lowers.split()
            tokens_tf = Counter(create_list)
            print(tokens_tf)
            for keys,values in tokens_tf.items():  # total number in dictionary
                tokens_list.append(keys) # to change the dictionary to list
                temp=[values]
                if list_test[k]==keys.replace(",","").replace(".",""):
                    print("Hahahahahah")
                    value.append(temp)
            print("----------Wuwi---------------")
            #print(range(len(tokens_tf)))
            #print(len(tokens_list))
            #print("Token list")
            print(value)
            print(len(tokens_list))
            y=len(tokens_list)
            #print(range(len(tokens_tf.items())))
            print("-------------------------")
            for w in range(0,len(tokens_list)):
               #print("Tootoru")
                #print("-----------Wu is -------------")
                #print("W is %d" %w)
                #print("------------     ------------")
                #w_count += 1
                #print(list_test[k])
                #print("W_count = %d" %w_count)
                print("------------------------")
                print(tokens_list[w])
                print(list_test[k])
                if str(tokens_list[w])==str(list_test[k]):
                    print("Value of w = %d " %w)
                    print("Value of k =  %d" %k)
                    w_count += 1
                    print("This is value 1 of w_count %d" %w_count)

                    #break

        print("This is value 2 of w_count %d" %w_count)
        list_count.append(w_count)

        print("-------------Total doc-------------------")
        print(list_count)
        print("-------------End doc-------------------")
        #print("\n")
       # token_dict[file] = no_punctuation



print("Article : %d" %article_count)
#rint("Token Dict")
#print(token_dict)
#print("No punch")

#print(no_punctuation)


#def list_app(value):
#    list


'''
tfidf = TfidfVectorizer(tokenizer=tokenize,stop_words='english')
tfs = tfidf.fit_transform(token_dict.values())

#print(tfidf)
#print(tfs)




def k_means(tfs):
    true_k=2
    model = KMeans(n_clusters=true_k, init='k-means++', max_iter=50, n_init=1)
    model.fit(tfs)
    print('Top terms per cluster: ')
    order_centroids = model.cluster_centers_.argsort()[:,::-1]
    terms=tfidf.get_feature_names()

    for i in range(true_k):
        #print("Cluster %d: " %i)
        for ind in order_centroids[i, :10]:
            print(' %s' % terms[ind])
k_means(tfs)

   for w in range(len(tokens_tf.items())) :
            #print("Bawah ni W")
            #print(w)
            #print("----------------------------------")
'''
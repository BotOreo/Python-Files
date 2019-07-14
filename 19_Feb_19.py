#Class Natural Language Processing 19 February 2019
import nltk
from nltk.book import *

x=("Welcome to NLP Class")
#print(x.split())
y=x.split()
#print(list(y[0]))

al_b=("Welcome welcome Welcome helloooooooooooooooooooooooooooooo welcome to to to to to NLP class Class class")
text1=al_b.split()
long_w=[words for words in text1 if len(words) > 15] #print words, bring forward the command into front
print(long_w)


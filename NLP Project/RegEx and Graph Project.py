#Tun Muhammad Zaim Bin Aminuddin    1629501
#Section 1

import re
import matplotlib.pyplot as plt
import numpy as np

x2 = []
y2 = []
x3 = []
y3 = []

total_dog = 0
total_cat = 0
total_all = 0

positive_cat = 0
negative_cat = 0
neutral_cat = 0

positive_dog = 0
negative_dog = 0
neutral_dog = 0


f = open('Dog.dat', 'r')
u = open('Cat.dat', 'r')

s = f.read()
s2 = u.read()

sentiment_value = re.compile('[-]?[0]+[.]+[0]?[0-9]?[0-9]?[0-9]?[0-9]?')
sentiment_value1 = sentiment_value.findall(s,re.I)
sentiment_value2 = sentiment_value.findall(s2,re.I)

timestamp = re.compile('1[0-9]{12}')
timestamp1 = timestamp.findall(s,re.I)
timestamp2 = timestamp.findall(s2,re.I)
'''
date = re.compile('\d+[-]\d+[-]\d+')
date1 = date.findall(s,re.I)
time = re.compile('\d+[:]\d+[:]\d+')
time1 = time.findall(s,re.I)
'''
print(len(timestamp1))
print(len(sentiment_value1))

print(len(timestamp2))
print(len(sentiment_value2))


for x in range(len(timestamp1)):
  
    y2.append(float(sentiment_value1[x]))
    x2.append(int(timestamp1[x]))
    total_dog += 1
    
    if float(sentiment_value1[x]) > 0:
        positive_dog += 1
    elif float(sentiment_value1[x]) == 0:
        neutral_dog += 1
    elif float(sentiment_value1[x]) < 0:
        negative_dog += 1
    
print("arif-------------------------------------------------------")
for x in range(len(timestamp2)):
    
    y3.append(float(sentiment_value2[x]))
    x3.append(int(timestamp2[x]))
    total_cat += 1
    
    if float(sentiment_value1[x]) > 0:
        positive_cat += 1
    elif float(sentiment_value1[x]) == 0:
        neutral_cat += 1
    elif float(sentiment_value1[x]) < 0:
        negative_cat += 1

print("Result")
print(positive_dog)
print(positive_cat)
print(negative_dog)
print(negative_cat)
total_all = total_cat + total_dog
#print(zaim2)
#print(zaim2)
plt.scatter(x2,y2, label='Dog', color='blue', s=3, marker="x")    #scatter plot for unsorted
plt.scatter(x3,y3, label='Cat', color='red', s=3, marker="o")

plt.xlabel('Timestamp (ms)')
plt.ylabel('Sentiment Value')
plt.title('Scatter Plot for Project')
plt.legend()
plt.grid()
plt.show()
    
    

# Data to plot for dog
labels = "Positive", "Neutral", "Negative"
sizes = [positive_dog, neutral_dog, negative_dog]

colors = ["palegreen", "blue", "orangered"]
explode = (0.1, 0, 0)  # explode 1st slice

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle = 270)

plt.title('Percent of Sentiment Analysis of Dog', size=20)
plt.show()



# Data to plot for cat
labels = "Positive", "Neutral", "Negative"
sizes = [positive_cat, neutral_cat, negative_cat]

colors = ["palegreen", "blue", "orangered"]
explode = (0.1, 0, 0)  # explode 1st slice


plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle = 270)

plt.title('Percent of Sentiment Analysis of Cat', size=20)
plt.show()

# Data to plot for total
labels = "Cat", "Dog"
sizes = [total_cat, total_dog]

colors = ["palegreen", "blue"]
explode = (0.1, 0)  # explode 1st slice


plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle = 270)

plt.title('Total Data Stream Tweets', size=20)
plt.show()

# Data to plot for 
labels = "Cat", "Dog"


colors = ["palegreen", "blue"]
#explode = (0.1, 0)  # explode 1st slice


plt.hist([y3,y2], bins = 15, label=["Cat", "Dog"])
#plt.hist(y2,bins = 25)
plt.xlabel('Sentiment Value')
plt.ylabel('Number of sentiment')
plt.title('Cat vs Dog Histogram', size=20)
plt.legend(loc='upper right')
plt.show()




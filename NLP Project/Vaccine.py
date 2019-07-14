# Tun Muhammad Zaim Bin Aminuddin    1629501
# Section 1

import re
import matplotlib.pyplot as plt
import numpy as np
import os
os.chdir('C:/Users/muham/Documents/CSC 4309_Natural Language Processing/Project/Project')

x2 = []
y2 = []
x3 = []
y3 = []

total_vaccine = 0
#total_cat = 0
#total_all = 0

#positive_cat = 0
#negative_cat = 0
#neutral_cat = 0

positive_vaccine = 0
negative_vaccine= 0
neutral_vaccine= 0

f = open('Vaccine.dat', 'r')
#u = open('Cat.dat', 'r')

s = f.read()
#s2 = u.read()

sentiment_value = re.compile('[-]?[0]+[.]+[0]?[0-9]?[0-9]?[0-9]?[0-9]?')
sentiment_value1 = sentiment_value.findall(s, re.I)
#sentiment_value2 = sentiment_value.findall(s2, re.I)

timestamp = re.compile('1[0-9]{12}')
timestamp1 = timestamp.findall(s, re.I)
#timestamp2 = timestamp.findall(s2, re.I)
'''
date = re.compile('\d+[-]\d+[-]\d+')
date1 = date.findall(s,re.I)
time = re.compile('\d+[:]\d+[:]\d+')
time1 = time.findall(s,re.I)
'''
print(len(timestamp1))
print(len(sentiment_value1))

#print(len(timestamp2))
#print(len(sentiment_value2))

for x in range(len(timestamp1)):

    y2.append(float(sentiment_value1[x]))
    x2.append(int(timestamp1[x]))
    total_vaccine += 1

    if float(sentiment_value1[x]) > 0:
        positive_vaccine += 1
    elif float(sentiment_value1[x]) == 0:
        neutral_vaccine += 1
    elif float(sentiment_value1[x]) < 0:
        negative_vaccine += 1
'''
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
'''
print("Result")
print(positive_vaccine)
#print(positive_cat)
print(negative_vaccine)
print(neutral_vaccine)
print(total_vaccine)
#total_all = total_cat + total_dog
# print(zaim2)
# print(zaim2)

plt.rcParams['font.size'] = 20
plt.scatter(x2, y2, label='Vaccine', color='blue', s=3, marker="x")  # scatter plot for unsorted
#plt.scatter(x3, y3, label='Cat', color='red', s=3, marker="o")

plt.xlabel('Timestamp (ms)')
plt.ylabel('Sentiment Value')
plt.title('Scatter Plot for Project')
plt.legend()
plt.grid()
plt.show()

# Data to plot for dog
labels = "Positive", "Neutral", "Negative"
sizes = [positive_vaccine, neutral_vaccine, negative_vaccine]

colors = ["palegreen", "blue", "orangered"]
explode = (0.1, 0, 0)  # explode 1st slice
plt.rcParams['font.size'] = 30

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=270)

plt.title('Percent of Sentiment Analysis on Vaccination', size=20)
plt.show()

# Data to plot for cat
#labels = "Positive", "Neutral", "Negative"
#sizes = [positive_cat, neutral_cat, negative_cat]

#colors = ["palegreen", "blue", "orangered"]
#explode = (0.1, 0, 0)  # explode 1st slice

#plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=270)

#plt.title('Percent of Sentiment Analysis of Cat', size=20)
#plt.show()
'''
# Data to plot for total
labels = "Vaccine"
sizes = [total_vaccine]

colors = ["palegreen", "blue"]
explode = (0.1, 0)  # explode 1st slice

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=270)

plt.title('Total Data Stream Tweets', size=20)
plt.show()
'''
'''
# Data to plot for
labels = "Vaccine"

colors = ["palegreen"]
# explode = (0.1, 0)  # explode 1st slice


plt.hist(y2, bins=15, label="Vaccine")
# plt.hist(y2,bins = 25)
plt.xlabel('Sentiment Value')
plt.ylabel('Number of sentiment')
plt.title('Hi', size=20)
plt.legend(loc='upper right')
plt.show()
'''




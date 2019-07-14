#Tun Muhammad Zaim Bin Aminuddin    1629501
#Section 1

import re
import matplotlib.pyplot as plt
import numpy as np

x2 = []
y2 = []
x3 = []
y3 = []


f = open('Dog.dat', 'r')
u = open('Cat.dat', 'r')

s = f.read()
s2 = u.read()

#b = open('sentiment_file.txt', 'w')
#c = open('timestamp_file.txt', 'w')

#d = open('sentiment_file.txt', 'w')
#e = open('timestamp_file.txt', 'w')

#host_address = re.compile('[fe]+\d+.+[0-9]')
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

#print("%-30s" % "MAC Address", "%-20s" % "Date of Access", "%-30s" % "Time of Access")
#print(len(host_address1))

for x in range(len(timestamp1)):
    #print("%-30s" % str(host_address1[x]), "%-20s" % str(date1[x]), "%-30s" % str(time1[x]))
    #print("%-30s" % str(host_address1[x]))
    #sentiment.append(str(host_address1[x]))
    '''b.write(sentiment_value1[x])
    b.write("\n")
    c.write(timestamp1[x])
    c.write("\n")'''
    y2.append(sentiment_value1[x])
    x2.append(timestamp1[x])
    #print("Sentiment: " + "%-10s" % sentiment_value1[x] + "Timestamp: " + "%-15s" % timestamp1[x])
    #print(timestamp1[x])

print("arif-------------------------------------------------------")
for x in range(len(timestamp2)):
    #print("%-30s" % str(host_address1[x]), "%-20s" % str(date1[x]), "%-30s" % str(time1[x]))
    #print("%-30s" % str(host_address1[x]))
    #sentiment.append(str(host_address1[x]))
    '''
    b.write(sentiment_value2[x])
    b.write("\n")
    c.write(timestamp2[x])
    c.write("\n")
    '''
    y3.append(sentiment_value2[x])
    x3.append(timestamp2[x])
    #print("Sentiment: " + "%-10s" % sentiment_value2[x] + "Timestamp: " + "%-15s" % timestamp2[x])
    #print(timestamp1[x])

    

#b.close()
#c.close()


'''
np.random.seed(200)
k = 3
# centroids[i] = [x, y]
colmap = {1: 'r', 2: 'g', 3: 'b'}
centroids = {
    i+1: [np.random.randint(0, 80), np.random.randint(0, 80)]
    for i in range(k)
}

for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])    
'''
#y = sentiment_value1
#x = timestamp1
#y1 = sentiment_value2
#x1 = timestamp2

#sorted(float(x))
#sorted(float(y))
zaim = [float(i) for i in y2]
zaim2 = sorted(zaim)
zaim3 = [int(i) for i in x2]
zaim4 = sorted(zaim3)

arif = [float(i) for i in y3]
arif2 = sorted(arif)
arif3 = [int(i) for i in x3]
arif4 = sorted(arif3)
#print(zaim2)
plt.scatter(zaim3,zaim, label='Dog', color='blue', s=3, marker="x")    #scatter plot for unsorted
plt.scatter(arif3,arif, label='Cat', color='red', s=3, marker="o")

plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot for Project')
plt.legend()
plt.grid()
plt.show()
    
    # Data to plot
    labels = "Positive", "Neutral", "Negative"
    sizes = [positive, neutral, negative]

    colors = ["palegreen", "orangered", "blue"]
    explode = (0.1, 0, 0)  # explode 1st slice

    #rcParams['figure.figsize'] = 8, 8
    #fig1, ax1 = plt.subplots()
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle = 270)

    plt.title('Percent of Sentiment Analysis of #Autism', size=20)
    plt.show()
    #data['Free'] = data['Type'].map(lambda s :1  if s =='Free' else 0)
    #data.drop(['Type'], axis=1, inplace=True)

    #x = sentiment_value
    #y = total_sentiment
    plt.plot(total_value, sentiment_value)
    plt.show()   



'''

sent = "I tested predator"

test = re.compile('.+ed')
test2 = test.findall(sent,re.I)

print(test2)
'''

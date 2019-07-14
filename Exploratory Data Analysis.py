import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns # used for plot interactive graph.
import os
import matplotlib.pyplot as plt
import plotly.offline as py
#py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import warnings
warnings.filterwarnings('ignore')
from pylab import rcParams
# figure size in inches
os.chdir('C:/Users/muham/Documents/CSC 3303_Big Data Analytics/Project')
#%matplotlib inline

data = pd.read_csv("googleplaystore.csv")
print(data.head())
print(data.shape)

#missing data
print("\n#--------Missing data------------#")
total = data.isnull().sum().sort_values(ascending=False)
percent = (data.isnull().sum()/data.isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
print(missing_data.head(6))

data.dropna(how ='any', inplace = True)

#After dropping missing data
total = data.isnull().sum().sort_values(ascending=False)
percent = (data.isnull().sum()/data.isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
print(missing_data.head(6))

print(data.shape)

rcParams['figure.figsize'] = 11.7,8.27
g = sns.kdeplot(data.Rating, color="Red", shade = True)
g.set_xlabel("Rating")
g.set_ylabel("Frequency")
plt.title('Distribution of Rating',size = 20)
plt.show()

#Category----------
print("\n#--------Category section------------#")
print( len(data['Category'].unique()) , "categories")

print("\n", data['Category'].unique())

g = sns.countplot(x="Category",data=data, palette = "Set1")
g.set_xticklabels(g.get_xticklabels(), rotation=90, ha="right")
g
plt.title('Count of app in each category',size = 20)
plt.show()

g = sns.catplot(x="Category",y="Rating",data=data, kind="box", height = 10 ,
palette = "Set1")
g.despine(left=True)
g.set_xticklabels(rotation=90)
g.set( xticks=range(0,34))
g = g.set_ylabels("Rating")
plt.title('Boxplot of Rating VS Category',size = 20)
plt.show()

print("\n#--------Reviews section------------#")
print(data['Reviews'].head())
# convert to int
data['Reviews'] = data['Reviews'].apply(lambda x: int(x))
# rating distibution
rcParams['figure.figsize'] = 11.7,8.27
g = sns.kdeplot(data.Reviews, color="Green", shade = True)
g.set_xlabel("Reviews")
g.set_ylabel("Frequency")
plt.title('Distribution of Review',size = 20)
plt.show()

print(data[data.Reviews > 5000000].head())

plt.figure(figsize = (10,10))
g = sns.jointplot(x="Reviews", y="Rating",color = 'orange', data=data,size = 8)
plt.show()

plt.figure(figsize = (10,10))
sns.regplot(x="Reviews", y="Rating", color = 'darkorange',data=data[data['Reviews']<1000000]);
plt.title('Rating VS Reveiws',size = 20)
plt.show()

print("\n#--------------Size-------------")
print(data['Size'].head())
print(data['Size'].unique())
print(len(data[data.Size == 'Varies with device']))
data['Size'].replace('Varies with device', np.nan, inplace = True )
data.Size = (data.Size.replace(r'[kM]+$', '', regex=True).astype(float) * \
             data.Size.str.extract(r'[\d\.]+([KM]+)', expand=False)
            .fillna(1)
            .replace(['k','M'], [10**3, 10**6]).astype(int))
data['Size'].fillna(data.groupby('Category')['Size'].transform('mean'),inplace = True)

print("\n#--------------Installs-------------")
print(data['Installs'].head())
print(data['Installs'].unique())
data.Installs = data.Installs.apply(lambda x: x.replace(',',''))
data.Installs = data.Installs.apply(lambda x: x.replace('+',''))
data.Installs = data.Installs.apply(lambda x: int(x))
print(data['Installs'].unique())
Sorted_value = sorted(list(data['Installs'].unique()))
data['Installs'].replace(Sorted_value,range(0,len(Sorted_value),1), inplace = True )
print(data['Installs'].head())
plt.figure(figsize = (10,10))
sns.regplot(x="Installs", y="Rating", color = 'teal',data=data);
plt.title('Rating VS Installs',size = 20)
plt.show()

print("\n#--------------Type-------------")
print(data['Type'].unique())
# Data to plot
labels = data['Type'].value_counts(sort=True).index
sizes = data['Type'].value_counts(sort=True)

colors = ["palegreen", "orangered"]
explode = (0.1, 0)  # explode 1st slice

rcParams['figure.figsize'] = 8, 8
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=270, )

plt.title('Percent of Free App in store', size=20)
plt.show()
data['Free'] = data['Type'].map(lambda s :1  if s =='Free' else 0)
data.drop(['Type'], axis=1, inplace=True)

print("\n#--------------Price-------------")
print(data['Price'].head())
print(data.Price.unique())
print(data['Price'].value_counts().head(30))
data.Price = data.Price.apply(lambda x: x.replace('$',''))
data['Price'] = data['Price'].apply(lambda x: float(x))
print(data['Price'].describe())
print(data[data['Price'] == 400])
plt.figure(figsize = (10,10))
sns.regplot(x="Price", y="Rating", color = 'darkorange',data=data[data['Reviews']<1000000]);
plt.title('Scatter plot Rating VS Price',size = 20)
plt.show()



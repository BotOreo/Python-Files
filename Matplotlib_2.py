import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates
import sklearn.cluster.dbscan_ as db


#dfmt = date format which takes the argument of %Y-%m-%d from the function call below
def texttodate(dfmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(dfmt)
    def bytesconverter(b):
        s=b.decode(encoding)
        return strconverter(s)
    return bytesconverter




def graph_data(stock):
    stock_price_URL='https://pythonprogramming.net/yahoo_finance_replacement'
    source_code=urllib.request.urlopen(stock_price_URL).read().decode()
    stock_data=[]
    split_source = source_code.split('\n')

    for line in split_source:
        split_line=line.split(',')
        if len(split_line) ==7:
            if 'Volume' not in line:
                stock_data.append(line)

    date,openp,higp,lowp,closep,adj_clp,volumep=np.loadtxt(stock_data,
                                                           delimiter=',',
                                                           unpack=True,
                                                           converters={0:texttodate('%Y-%m-%d')}
                                                           )

    plt.plot_date(date,closep,'-', label='Price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.show()

graph_data('TSLA')
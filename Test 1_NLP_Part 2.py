import re
import os

#Muhamad Arif Lutfi bin Aziz (1315791)
os.chdir('C:/Users/muham/Documents/CSC 4309_Natural Language Processing/')
text = open('log.xml','r')
readfile = text.readlines()

answer=dict()
#----------------All website in the vicinity-------------------
mac_acc=re.compile('([a-zA-z0-9]+::[a-zA-z0-9]+:[a-zA-z0-9]+:[a-zA-z0-9]+:[a-zA-z0-9]+%[0-9])')
mac_acc=(mac_acc.findall(str(readfile),re.I))
#print(mac_acc)
#----------------All email-------------
date_r=re.compile('[0-9]+-[0-9]+-[0-9]+')
date_r=(date_r.findall(str(readfile),re.I))
#print(date_r)

#----------------All phone-number-----------------
tel_f=re.compile('[0-9]+:[0-9]+:[0-9]+')
tel_f=(tel_f.findall(str(readfile),re.I))
#print

p = re.compile('(bad|arrogant)')

print('MAC Address :    ')
print(str(mac_acc[1]))
print('\nDate of access : ')
print(str(date_r[1]))
print('\nTime of Access :')
print(str(tel_f[1]))


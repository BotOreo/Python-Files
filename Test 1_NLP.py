import re
import os

#Muhamad Arif Lutfi bin Aziz (1315791)
#Tun Muhammad Zaim bin Aminuddin (1629501)
#os.chdir('C:/Users/muham/Documents/CSC 4309_Natural Language Processing/')
readfile = " impossible immature evacuated interim trimming showed education predator"
readfile=readfile.split('\s')

#----------------All website in the vicinity-------------------
web_f=re.compile('[ ]im[a-zA-Z]*')
web_f=(web_f.findall(str(readfile),re.I))
print(web_f)

web_f=re.compile('[a-zA-Z]+[ ]?ed[ ]')
web_f=(web_f.findall(str(readfile),re.I))
print(web_f)



import re
import os

#Muhamad Arif Lutfi bin Aziz (1315791)
#Tun Muhammad Zaim bin Aminuddin (1629501)
os.chdir('C:/Users/muham/Documents/CSC 4309_Natural Language Processing/')
text = open('clients.dat','r')
readfile = text.readlines()

#----------------All website in the vicinity-------------------
web_f=re.compile('(w{3}?[.][a-zA-Z]+[.][a-zA-Z]+|http://[a-zA-Z]+[.]?[a-zA-z]+[.]?[a-zA-Z]+[.]?[a-zA-Z]+)')
web_f=(web_f.findall(str(readfile),re.I))
print(web_f)
#----------------All email-------------
email_f=re.compile('[a-zA-Z]+@[a-zA-Z]+[.]?[a-zA-Z]*[.]?[a-z]+')
email_f=(email_f.findall(str(readfile),re.I))
print(email_f)

#----------------All phone-number-----------------
tel_f=re.compile('[+][0-9]+[ ]?[0-9]+[-][0-9]+[ ]?[0-9]+')
tel_f=(tel_f.findall(str(readfile),re.I))
print(tel_f)

with open('1315791_track.log','w') as file:
    file.write("Name : Muhamad Arif Lutfi (Matric no: 1315791)\n\n")
    file.write("%-40s" % "Company Website :" )
    file.write("%-40s" % "Email Address :")
    file.write("%-40s" % "Contact :")
    file.write("\n")

    for item in range(5):
        file.write("%-40s" % str(web_f[item]))
        file.write("%-40s" % str(email_f[item]))
        file.write("%-40s" % str(tel_f[item]))
        file.write("\n")



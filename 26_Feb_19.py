import re

text = "Advances in of Natural Language Processing and Machine " \
       "Learning are broadening the scope of what technology can do " \
       "in people’s everyday lives, and because of this, there is an " \
       "unprecedented number of people developing a curiosity in the fields. " \
       "And with the availability of educational content online, it has never been " \
       "easier to go from curiosity to proficiency." \
       "We gathered some of our favorite resources together so " \
       "you will have a jumping off point into studying these " \
       "fields on your own. Some of the resources here are suitable " \
       "for absolute beginners in either Natural Language Processing or " \
       "Machine Learning, and others are suitable for those with an " \
       "understanding of one who wish to learn more about the other."

#----------------All whole 'an' in the text----------------
an=re.compile(' an ')
print(an.findall(text,re.I))

#----------------All an in the vicinity-------------------
con_an=re.compile('([aA]n)')
print(con_an.findall(text,re.I))

#----------------All that starts with an or An-------------
start_an=re.compile('[ ][aA]n[a-zA-Z]*')
print(start_an.findall(text,re.I))

#----------------All that ends with an, An-----------------
end_an=re.compile('[a-zA-Z]*[aA]n[ ,.]')
print(end_an.findall(text,re.I))








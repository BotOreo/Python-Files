import re

x=re.match('[bcs]oil',"Boiling some water.",re.I)
print(x.group())
y=re.match("The","The boy eats another cake in the kitchen",re.I)
print(y.group())
w=re.search(r'[tT]he',"the boy eats another cake in the kitchen",re.I)
print(w.group())
z=re.findall(r'[tT]he',"The boy eats another cake in the kitchen",re.I)
#\b is for boudary
print(z)


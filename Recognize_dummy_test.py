# example that uses the nltk_contrib FST class
from nltk.nltk_contrib.fst.fst import *
import os

os.chdir('C:/Users/muham/Documents/CSC 4309_Natural Language Processing/')


class myFST(FST):
    def recognize(self, iput, oput):

        # insert your codes here
        # self.inp = iput.split()
        # self.outp = oput.split()
        print(f.add_arc('1', '2', ('co'), ('ko'))) # 1 -> 2 [a:1]
        self.inp = list(iput)
        self.outp = list(oput)
        # f.transduce("abc")

        if list(oput) == f.transduce(list(iput)):
            # print(" ".join(f.transduce(iput.split())))
            return True
        else:
            return False



f = myFST('example')

# first add the states in the FST
for i in range(1, 8):
    f.add_state(str(i))  # add states '1' .. '5'

print("English Word : ")
Eng_Org_W = input()

Eng_word = Eng_Org_W.replace(" ", "").lower()  # receive input from user
# print("Transliteration : ")
Jap_word = " "

# ------- dictionary Japanglish----------------
JE_Dict = dict()
JE = open('transliterate-Jap.dat', 'r')
listJE = JE.readlines()
for line in listJE:
    for word in line.split('\n'):
        a = 0
        for item in word.split('\t'):
            a = a + 1
            # print(a)
            # print(item)
            if a == 1:
                keys = item
            elif a == 2:
                value = item
                JE_Dict[keys] = value

# print(JE_Dict)

for keys, value in JE_Dict.items():  # total number in dictionary
    # print(keys, value)
    if Eng_word == keys.replace(" ", ""):
        # print("Tracing 1 : ")
        # print(keys)
        Jap_word = str(value)
        #  print("found")
        break
    # elif Eng_word!=keys:
    # print("Not found")

# print("Tracing 2 : ")
# print(Jap_word)

# Eng_word=Eng_word.split()
# add one initial state

f.initial_state = '1'  # -> 1
# transition 1 - 2 states
t=f.add_arc('1', '2', ('co'), ('ko'))  # 1 -> 2 [a:1]
t1=f.add_arc('1', '2', ('new'), ('nyu'))  # 1 -> 2 [a:1
f.add_arc('1', '2', ('bi'), ('bi'))  # 1 -> 2 [a:1
f.add_arc('1', '2', ('go'), ('go'))  # 1 -> 2 [a:1
f.add_arc('1', '2', ('te'), ('te'))  # 1 -> 2 [a:1
f.add_arc('1', '2', ('t'), ('tsu'))  # 1 -> 2 [a:1
f.add_arc('1', '2', ('vi'), ('bi'))  # 1 -> 2 [a:1
f.add_arc('1', '2', ('s'), ('su'))  # 1 -> 2 [a:1
f.add_arc('1', '2', ('e'), ('e'))  # 1 -> 2 [a:1
f.add_arc('1', '2', ('i'), ('ai'))  # 1 -> 2 [a:1
f.add_arc('1', '2', ('re'), ('re'))  # 1 -> 2 [a:1
f.add_arc('1', '2', ('ba'), ('bo'))  # 1 -> 2 [a:1
f.add_arc('1', '3', ('ba'), ('bi'))  # 1 -> 2 [a:1

# transition 2 - 3 states
f.add_arc('2', '3', ('m'), ('n'))  # 2 -> 3
f.add_arc('2', '3', ('kar'), ('ko'))  # 2 -> 3
f.add_arc('2', '3', ('yor'), ('yo'))  # 2 -> 3
f.add_arc('2', '3', ('ll'), ('ru'))  # 2 -> 3
f.add_arc('2', '3', ('l'), ('ru'))  # 2 -> 3
f.add_arc('2', '3', ('le'), ('re'))  # 2 -> 3
f.add_arc('2', '3', ('di'), ('ji'))  # 2 -> 3
f.add_arc('2', '3', ('win'), ('in'))  # 2 -> 3
f.add_arc('2', '3', ('de'), ('de'))  # 2 -> 3
f.add_arc('2', '3', ('s'), ('su'))  # 2 -> 3
f.add_arc('2', '3', ('to'), ('to'))  # 2 -> 3
f.add_arc('2', '3', ('le'), ('re'))  # 2 -> 3
f.add_arc('2', '3', ('ce'), ('su'))  # 2 -> 3
f.add_arc('2', '3', ('gate'), ('geit'))

# transition 3 - 4 states
f.add_arc('3', '4', ('pu'), ('pyu'))  # 3 -> 4 [a:1
f.add_arc('3', '5', ('ki'), ('ko'))  # 3 -> 4 [a:1
f.add_arc('3', '4', ('kir'), ('ko'))  # 3 -> 4 [a:1

f.add_arc('3', '4', ('k'), ('ku'))  # 3 -> 4 [a:1
f.add_arc('3', '4', ('gate'), ('geit'))  # 3 -> 4 [a:1
f.add_arc('3', '4', ('f'), ('hu'))  # 3 -> 4 [a:1
f.add_arc('3', '4', ('vi'), ('bi'))  # 3 -> 4 [a:1
f.add_arc('3', '4', ('o'), ('o'))  # 3 -> 4 [a:1
f.add_arc('3', '4', ('to'), ('ta'))  # 3 -> 4 [a:1
f.add_arc('3', '4', ('tau'), ('to'))  # 3 -> 4 [a:1
f.add_arc('3', '4', ('ry'), ('ri'))  # 1 -> 2 [a:1
f.add_arc('3', '4', ('va'), ('be'))  # 1 -> 2 [a:1
f.add_arc('3', '4', ('c'), ('ku'))  # 1 -> 2 [a:1

# transition 4 - 5 states
f.add_arc('4', '5', ('ter'), ('ta'))  # 4 -> 5[a:1
f.add_arc('4', '5', ('ah'), ('ra'))  # 4 -> 5[a:1
f.add_arc('4', '5', ('s'), ('su'))  # 4 -> 5[a:1
f.add_arc('4', '5', ('ba'), ('bo'))  # 4 -> 5[a:1
f.add_arc('4', '5', ('si'), ('ba'))  # 4 -> 5[a:1
f.add_arc('4', '5', ('wer'), ('wa'))  # 4 -> 5[a:1
f.add_arc('4', '5', ('ga'), ('ge'))  # 4 -> 5[a:1
f.add_arc('4', '5', ('rant'), ('ran'))  # 4 -> 5[a:1
f.add_arc('4', '5', ('rea'), ('ri'))  # 4 -> 5[a:1

# transition 5 - 5 states
f.add_arc('5', '6', ('ll'), ('ru'))  # 4 -> 5[a:1
f.add_arc('5', '1', ('rah'), ('ra'))  # 4 -> 5[a:1
f.add_arc('5', '6', ('me'), ('mu'))  # 4 -> 5[a:1
f.add_arc('5', '6', ('m'), ('mu'))  # 4 -> 5[a:1

# add final/accepting state(s)
f.set_final('2')
f.set_final('3')
f.set_final('4')
f.set_final('5')
f.set_final('6')

"""
for arc in f:
    for arc in state.arcs:
        print('{} -> {} / {}:{} / {}'.format(state.stateid,
                                             arc.nextstate,
                                             f.isyms.find(arc.ilabel),
                                             f.osyms.find(arc.olabel),
                                             arc.weight))
                                             
"""

#v=1
print(f._dst)
#print(t)
print(f.arc_info(t1))
'''
saveFile = open('Assignment 1 Mapping.dat', 'w')
for v in range(1,len(JE_Dict)):
    #print(v)
    a = str(''.join(f.in_string(arc="a%d"%v))+" ---> "+ ''.join(f.out_string(arc="a%d"%v)))
    saveFile.write(a)
    saveFile.write("\n")
    v+=1

saveFile.close()
'''
inp = Eng_word.replace(" ", "")

Jap_word_Org = Jap_word
outp = Jap_word.replace(" ", "")

# print(inp)

if f.recognize(inp, outp):
    print("English word: ")
    print(Eng_Org_W)
    print("Japanese word: ")
    print(Jap_word_Org)
    print("accept")
else:
    print("English word: ")
    print(Eng_Org_W)
    print("Japanese word: null")
    # print(outp)
    print("reject")

disp = FSTDisplay(f)
print("Enter x value : ")
x=input().isnumeric()

print("x is bigger than 5") if ( x > 5 ) else print("x is smaller than 5") # ternary conditional operators



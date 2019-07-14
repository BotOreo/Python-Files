# example that uses the nltk_contrib FST class
from nltk.nltk_contrib.fst.fst import *
import os
os.chdir('C:/Users/muham/Documents/CSC 4309_Natural Language Processing/')

class myFST(FST):    
    def recognize(self,iput,oput):

        # insert your codes here
        #self.inp = iput.split()
        #self.outp = oput.split()
        self.inp = list(iput)
        self.outp = list(oput)
        #f.transduce("abc")
        
        if list(oput) == f.transduce(list(iput)):
            #print(" ".join(f.transduce(iput.split())))        
            return True
        else:
            return False

# you can define an FST either this way:
#f = myFST.parse("example", """
#-> 1
#1 -> 2 [a:1]
#2 -> 2 [a:0]
#2 -> 2 [b:1]
#2 -> 3 [:1]
#3 -> 4 [b:1]
#4 -> 5 [b:]
#5 ->
#""")

# or this more verbose way
f = myFST('example')
# first add the states in the FST
for i in range(1,9):
    f.add_state(str(i)) # add states '1' .. '5'

Eng_word=" "

while Eng_word in Eng_word!="end":
    print("\nEnglish Word : ")
    Eng_Org_W = input()
    Eng_word=Eng_Org_W.replace(" ","").lower()  #receive input from user
    #print("Transliteration : ")
    Jap_word =" "

    #------- dictionary Japanglish----------------
    JE_Dict = dict()
    JE = open('transliterate-Jap.dat','r')
    listJE=JE.readlines()
    for line in listJE:
        for word in line.split('\n'):
            a = 0
            for item in word.split('\t'):
                a=a+1
               # print(a)
                #print(item)
                if a==1:
                    keys=item
                elif a==2:
                    value=item
                    JE_Dict[keys]=value
                   

    #print(JE_Dict)

    for keys, value in JE_Dict.items(): #total number in dictionary
        #print(keys, value)
        if Eng_word==keys.replace(" ",""):
            #print("Tracing 1 : ")
            #print(keys)
            Jap_word = str(value)
          #  print("found")
            break
        #elif Eng_word!=keys:
            #print("Not found")



    #print("Tracing 2 : ")
    #print(Jap_word)

    #Eng_word=Eng_word.split()
    # add one initial state

    f.initial_state = '1' # -> 1
    # transition 1 - 2 states
    #f.add_arc()
    f.add_arc('1', '2', ('co') ,('ko')) # 1 -> 2 [a:1]
    f.add_arc('1', '2', ('new') ,('nyu')) # 1 -> 2 [a:1
    f.add_arc('1', '2', ('bi') ,('bi')) # 1 -> 2 [a:1
    f.add_arc('1', '2', ('go') ,('go')) # 1 -> 2 [a:1
    f.add_arc('1', '2', ('te') ,('te')) # 1 -> 2 [a:1   #
    f.add_arc('1', '2', ('vi') ,('bi')) # 1 -> 2 [a:1
    f.add_arc('1', '2', ('sa') ,('sa')) # 1 -> 2 [a:1
    f.add_arc('1', '2', ('s') ,('su')) # 1 -> 2 [a:1
    f.add_arc('1', '2', ('e') ,('e')) # 1 -> 2 [a:1
    f.add_arc('1', '2', ('i') ,('ai')) # 1 -> 2 [a:1
    f.add_arc('1', '2', ('re') ,('re')) # 1 -> 2 [a:1
    f.add_arc('1', '2', ('ba') ,('bo')) # 1 -> 2 [a:1
    f.add_arc('1', '2', ('cof') ,('ko')) # 1 -> 2 [a:1
    f.add_arc('1', '2', ('mi') ,('mi')) # 1 -> 2 [a:1
    f.add_arc('1', '2', ('to') ,('to')) # 1 -> 2 [a:1
    f.add_arc('1', '2', ('g') ,('gu')) # 1 -> 2 [a:1        #
    f.add_arc('1', '2', ('mai') ,('me')) # 1 -> 2 [a:1
    f.add_arc('1', '2', ('pe') ,('pet')) # 1 -> 2 [a:1
    f.add_arc('1', '2', ('ro') ,('ro')) # 1 -> 2 [a:1
    f.add_arc('1', '2', ('ta') ,('ta')) # 1 -> 2 [a:1   
    f.add_arc('1', '2', ('cou') ,('ku')) # 1 -> 2 [a:1
    f.add_arc('1', '2', ('bo') ,('bo')) # 1 -> 2 [a:1       #
    f.add_arc('1', '2', ('a') ,('a')) # 1 -> 2 [a:1
    f.add_arc('1', '2', ('bu') ,('ba')) # 1 -> 2 [a:1
    f.add_arc('1', '2', ('in') ,('in')) # 1 -> 2 [a:1
    f.add_arc('1', '2', ('ca') ,('ka')) # 1 -> 2 [a:1
    f.add_arc('1', '2', ('b') ,('ba')) # 1 -> 2 [a:1
    f.add_arc('1', '2', ('su') ,('su')) # 1 -> 2 [a:1
    f.add_arc('1', '2', ('but') ,('ba')) # 1 -> 2 [a:1
    f.add_arc('1', '2', ('chic') ,('chi')) # 1 -> 2 [a:1
    f.add_arc('1', '2', ('des') ,('de')) # 1 -> 2 [a:1
    f.add_arc('1', '2', ('jui') ,('ju')) # 1 -> 2 [a:1
    f.add_arc('1', '2', ('kit') ,('ki')) # 1 -> 2 [a:1
    f.add_arc('1', '2', ('me') ,('me')) # 1 -> 2 [a:1
    f.add_arc('1', '2', ('sau') ,('so')) # 1 -> 2 [a:1
    f.add_arc('1', '2', ('f') ,('fu')) # 1 -> 2 [a:1
    f.add_arc('1', '2', ('ha') ,('ha')) # 1 -> 2 [a:1
    f.add_arc('1', '2', ('so') ,('so')) # 1 -> 2 [a:1
    f.add_arc('1', '2', ('pa') ,('pa')) # 1 -> 2 [a:1
    f.add_arc('1', '2', ('per') ,('pa')) # 1 -> 2 [a:1
    f.add_arc('1', '2', ('d') ,('do')) # 1 -> 2 [a:1
    f.add_arc('1', '2', ('mo') ,('mo')) # 1 -> 2 [a:1
    f.add_arc('1', '2', ('hoc') ,('ho')) # 1 -> 2 [a:1
    f.add_arc('1', '2', ('ma') ,('ma')) # 1 -> 2 [a:1
    f.add_arc('1', '2', ('ru') ,('ra')) # 1 -> 2 [a:1
    f.add_arc('1', '2', ('soc') ,('sa')) # 1 -> 2 [a:1
    f.add_arc('1', '2', ('hu') ,('ha')) # 1 -> 2 [a:1
    f.add_arc('1', '2', ('t') ,('to')) # 1 -> 2 [a:1
    f.add_arc('1', '2', ('ra') ,('ra')) # 1 -> 2 [a:1
    f.add_arc('1', '2', ('to') ,('to')) # 1 -> 2 [a:1   #
    
    
    #Special Character
    f.add_arc('1', '3', ('t') ,('tsu')) # 1 -> 2 [a:1
    f.add_arc('1', '3', ('e') ,('i')) # 1 -> 2 [a:1
    f.add_arc('1', '3', ('ba') ,('bo')) # 1 -> 2 [a:1
    f.add_arc('1', '3', ('bee') ,('bi')) # 1 -> 2 [a:1
    f.add_arc('1', '3', ('ma') ,('mi')) # 1 -> 2 [a:1       #
    f.add_arc('1', '3', ('ca') ,('ke')) # 1 -> 2 [a:1
    f.add_arc('1', '4', ('ca') ,('ki')) # 1 -> 2 [a:1   #
     
    # transition 2 - 3 states
    f.add_arc('2', '3', ('m') ,('n')) # 2 -> 3
    f.add_arc('2', '3', ('yor') ,('yo')) # 2 -> 3
    f.add_arc('2', '3', ('ll') ,('ru')) # 2 -> 3
    f.add_arc('2', '3', ('l') ,('ru')) # 2 -> 3
    f.add_arc('2', '3', ('le') ,('re')) # 2 -> 3
    f.add_arc('2', '3', ('di') ,('ji')) # 2 -> 3
    f.add_arc('2', '3', ('de') ,('de')) # 2 -> 3
    f.add_arc('2', '3', ('s') ,('su')) # 2 -> 3
    f.add_arc('2', '3', ('to') ,('to')) # 2 -> 3
    f.add_arc('2', '3', ('ce') ,('su')) # 2 -> 3
    f.add_arc('2', '3', ('gate') ,('geit'))
    f.add_arc('2', '3', ('fee') ,('hi')) # 2 -> 3
    f.add_arc('2', '3', ('s') ,('su')) # 2 -> 3
    f.add_arc('2', '3', ('lon') ,('ron')) # 2 -> 3      #recheck
    f.add_arc('2', '3', ('i') ,('i')) # 2 -> 3       #
    f.add_arc('2', '3', ('t') ,('to')) # 2 -> 3
    f.add_arc('2', '3', ('ma') ,('ma')) # 2 -> 3
    f.add_arc('2', '3', ('rou') ,('ra')) # 2 -> 3
    f.add_arc('2', '3', ('po') ,('po')) # 2 -> 3
    f.add_arc('2', '3', ('f') ,('fu')) # 2 -> 3
    f.add_arc('2', '3', ('me') ,('me')) # 2 -> 3
    f.add_arc('2', '3', ('x') ,('ku')) # 2 -> 3
    f.add_arc('2', '3', ('per') ,('pa')) # 2 -> 3
    f.add_arc('2', '3', ('ter') ,('ta')) # 2 -> 3
    f.add_arc('2', '3', ('ken') ,('kin')) # 2 -> 3
    f.add_arc('2', '3', ('ser') ,('za')) # 2 -> 3
    f.add_arc('2', '3', ('ke') ,('ki')) # 2 -> 3
    f.add_arc('2', '3', ('che') ,('chi')) # 2 -> 3
    f.add_arc('2', '3', ('b') ,('ya')) # 2 -> 3
    f.add_arc('2', '3', ('n') ,('n')) # 2 -> 3
    f.add_arc('2', '3', ('sa') ,('se')) # 2 -> 3
    f.add_arc('2', '3', ('r') ,('ra')) # 2 -> 3
    f.add_arc('2', '3', ('rai') ,('re')) # 2 -> 3
    f.add_arc('2', '3', ('ree') ,('ri')) # 2 -> 3
    f.add_arc('2', '3', ('ra') ,('ra')) # 2 -> 3
    f.add_arc('2', '3', ('ni') ,('ni')) # 2 -> 3
    f.add_arc('2', '3', ('g') ,('gu')) # 2 -> 3
    f.add_arc('2', '3', ('cer') ,('ka')) # 2 -> 3
    f.add_arc('2', '3', ('ll') ,('ru')) # 2 -> 3
    f.add_arc('2', '3', ('cy') ,('shu')) # 2 -> 3
    f.add_arc('2', '3', ('key') ,('ke')) # 2 -> 3
       
    #Special Character
    f.add_arc('2', '4', ('la') ,('ra')) # 2 -> 3        #
    f.add_arc('2', '4', ('lo') ,('ro')) # 2 -> 3

    
    # transition 3 - 4 states
    f.add_arc('3', '4', ('win') ,('in')) # 2 -> 3
    f.add_arc('3', '4', ('pu') ,('pyu')) # 3 -> 4 [a:1
    f.add_arc('3', '4', ('k') ,('ku')) # 3 -> 4 [a:1
    f.add_arc('3', '4', ('gate') ,('geit')) # 3 -> 4 [a:1
    f.add_arc('3', '4', ('f') ,('hu')) # 3 -> 4 [a:1
    f.add_arc('3', '4', ('vi') ,('bi')) # 3 -> 4 [a:1   #
    f.add_arc('3', '4', ('o') ,('o')) # 3 -> 4 [a:1
    f.add_arc('3', '4', ('tau') ,('to')) # 3 -> 4 [a:1
    f.add_arc('3', '4', ('ry') ,('ri')) # 1 -> 2 [a:1
    f.add_arc('3', '4', ('va') ,('be')) # 1 -> 2 [a:1
    f.add_arc('3', '4', ('c') ,('ku')) # 1 -> 2 [a:1
    f.add_arc('3', '4', ('ca') ,('ka')) # 1 -> 2 [a:1
    f.add_arc('3', '4', ('s') ,('sa')) # 1 -> 2 [a:1
    f.add_arc('3', '4', ('n') ,('n')) # 1 -> 2 [a:1
    f.add_arc('3', '4', ('b') ,('bu')) # 1 -> 2 [a:1
    f.add_arc('3', '4', ('me') ,('mu')) # 1 -> 2 [a:1
    f.add_arc('3', '4', ('le') ,('ru')) # 1 -> 2 [a:1       #
    f.add_arc('3', '4', ('pha') ,('fa')) # 1 -> 2 [a:1
    f.add_arc('3', '4', ('lu') ,('ru')) # 1 -> 2 [a:1
    f.add_arc('3', '4', ('ra') ,('ra')) # 1 -> 2 [a:1
    f.add_arc('3', '4', ('i') ,('shi')) # 1 -> 2 [a:1
    f.add_arc('3', '4', ('ke') ,('ku')) # 1 -> 2 [a:1
    f.add_arc('3', '4', ('ne') ,('n')) # 1 -> 2 [a:1
    f.add_arc('3', '4', ('la') ,('re')) # 1 -> 2 [a:1
    f.add_arc('3', '4', ('t') ,('to')) # 1 -> 2 [a:1    #
    f.add_arc('3', '4', ('ba') ,('be')) # 1 -> 2 [a:1
    f.add_arc('3', '4', ('u') ,('yu')) # 1 -> 2 [a:1
    f.add_arc('3', '4', ('ge') ,('ji')) # 1 -> 2 [a:1
    f.add_arc('3', '4', ('ri') ,('ri')) # 1 -> 2 [a:1
    f.add_arc('3', '4', ('ie') ,('i')) # 1 -> 2 [a:1
    f.add_arc('3', '4', ('bur') ,('ba')) # 1 -> 2 [a:1
    f.add_arc('3', '4', ('ts') ,('tsu')) # 1 -> 2 [a:1
    f.add_arc('3', '4', ('ner') ,('na')) # 1 -> 2 [a:1
    f.add_arc('3', '4', ('ne') ,('ne')) # 1 -> 2 [a:1
    f.add_arc('3', '4', ('ma') ,('ma')) # 1 -> 2 [a:1
    f.add_arc('3', '4', ('ta') ,('ta')) # 1 -> 2 [a:1
    f.add_arc('3', '4', ('tho') ,('so')) # 1 -> 2 [a:1
    f.add_arc('3', '4', ('by') ,('bi')) # 1 -> 2 [a:1
    f.add_arc('3', '4', ('tle') ,('ru')) # 1 -> 2 [a:1
    f.add_arc('3', '4', ('d') ,('do')) # 1 -> 2 [a:1
    f.add_arc('3', '4', ('to') ,('ta')) # 1 -> 2 [a:1

    #Special Character
    f.add_arc('3', '5', ('d') ,('da')) # 1 -> 2 [a:1
    f.add_arc('3', '4', ('ar') ,('ya')) # 2 -> 3    #
    f.add_arc('3', '5', ('le') ,('ret')) # 1 -> 2 [a:1      #
    f.add_arc('3', '4', ('point') ,('')) # 1 -> 2 [a:1      #
    f.add_arc('3', '4', ('r') ,('ru')) # 2 -> 3
    f.add_arc('3', '4', ('chi') ,('shi')) # 2 -> 3
    f.add_arc('4', '5', ('rie') ,('ri')) # 1 -> 2 [a:1
    f.add_arc('3', '4', ('ke') ,('ki')) # 2 -> 3
    

    # transition 4 - 5 states
    f.add_arc('4', '5', ('ter') ,('ta')) # 4 -> 5[a:1
    #print("Arc 1 : ")
    #print(f.arcs(1))
    f.add_arc('4', '5', ('s') ,('su')) # 4 -> 5[a:1      #
    f.add_arc('4', '5', ('ba') ,('bo')) # 4 -> 5[a:1
    f.add_arc('4', '5', ('si') ,('ba')) # 4 -> 5[a:1    #
    f.add_arc('4', '5', ('pen') ,('pen')) # 1 -> 2 [a
    f.add_arc('4', '5', ('ga') ,('ge')) # 4 -> 5[a:1
    f.add_arc('4', '5', ('rant') ,('ran')) # 4 -> 5[a:1
    f.add_arc('4', '5', ('rea') ,('ri')) # 4 -> 5[a:1
    f.add_arc('4', '5', ('la') ,('re')) # 4 -> 5[a:1
    f.add_arc('4', '5', ('t') ,('to')) # 4 -> 5[a:1
    f.add_arc('4', '5', ('ti') ,('chi')) # 4 -> 5[a:1
    f.add_arc('4', '5', ('le') ,('ru')) # 4 -> 5[a:1
    f.add_arc('4', '5', ('s') ,('su')) # 4 -> 5[a:1
    f.add_arc('4', '5', ('be') ,('be')) # 4 -> 5[a:1
    f.add_arc('4', '5', ('e') ,('e')) # 4 -> 5[a:1
    f.add_arc('4', '5', ('ge') ,('tsu')) # 4 -> 5[a:1
    f.add_arc('4', '5', ('wi') ,('i')) # 4 -> 5[a:1
    f.add_arc('4', '5', ('ca') ,('ka')) # 4 -> 5[a:1
    f.add_arc('4', '5', ('ger') ,('gu')) # 4 -> 5[a:1
    f.add_arc('4', '5', ('c') ,('ku')) # 4 -> 5[a:1
    f.add_arc('4', '5', ('i') ,('i')) # 4 -> 5[a:1
    f.add_arc('4', '5', ('n') ,('n')) # 4 -> 5[a:1
    f.add_arc('4', '5', ('ri') ,('ri')) # 4 -> 5[a:1
    f.add_arc('4', '5', ('te') ,('to')) # 4 -> 5[a:1
    f.add_arc('4', '5', ('d') ,('do')) # 4 -> 5[a:1
    f.add_arc('4', '5', ('to') ,('ta')) # 3 -> 4 [a:1
    f.add_arc('4', '5', ('tor') ,('ta')) # 3 -> 4 [a:1

    #Special Character
    f.add_arc('4', '5', ('phone') ,('hon')) # 1 -> 2 [a:1       #recheck
    f.add_arc('4', '5', ('ss') ,('su')) # 1 -> 2 [a:1   #
    f.add_arc('4', '5', ('ne') ,('n')) # 4 -> 5[a:1
    f.add_arc('4', '5', ('b') ,('ya')) # 2 -> 3
    
    # transition 5 - 6 states
    f.add_arc('5', '6', ('ll') ,('ru')) # 4 -> 5[a:1
    f.add_arc('5', '6', ('me') ,('mu')) # 4 -> 5[a:1
    f.add_arc('5', '6', ('m') ,('mu')) # 4 -> 5[a:1
    f.add_arc('5', '6', ('tor') ,('ta')) # 4 -> 5[a:1
    f.add_arc('5', '6', ('c') ,('ku')) # 4 -> 5[a:1
    f.add_arc('5', '6', ('li') ,('ri')) # 4 -> 5[a:1
    f.add_arc('5', '6', ('t') ,('to')) # 4 -> 5[a:1
    f.add_arc('5', '6', ('n') ,('n')) # 4 -> 5[a:1
    f.add_arc('5', '6', ('ch') ,('chi')) # 4 -> 5[a:1
    f.add_arc('5', '6', ('po') ,('po')) # 4 -> 5[a:1
    f.add_arc('5', '6', ('rea') ,('ri')) # 4 -> 5[a:1
    f.add_arc('5', '6', ('ze') ,('zu')) # 4 -> 5[a:1
    f.add_arc('5', '6', ('wer') ,('wa')) # 4 -> 5[a:1
    #Special Character
    f.add_arc('5', '6', ('o') ,('n')) # 4 -> 5[a:1
    f.add_arc('5', '6', ('t') ,('to')) # 3 -> 4 [a:1
    f.add_arc('5', '6', ('ba') ,('be')) # 1 -> 2 [a:1
    # transition 6 - 7 states
    f.add_arc('6', '7', ('p') ,('pu')) # 4 -> 5[a:1
    f.add_arc('6', '7', ('za') ,('za')) # 4 -> 5[a:1
    f.add_arc('6', '7', ('do') ,('do')) # 4 -> 5[a:1
    f.add_arc('6', '7', ('ta') ,('te')) # 4 -> 5[a:1
    f.add_arc('6', '7', ('m') ,('mu')) # 4 -> 5[a:1
    f.add_arc('6', '7', ('g') ,('gu')) # 4 -> 5[a:1
    #Special Character
    f.add_arc('6', '7', ('n') ,('gu')) # 4 -> 5[a:1
    f.add_arc('6', '7', ('ge') ,('tsu')) # 4 -> 5[a:1

    # transition 7 - 8 states
    f.add_arc('7', '8', ('g') ,('gu')) # 4 -> 5[a:1
    f.add_arc('7', '8', ('to') ,('to')) # 4 -> 5[a:1

    # add final/accepting state(s)
    f.set_final('2')
    f.set_final('3')
    f.set_final('4')
    f.set_final('5')
    f.set_final('6')
    f.set_final('7')
    f.set_final('8')

    #print("Tracing 3 : ")
    #print(Jap_word)
    #print(f._dst) # check destination and address of arc

    saveFile = open('Assignment 1 Mapping.dat', 'w')
    for v in range(1, len(f._dst)+1):
        # print(v)
        a = str(''.join(f.in_string(arc="a%d" % v)) + " ---> " + ''.join(f.out_string(arc="a%d" % v)))
        saveFile.write(a)
        saveFile.write("\n")
        v += 1

    saveFile.close()
    inp = Eng_word.replace(" ","")
    Jap_word_Org = Jap_word
    outp = Jap_word.replace(" ","")

    #print(inp)

    if f.recognize(inp, outp):
        print("English word: ")
        print(Eng_Org_W)
        print("Japanese word: ")
        print(Jap_word_Org)
        print("accept")
    else:
        if Eng_Org_W=="end":
            print("Program ended!")
            break
        print("English word: ")
        print(Eng_Org_W)
        print("Japanese word: null")
        #print(outp)
        print("reject")

disp = FSTDisplay(f)        #to show the arc

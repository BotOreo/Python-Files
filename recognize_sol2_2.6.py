#Muhammad Arif Lutfi Bin Aziz       1315791
#Tun Muhammad Zaim Bin Aminuddin    1629501
#Mohd Faris Fitri Bin Mohd Hanafi   1614839
#Muhammad Zharif Bin Msduki         1611777

from nltk.nltk_contrib.fst.fst import *
import os
os.chdir('C:/Users/muham/Documents/CSC 4309_Natural Language Processing/')     #This is for local machine directory change

class myFST(FST):    
    def recognize(self,iput,oput):
        self.inp = list(iput)
        self.outp = list(oput)
       
        
        if list(oput) == f.transduce(list(iput)):       
            return True
        else:
            return False

f = myFST('example')
# first add the states in the FST
for i in range(1,10):
    f.add_state(str(i)) 

Eng_word=" "
y = 0
while Eng_word in Eng_word!="end":
    print("\nEnglish Word : ")
    Eng_Org_W = input()                             #receive input from user
    Eng_word=Eng_Org_W.replace(" ","").lower()  
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
                if a==1:
                    keys=item
                elif a==2:
                    value=item
                    JE_Dict[keys]=value
                   
    for keys, value in JE_Dict.items(): #total number in dictionary
        if Eng_word==keys.replace(" ",""):
            Jap_word = str(value)
            break
    
    f.initial_state = '1'

    # transition 1 - 2 states
    f.add_arc('1', '2', ('co') ,('ko')) 
    f.add_arc('1', '2', ('new') ,('nyu')) 
    f.add_arc('1', '2', ('bi') ,('bi')) 
    f.add_arc('1', '2', ('go') ,('go')) 
    f.add_arc('1', '2', ('te') ,('te'))   
    f.add_arc('1', '2', ('vi') ,('bi')) 
    f.add_arc('1', '2', ('sa') ,('sa')) 
    f.add_arc('1', '2', ('s') ,('su')) 
    f.add_arc('1', '2', ('e') ,('e')) 
    f.add_arc('1', '2', ('i') ,('ai')) 
    f.add_arc('1', '2', ('re') ,('re')) 
    f.add_arc('1', '2', ('ba') ,('bo')) 
    f.add_arc('1', '2', ('cof') ,('ko')) 
    f.add_arc('1', '2', ('mi') ,('mi')) 
    f.add_arc('1', '2', ('to') ,('to')) 
        
    f.add_arc('1', '2', ('mai') ,('me')) 
    f.add_arc('1', '2', ('pe') ,('pet')) 
    f.add_arc('1', '2', ('ro') ,('ro')) 
    f.add_arc('1', '2', ('ta') ,('ta'))    
    f.add_arc('1', '2', ('cou') ,('ku')) 
    f.add_arc('1', '2', ('bo') ,('bo')) 
    f.add_arc('1', '2', ('a') ,('a')) 
    f.add_arc('1', '2', ('bu') ,('ba')) 
    f.add_arc('1', '2', ('in') ,('in')) 
    f.add_arc('1', '2', ('ca') ,('ka')) 
    
    f.add_arc('1', '2', ('su') ,('su')) 
    f.add_arc('1', '2', ('but') ,('ba')) 
    f.add_arc('1', '2', ('chic') ,('chi')) 
    f.add_arc('1', '2', ('des') ,('de')) 
    f.add_arc('1', '2', ('jui') ,('ju')) 
    f.add_arc('1', '2', ('kit') ,('ki')) 
    f.add_arc('1', '2', ('me') ,('me')) 
    f.add_arc('1', '2', ('sau') ,('so'))
    f.add_arc('1', '2', ('f') ,('fu')) 
    f.add_arc('1', '2', ('ha') ,('ha')) 
    f.add_arc('1', '2', ('so') ,('so')) 
    f.add_arc('1', '2', ('pa') ,('pa')) 
    f.add_arc('1', '2', ('per') ,('pa')) 
    f.add_arc('1', '2', ('d') ,('do')) 
    f.add_arc('1', '2', ('mo') ,('mo')) 
    f.add_arc('1', '2', ('hoc') ,('ho'))
    f.add_arc('1', '2', ('ma') ,('ma')) 
    f.add_arc('1', '2', ('ru') ,('ra')) 
    f.add_arc('1', '2', ('soc') ,('sa')) 
    f.add_arc('1', '2', ('hu') ,('ha')) 
    f.add_arc('1', '2', ('t') ,('to')) 
    f.add_arc('1', '2', ('ra') ,('ra')) 
    f.add_arc('1', '2', ('to') ,('to'))
    
    
    #Special Character
    f.add_arc('1', '3', ('t') ,('tsu')) 
    f.add_arc('1', '3', ('e') ,('i')) 
    f.add_arc('1', '3', ('ba') ,('bo')) 
    f.add_arc('1', '3', ('bee') ,('bi')) 
    f.add_arc('1', '3', ('ma') ,('mi')) 
    f.add_arc('1', '3', ('ca') ,('ke')) 
    f.add_arc('1', '4', ('ca') ,('ki'))
    f.add_arc('1', '3', ('g') ,('gu'))
    f.add_arc('1', '4', ('b') ,('ba'))
    f.add_arc('1', '4', ('t') ,('ta'))
    f.add_arc('1', '3', ('cho') ,('cho'))
     
    # transition 2 - 3 states
    f.add_arc('2', '3', ('m') ,('n')) 
    f.add_arc('2', '3', ('yor') ,('yo'))
    f.add_arc('2', '3', ('ll') ,('ru')) 
    f.add_arc('2', '3', ('l') ,('ru')) 
    f.add_arc('2', '3', ('le') ,('re')) 
    f.add_arc('2', '3', ('di') ,('ji')) 
    f.add_arc('2', '3', ('de') ,('de')) 
    f.add_arc('2', '3', ('s') ,('su')) 
    f.add_arc('2', '3', ('to') ,('to')) 
    f.add_arc('2', '3', ('ce') ,('su')) 
    f.add_arc('2', '3', ('gate') ,('geit'))
    f.add_arc('2', '3', ('fee') ,('hi')) 
    f.add_arc('2', '3', ('s') ,('su')) 
    f.add_arc('2', '3', ('i') ,('i')) 
    f.add_arc('2', '3', ('t') ,('to')) 
    f.add_arc('2', '3', ('ma') ,('ma')) 
    f.add_arc('2', '3', ('rou') ,('ra')) 
    f.add_arc('2', '3', ('po') ,('po')) 
    f.add_arc('2', '3', ('f') ,('fu')) 
    f.add_arc('2', '3', ('me') ,('me'))
    f.add_arc('2', '3', ('x') ,('ku')) 
    f.add_arc('2', '3', ('per') ,('pa')) 
    f.add_arc('2', '3', ('ter') ,('ta')) 
    f.add_arc('2', '3', ('ken') ,('kin')) 
    f.add_arc('2', '3', ('ser') ,('za')) 
    f.add_arc('2', '3', ('ke') ,('ki')) 
    f.add_arc('2', '3', ('che') ,('chi')) 
    f.add_arc('2', '3', ('b') ,('ya')) 
    f.add_arc('2', '3', ('n') ,('n')) 
    f.add_arc('2', '3', ('sa') ,('se')) 
    f.add_arc('2', '3', ('r') ,('ra')) 
    f.add_arc('2', '3', ('rai') ,('re')) 
    f.add_arc('2', '3', ('ree') ,('ri')) 
    f.add_arc('2', '3', ('ra') ,('ra')) 
    f.add_arc('2', '3', ('ni') ,('ni')) 
    f.add_arc('2', '3', ('g') ,('gu')) 
    f.add_arc('2', '3', ('cer') ,('ka')) 
    f.add_arc('2', '3', ('ll') ,('ru')) 
    f.add_arc('2', '3', ('cy') ,('shu')) 
    f.add_arc('2', '3', ('key') ,('ke'))
    
       
    #Special Character
    f.add_arc('2', '5', ('la') ,('ra')) 
    f.add_arc('2', '4', ('lo') ,('ro')) 

    
    # transition 3 - 4 states
    f.add_arc('3', '4', ('win') ,('in')) 
    f.add_arc('3', '4', ('pu') ,('pyu')) 
    f.add_arc('3', '4', ('k') ,('ku'))          
    f.add_arc('3', '4', ('gate') ,('geit')) 
    f.add_arc('3', '4', ('f') ,('hu')) 
    f.add_arc('3', '4', ('vi') ,('bi')) 
    f.add_arc('3', '4', ('o') ,('o')) 
    f.add_arc('3', '4', ('tau') ,('to')) 
    f.add_arc('3', '4', ('ry') ,('ri')) 
    f.add_arc('3', '4', ('va') ,('be')) 
    f.add_arc('3', '4', ('c') ,('ku')) 
    f.add_arc('3', '4', ('ca') ,('ka')) 
    f.add_arc('3', '4', ('s') ,('sa')) 
    f.add_arc('3', '4', ('n') ,('n')) 
    f.add_arc('3', '4', ('b') ,('bu')) 
    f.add_arc('3', '4', ('me') ,('mu')) 
    f.add_arc('3', '4', ('le') ,('ru'))
    f.add_arc('3', '4', ('pha') ,('fa')) 
    f.add_arc('3', '4', ('lu') ,('ru')) 
    f.add_arc('3', '4', ('ra') ,('ra')) 
    f.add_arc('3', '4', ('i') ,('shi')) 
    
    f.add_arc('3', '4', ('ne') ,('n')) 
    f.add_arc('3', '4', ('la') ,('re')) 
    f.add_arc('3', '4', ('t') ,('to')) 
    f.add_arc('3', '4', ('ba') ,('be')) 
    f.add_arc('3', '4', ('u') ,('yu')) 
    f.add_arc('3', '4', ('ge') ,('ji')) 
    f.add_arc('3', '4', ('ri') ,('ri')) 
    f.add_arc('3', '4', ('ie') ,('i')) 
    f.add_arc('3', '4', ('bur') ,('ba')) 
    f.add_arc('3', '4', ('ts') ,('tsu')) 
    f.add_arc('3', '4', ('ner') ,('na')) 
    f.add_arc('3', '4', ('ne') ,('ne')) 
    f.add_arc('3', '4', ('ma') ,('ma')) 
    f.add_arc('3', '4', ('ta') ,('ta')) 
    f.add_arc('3', '4', ('tho') ,('so')) 
    f.add_arc('3', '4', ('by') ,('bi')) 
    f.add_arc('3', '4', ('tle') ,('ru')) 
    f.add_arc('3', '4', ('d') ,('do')) 
    f.add_arc('3', '4', ('to') ,('ta')) 

    #Special Character
    f.add_arc('3', '5', ('d') ,('da')) 
    f.add_arc('3', '4', ('ar') ,('ya')) 
    f.add_arc('3', '5', ('le') ,('ret')) 
    f.add_arc('3', '4', ('point') ,('')) 
    f.add_arc('3', '4', ('r') ,('ru')) 
    f.add_arc('3', '4', ('chi') ,('shi')) 
    f.add_arc('3', '4', ('ke') ,('ki'))         
    f.add_arc('3', '4', ('la') ,('ra'))
    f.add_arc('3', '4', ('co') ,('ko'))
      
    

    # transition 4 - 5 states
    f.add_arc('4', '5', ('ter') ,('ta')) 
    f.add_arc('4', '5', ('s') ,('su')) 
    f.add_arc('4', '5', ('ba') ,('bo')) 
    f.add_arc('4', '5', ('si') ,('ba')) 
    f.add_arc('4', '5', ('pen') ,('pen')) 
    f.add_arc('4', '5', ('ga') ,('ge')) 
    f.add_arc('4', '5', ('rant') ,('ran')) 
    f.add_arc('4', '5', ('rea') ,('ri')) 
    f.add_arc('4', '5', ('la') ,('re')) 
    f.add_arc('4', '5', ('t') ,('to')) 
    f.add_arc('4', '5', ('ti') ,('chi')) 
    f.add_arc('4', '5', ('le') ,('ru')) 
    f.add_arc('4', '5', ('be') ,('be')) 
    f.add_arc('4', '5', ('e') ,('e')) 
    f.add_arc('4', '5', ('ge') ,('tsu')) 
    f.add_arc('4', '5', ('wi') ,('i')) 
    f.add_arc('4', '5', ('ca') ,('ka')) 
    f.add_arc('4', '5', ('ger') ,('gu')) 
    f.add_arc('4', '5', ('c') ,('ku')) 
    f.add_arc('4', '5', ('i') ,('i')) 
    f.add_arc('4', '5', ('n') ,('n')) 
    f.add_arc('4', '5', ('ri') ,('ri')) 
    f.add_arc('4', '5', ('te') ,('to')) 
    f.add_arc('4', '5', ('d') ,('do')) 
    f.add_arc('4', '5', ('to') ,('ta')) 
    f.add_arc('4', '5', ('tor') ,('ta')) 

    #Special Character
    f.add_arc('4', '5', ('pho') ,('ho')) 
    f.add_arc('4', '5', ('ss') ,('su')) 
    f.add_arc('4', '5', ('ne') ,('n')) 
    f.add_arc('4', '5', ('b') ,('ya'))
    f.add_arc('4', '5', ('rie') ,('ri'))
  
    
    # transition 5 - 6 states
    f.add_arc('5', '6', ('ll') ,('ru')) 
    f.add_arc('5', '6', ('me') ,('mu')) 
    f.add_arc('5', '6', ('m') ,('mu')) 
    f.add_arc('5', '6', ('tor') ,('ta')) 
    f.add_arc('5', '6', ('c') ,('ku')) 
    f.add_arc('5', '6', ('li') ,('ri')) 
    f.add_arc('5', '6', ('t') ,('to')) 
    f.add_arc('5', '6', ('n') ,('n')) 
    f.add_arc('5', '6', ('ch') ,('chi')) 
    f.add_arc('5', '6', ('po') ,('po')) 
    f.add_arc('5', '6', ('rea') ,('ri')) 
    f.add_arc('5', '6', ('ze') ,('zu')) 
    f.add_arc('5', '6', ('wer') ,('wa'))
    f.add_arc('5', '6', ('ne') ,('n')) 

    #Special Character
    f.add_arc('5', '6', ('o') ,('n')) 
    f.add_arc('5', '6', ('t') ,('to')) 
    f.add_arc('5', '6', ('ba') ,('be'))
    f.add_arc('5', '6', ('d') ,('da'))
    f.add_arc('5', '6', ('ke') ,('ku'))
    f.add_arc('5', '6', ('te') ,('to'))
    
    # transition 6 - 7 states
    f.add_arc('6', '7', ('p') ,('pu')) 
    f.add_arc('6', '7', ('za') ,('za')) 
    f.add_arc('6', '7', ('do') ,('do')) 
    f.add_arc('6', '7', ('ta') ,('te')) 
    f.add_arc('6', '7', ('m') ,('mu')) 
    f.add_arc('6', '7', ('g') ,('gu')) 
    #Special Character
    f.add_arc('6', '7', ('n') ,('gu')) 
    f.add_arc('6', '7', ('ge') ,('tsu'))
    f.add_arc('6', '7', ('s') ,('su')) 

    # transition 7 - 8 states
    f.add_arc('7', '8', ('g') ,('gu')) 
    f.add_arc('7', '8', ('to') ,('to'))
    f.add_arc('7', '8', ('li') ,('ri'))

    # transition 8 - 9 states
    f.add_arc('8', '9', ('p') ,('pu'))

    # add final/accepting state(s)
    f.set_final('2')
    f.set_final('3')
    f.set_final('4')
    f.set_final('5')
    f.set_final('6')
    f.set_final('7')
    f.set_final('8')
    f.set_final('9')


    inp = Eng_word.replace(" ","")
    Jap_word_Org = Jap_word
    outp = Jap_word.replace(" ","")
    y+=1
    if y==1:
        saveFile = open('transliterate.txt', 'w')
        for v in range(1, len(f._dst)+1):   
            a = str(''.join(f.in_string(arc="a%d" % v)) + " ---> " + ''.join(f.out_string(arc="a%d" % v)))
            saveFile.write(a)
            saveFile.write("\n")
            v += 1
        saveFile.close()
         
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
        print("reject")


disp = FSTDisplay(f)        #to show the arc

import re
import os
os.chdir('C:/Users/muham/Documents/CSC 4309_Natural Language Processing/')
di_unigram={}
di_bigram={}
di_trigram={}

di_unigram_count = {}
di_bigram_count = {}
di_trigram_count = {}

di_probability = {}
di_test_unigram = {}
di_test_bigram = {}
di_test_trigram = {}
test = "KICT also aspires to enhance the quality of learning and teaching"

#tri = line.split()[k]+" "+line.split()[k+1]+" "+line.split()[k+2]
def ngram():


    for i in range(len(test.split())):        #range 0 sampai total perkataan yg ada
        uni_test = test.split()[i].replace(',','')                  

        if uni_test in di_test_unigram:
            di_test_unigram[uni_test] = di_test_unigram[uni_test] + 1

        else:
            di_test_unigram[uni_test] = 1

    #print(di_test_unigram)
    
    for j in range(len(test.split())-1):        #range 0 sampai total perkataan yg ada
        bi_test = test.split()[j].replace(',','')+" "+test.split()[j+1].replace(',','')                  
       
        if bi_test in di_test_bigram:
            di_test_bigram[bi_test] = di_test_bigram[bi_test] + 1

        else:
            di_test_bigram[bi_test] = 1

    #print(di_test_bigram)
            
    for k in range(len(test.split())-2):        #range 0 sampai total perkataan yg ada
        tri_test = test.split()[k].replace(',','')+" "+test.split()[k+1].replace(',','')+" "+test.split()[k+2].replace(',','')                 
       
        if tri_test in di_test_trigram:
            di_test_trigram[tri_test] = di_test_trigram[tri_test] + 1

        else:
            di_test_trigram[tri_test] = 1

    #print(di_test_trigram)      
    #using "with" will close the file immediately after last call
    with open("text-ngram.dat","r") as rfile:
        infile = rfile.readlines()
        #for line in infile:
           # word = line.split()
           # di_unigram = word

    sent = [s for s in infile[0].split(".")]   #store every line
    
    for line in sent:        
        for j in range(len(line.split())):        #range 0 sampai total perkataan yg ada
            uni = line.split()[j].replace(',','')                   #unigram words = 1 word  #store first word dulu dalam uni starting from index j=0

            if uni in di_unigram:
                di_unigram[uni] = di_unigram[uni] + 1

            else:
                di_unigram[uni] = 1

    for line in sent:
        for j in range(len(line.split())-1):        #range 0 sampai total perkataan yg ada
            bi = line.split()[j].replace(',','')+" "+line.split()[j+1].replace(',','')               

            if bi in di_bigram:
                di_bigram[bi] = di_bigram[bi] + 1

            else:
                di_bigram[bi] = 1
                
          
    #print("This is the unigram")
    #print(di_unigram)
    #print("\nThis is the bigram")
    #print(di_bigram)

    for line in sent:          
        for k in range(len(line.split())-2):           
            tri = line.split()[k].replace(',','')+" "+line.split()[k+1].replace(',','')+" "+line.split()[k+2].replace(',','')  #trigram words pairing

            if tri in di_trigram:
                di_trigram[tri] = di_trigram[tri] +1
            else:
                di_trigram[tri] = 1

    #print("\nThis is the trigram")
    #print(di_trigram)

    #print("\nTest")
    x_bi = []
    x_range=0
    for keys, values in di_test_bigram.items(): #total number in dictionary
        for key,value in di_bigram.items():
            if key==keys:
                x_bi.append(value)
                x_range+=1
                x_name=key
                #print(str(x_bi),x_name)


    y_uni=[]
    y_range=0
    for keys, values in di_test_unigram.items(): #total number in dictionary
        for key,value in di_unigram.items():
            if key==keys:
                y_uni.append(value)
                y_range+=1
                y_name=key
                #print(str(y_uni),y_name)

    z_tri = []
    z_name=[]
    z_range=0

    for keys, values in di_test_trigram.items():  # total number in dictionary
        for key, value in di_trigram.items():
            if key==keys:
                z_tri.append(value)
                z_range+=1
                z_name.append(key)
                print(z_range)
                # print(str(x_bi),x_name)

    prob=0
    count=0
    print("\nThe probability for test sentence Bi/Uni: \n")
    for keys, values in di_test_bigram.items():
        prob=x_bi[count]/y_uni[count]
        count+=1
        print(str(keys)+" = "+str(prob))




    prob=0
    count=0
    print("\nThe probability for test sentence Tri/bi: \n")
    for z in range(z_range):
        prob = z_tri[count]/x_bi[count]
        count += 1
        print(str(z_name[z]) + " = " + str(prob))


'''    for k in di_bigram:
        for v in di_unigram:
            #print(di_bigram[v])                             #setakat ni sequence die sama ngan dictionary
            probability = di_bigram[k]/di_unigram[v]
            #print(probability)
        #print("done")

        break
'''        
        
   
        #print(di_unigram[k])    #dpt values
        #print(k)                #dpt keys
'''    for line in sent:
        for k in range(len(line.split())-1):     
            probability = di_unigram.items()[k]
            print(probability)
'''    
           
        
        
        

#probability = di_bigram.items()/di_unigram.items()

#print("The probability is :")
#print(probability)
  
'''    unifile = open("E:/Zaim/3rd Year 1st Sem 2018_2019 sem 2/NLP/Python ngram/unigram.dat","w")
    bifile = open("E:/Zaim/3rd Year 1st Sem 2018_2019 sem 2/NLP/Python ngram/bigram.dat","w")
    trifile = open("E:/Zaim/3rd Year 1st Sem 2018_2019 sem 2/NLP/Python ngram/trigram.dat","w")   
    
    sent = [s for s in infile[0].split(".")]
   
    for line in sent:        
        for j in range(len(line.split())-1):
            uni = line.split()[j]                                  #unigram words
            bi = line.split()[j]+" "+line.split()[j+1]             #bigram words pairing

            #kene create dictionary for unigram, bigram, calculate probability just divide
            unifile = open("unigram.dat","a")
            bifile = open("bigram.dat","a")            
            unifile.write(str(uni)+"\n")
            bifile.write(str(bi)+"\n")            
            unifile.close()
            bifile.close()

        for k in range(len(line.split())-2):
            trifile = open("trigram.dat","a")            
            tri = line.split()[k]+" "+line.split()[k+1]+" "+line.split()[k+2]  #trigram words pairing
            trifile.write(str(tri)+"\n")
            trifile.close()

    
'''
ngram()
'''
print(di_test_unigram)
print(di_test_bigram)
print(di_test_trigram)
'''



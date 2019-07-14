import re

di_unigram={}
di_bigram={}
di_trigram={}

di_unigram_count = {}
di_bigram_count = {}
di_trigram_count = {}

di_probability = {}

def ngram():

    #using "with" will close the file immediately after last call
    with open("text-ngram.dat","r") as rfile:
        infile = rfile.readlines()
        #for line in infile:
           # word = line.split()
           # di_unigram = word

    sent = [s for s in infile[0].split(".")]   #store every line

    for line in sent:        
        for j in range(len(line.split())-1):        #range 0 sampai total perkataan yg ada
            uni = line.split()[j]                   #unigram words = 1 word  #store first word dulu dalam uni starting from index j=0

            if uni in di_unigram:
                di_unigram[uni] = di_unigram[uni] + 1

            else:
                di_unigram[uni] = 1

    for line in sent:
        for j in range(len(line.split())-1):        #range 0 sampai total perkataan yg ada
            bi = line.split()[j]+" "+line.split()[j+1]                  

            if bi in di_bigram:
                di_bigram[bi] = di_bigram[bi] + 1

            else:
                di_bigram[bi] = 1
                
          
    print("This is the unigram")
    print(di_unigram)
    print("\nThis is the bigram")
    print(di_bigram)

    for line in sent:          
        for k in range(len(line.split())-2):           
            tri = line.split()[k]+" "+line.split()[k+1]+" "+line.split()[k+2]  #trigram words pairing

            if tri in di_trigram:
                di_trigram[tri] = di_trigram[tri] +1
            else:
                di_trigram[tri] = 1

    print("\nThis is the trigram")
    print(di_trigram)

    print("\nTest")
    for k in di_bigram:
        for v in di_unigram:
            #print(di_bigram[v])                             #setakat ni sequence die sama ngan dictionary
            probability = di_bigram[k]/di_unigram[v]
            print(probability)
        #print("done")

        break
        
        
        
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


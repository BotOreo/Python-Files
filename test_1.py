import math

di_word = {}
di_unigram = {}
unigram_count = 0
bigram_count = 0
entropy = 0
new_entropy = 0
probability = []
perplexity = 0
laplace = 0
laplace2 = 0
bi_test_sentence = {}
uni_test_sentence = {}

test_sentence = "<s> I could not submit my assignment because my cat ate it </s>"
#print(test_sentence.split())

sentence = "<s> I could not finish my homework because there is a virus in my hard drive </s> \
<s> I could sleep all night since it is so quiet and peaceful </s> \
<s> I have not eaten since my cat hide the plate </s> \
<s> We don't like to do our assignment </s> "



                
for j in range(len(test_sentence.split())):        #range 0 sampai total perkataan yg ada
        uni = test_sentence.split()[j]                   #unigram words = 1 word  #store first word dulu dalam uni starting from index j=0

        if uni in uni_test_sentence:
                uni_test_sentence[uni] = uni_test_sentence[uni] + 1
                        #unigram_count+=1

        else:
                uni_test_sentence[uni] = 1
                #unigram_count+=1
                
#print("Uni test sentence")    
#print(uni_test_sentence)
for j in range(len(test_sentence.split())-1):        #range 0 sampai total perkataan yg ada
            bi = test_sentence.split()[j]+" "+test_sentence.split()[j+1]                  
            if bi in bi_test_sentence:
                bi_test_sentence[bi] = bi_test_sentence[bi] + 1
                #bigram_count+=1
                

            else:
                bi_test_sentence[bi] = 1
                #bigram_count+=1

sent = [s for s in sentence.split(".")]
#print(sent)


for line in sent:        
        for j in range(len(line.split())):        #range 0 sampai total perkataan yg ada
            uni = line.split()[j]                   #unigram words = 1 word  #store first word dulu dalam uni starting from index j=0

            if uni in di_unigram:
                di_unigram[uni] = di_unigram[uni] + 1
                unigram_count+=1

            else:
                di_unigram[uni] = 1
                unigram_count+=1
                
for line in sent:
    #print("test")
    for j in range(len(line.split())-1):        #range 0 sampai total perkataan yg ada
            bi = line.split()[j]+" "+line.split()[j+1]                  
            if bi in di_word:
                di_word[bi] = di_word[bi] + 1
                bigram_count+=1
                

            else:
                di_word[bi] = 1
                bigram_count+=1
                
x_bi = []
bi_range = 0
bi_keys = []
for keys, values in bi_test_sentence.items(): #mapping
        for key, value in di_word.items():
                if key==keys:
                        x_bi.append(value)
                        bi_range +=1
                        bi_keys.append(keys)
                        break
                        #print(str(x_bi),x_name)
                elif key!=keys and key==list(di_word.keys())[-1]:
                        x_bi.append(0)
  

print(x_bi)
y_uni=[]
uni_keys = []
#print(uni_test_sentence)
for keys in test_sentence.split(): #total number in dictionary
        for key,value in di_unigram.items():
                if key==keys:
                        y_uni.append(value)
                        uni_keys.append(keys)
                        break
                        #print(str(y_uni),y_name)
                elif key!=keys and key==list(di_unigram.keys())[-1]:
                        y_uni.append(0)

print(y_uni)
count = 0
'''print("\nThe probability for test sentence Bi/Uni: \n")
for k in range(bi_range):
        print(x_bi[count])
        print(y_uni[count])
        probability=x_bi[count]/y_uni[count]
        #total_prob*=prob
        #laplace_uni = (y_uni[count] + 1)/(total_unigram + len(di_unigram))
        
        print(str(bi_keys[count])+" = "+str(probability))
        count+=1'''
#print("\nBi test sentence")                
#print(bi_test_sentence)


#print("\n")
#print(len(di_word), len(di_unigram))
#print(bigram_count, unigram_count)
#print(di_unigram)
#print(di_word)
#print(list(di_word.items())[0][0].split()[0])   #to get the first word for bigram
#w = list(di_word.items())[0][0]
#print(w.split())
#------------probability of each bigram model
#print(list(di_unigram.items())[1][1])                  new knowledge
#print(len(di_word))
#print(di_word)
'''for i in range(len(di_word)):
        k = list(di_word.items())[i][1]         #store value
        w = list(di_word.items())[i][0].split()[0]      #for mapping 
        #print(k.split())
        for j in di_unigram:                    #for checking
               if j==w:
                       #print(k)
                       #print(di_unigram[j])
                       #print(w)
                       #print(j)
                       probability.append(k/di_unigram[j])
                    
                      
'''
#print("----------------laplace------------\n")
#print(bi_range)
for z in range(len(bi_test_sentence)):
        if y_uni[z] == 0:
                continue           
        else:
                print(x_bi[z], y_uni[z])
                probability.append(x_bi[z]/y_uni[z])
                       
#print(probability)

        
for i in range(len(probability)):
        if probability[i] == 0:
                continue
        else:
                entropy += (probability[i]*(math.log2(probability[i])))

#print(entropy)
      
new_entropy = -(entropy/bigram_count)           # check balik nilai N tu bigram or unigram
print("The per word entropy is : %.10f" %new_entropy)
print(bi_test_sentence)
print(bi_keys)
#LAPLACE
for count in range(len(bi_test_sentence)):
        print("Laplace for each bigram is ")
        laplace = (x_bi[count] + 1)/(y_uni[count] + len(di_word))
        laplace2 += laplace
        print(laplace)

print("Total laplace is ")
print(laplace2)
        
#perplexity
perplexity = 2**laplace2
print("The perplexity is : %.10f" %perplexity)


#print(len(di_word))

'''print("Bigram")
print(di_word)
print("Unigram")
print(di_unigram)
'''
print(bigram_count)

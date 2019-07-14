import math

di_word = {}
di_unigram = {}
unigram_count = 0
bigram_count = 0
entropy = 0
new_entropy = 0
probability = []
perplexity = 0


sentence = "<s> I could not finish my homework because there is a virus in my hard drive </s> \
<s> I could sleep all night since it is so quiet and peaceful </s> \
<s> I have not eaten since my cat hide the plate </s> \
<s> We don't like to do our assignment </s> "


print(sentence)
sent = [s for s in sentence.split(".")]
print(sent)


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

print("\n")
print(len(di_word), len(di_unigram))
#print(bigram_count, unigram_count)
print(di_unigram)
print(di_word)
#print(list(di_word.items())[0][0].split()[0])   #to get the first word for bigram
#w = list(di_word.items())[0][0]
#print(w.split())
#------------probability of each bigram model
#print(list(di_unigram.items())[1][1])                  new knowledge

for i in range(len(di_word)):
        k = list(di_word.items())[i][1]         #store value
        w = list(di_word.items())[i][0].split()[0] 
        
        #print(k.split())
        for j in di_unigram:                    #for checking
               if j==w:
                       #print(k)
                       #print(di_unigram[j])
                       #print(w)
                       #print(j)
                       probability.append(k/di_unigram[j])
                       

for i in range(len(di_word)):
        entropy += probability[i]*(math.log2(probability[i]))


new_entropy = -(entropy/bigram_count)           # check balik nilai N tu bigram or unigram
print(new_entropy)


#perplexity
perplexity = 2**new_entropy
print(perplexity)




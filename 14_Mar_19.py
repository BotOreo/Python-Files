di_word = {}
di_unigram = {}
unigram_count=0

sentence = "<s> I could not finish my homework because there is a virus in my hard drive </s>.\
<s> I could sleep all night since it is so quiet and peaceful </s>.\
<s> I have not eaton since my cat hide the plate </s>.\
<s> We don't like to do our assignment </s>."


print(sentence)
sent = [s for s in sentence.split(".")]
print(sent)


for line in sent:        
        for j in range(len(line.split())-1):        #range 0 sampai total perkataan yg ada
            uni = line.split()[j]                   #unigram words = 1 word  #store first word dulu dalam uni starting from index j=0

            if uni in di_unigram:
                di_unigram[uni] = di_unigram[uni] + 1
                unigram_count+=1
            else:
                di_unigram[uni] = 1
                
for line in sent:
    #print("test")
    for j in range(len(line.split())-1):        #range 0 sampai total perkataan yg ada
            bi = line.split()[j]+" "+line.split()[j+1]                  
            if bi in di_word:
                di_word[bi] = di_word[bi] + 1
                

            else:
                di_word[bi] = 1

#print(di_word)
print(di_unigram)
print(unigram_count)

    

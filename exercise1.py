#Tun Muhammad Zaim Bin Aminuddin
# 1629501

di ={}
saveFile = open('E:/Zaim/results.txt','w')

for line in open("recipe_Ital_115.txt"):
    word = line.split()
    for w in word:
        if w in di:
            di[w] = di[w] + 1
        else:
            di[w] = 1

print("Unique word and its frequency:\n\n",di,
      "\n\nNumber of word ""of"" occurs: ")
a = str(di)
saveFile.write("Unique word and its frequency:\n\n")
saveFile.write(a)


for k,v in di.items():
    if(k=='FISH'):
        print(v)
        
b = str(v)
saveFile.write("\n\nNumber of word ""of"" occurs: ")
saveFile.write(b)

print("\nWords that end with 'ly':\n")

for word in line.split():
    if word.endswith("ly"):
        print(word)
        saveFile.write("\n\nWords that end with 'ly':\n\n")
        saveFile.write(word)
     

saveFile.close()



    

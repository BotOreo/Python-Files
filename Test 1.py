import os
import itertools
import json
os.chdir('C:/Users/muham/Documents/CSC 4309_NLP/')
def readf_102():

    di_l = dict()
    infile = open('recipe_Ital_102.txt', 'r')
    inread = infile.readlines()

# ----------This is for dictionary-------------------------------------_#
    for line in inread:
        for word in line.split():
            di_l[word] = di_l.get(word, 0) + 1

    wr_res = open('1315791_result.txt', 'w')
    with open('1315791_result.txt', 'w') as file:
        file.write("Name : Muhamad Arif Lutfi\nMatric no : 1315791\n\n")
        file.write("Unique words in recipe_Ital_102:\n\nUnique = " + json.dumps(di_l))
        file.close()


def readf_115():

    infile = open('recipe_Ital_115.txt', 'r')
    inread = infile.readlines()
    of_w=0
    ly_w=[]

    count=0
    for line in open("recipe_Ital_115.txt"):
        for word in line.split():
            if word=="of":
                of_w+=1

    #print("There are " + str(of_w) + " 'of' words in this text")

#------------------This part is for word that ends with 'ly'----------#
    for line in open("recipe_Ital_115.txt"):
        for word in line.split():
            if word.endswith("ly"):
                ly_w.append(word)




    wr_res = open('1315791_result.txt', 'a')
    with open ('1315791_result.txt', 'a') as file:
        file.write("\n\nIn recipe_Ital_115.txt:\n\nThere are " + str(of_w) + " 'of' words in this text.")
        file.write("\nThe words that ends with 'ly' are: "+str(ly_w))
        file.close()










readf_102()
readf_115()




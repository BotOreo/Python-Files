import re
import os
os.chdir('C:/Users/muham/Documents/CSC 4309_Natural Language Processing/')
def ngram():

    #using "with" will close the file immediately after last call
    with open("text-ngram.dat","r") as rfile:
        infile = rfile.readlines()

    unifile = open("unigram.dat","w")
    bifile = open("bigram.dat","w")
    trifile = open("trigram.dat","w")

    sent = [s for s in infile[0].split(".")]
   
    for line in sent:        
        for j in range(len(line.split())-1):
            uni = line.split()[j]
            bi = line.split()[j]+" "+line.split()[j+1]
            
            unifile = open("unigram.dat","a")
            bifile = open("bigram.dat","a")
            unifile.write(str(uni)+"\n")
            bifile.write(str(bi)+"\n")            
            unifile.close()
            bifile.close()

        for k in range(len(line.split())-2):
            trifile = open("trigram.dat","a")
            tri = line.split()[k]+" "+line.split()[k+1]+" "+line.split()[k+2]
            trifile.write(str(tri)+"\n")
            trifile.close()


ngram()
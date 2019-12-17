from random import seed, randint
from random import random

seed(5)
i=0
statue = []
temp = 0

while (i<=10):

        y = randint(0,20)
        #print(statue)
        statue.append(y)
        i=i+1
print("The random height of the statue in meters (m) : \n",statue)
for x in range(len(statue)):
        for y in range(len(statue)):
                if (statue[x] > statue[y]):
                        temp = statue[x]
                        print("\nCompare statue ",str(x)+ " and statue ", str(y))
                        print("Before changing (m) : ", statue)
                        print("Statue[x]: ", statue[x])
                        print("Statue[y]: ", statue[y])
                        print("Change their place.")
                        statue[x] = statue[y]
                        statue[y] = temp
                        print("After changing (m) : ",statue)
                else:
                        print("\nCompare statue ",str(x)+ " and statue ", str(y))
                        print("Before : ", statue)
                        print("Statue[x]: ", statue[x])
                        print("Statue[y]: ", statue[y])
                        print("After : ",statue)


print("\nFinal result : ",statue)


from random import seed, randint
from random import random

# Python program for implementation of Quicksort Sort

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(arr, low, high):
        i = (low - 1)  # index of smaller element
        pivot = arr[high]  # pivot

        for j in range(low, high):

                # If current element is smaller than the pivot
                if arr[j] < pivot:
                        # increment index of smaller element
                        i = i + 1
                        arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return (i + 1)


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quickSort(arr, low, high):
        if low < high:
                # pi is partitioning index, arr[p] is now
                # at right place
                pi = partition(arr, low, high)

                # Separately sort elements before
                # partition and after partition
                quickSort(arr, low, pi - 1)
                quickSort(arr, pi + 1, high)

#seed(2)
i=0
statue = []
temp = 0

while (i<1000000):

        y = randint(0,9999)
        #print(statue)
        statue.append(y)
        i=i+1
n = len(statue)
quickSort(statue,0,n-1)

print(statue)

'''


# Python3 program to find minimum number
# of swaps required to sort an array

# Function returns the minimum
# number of swaps required to sort the array
def minSwaps(arr):
        n = len(arr)

        # Create two arrays and use
        # as pairs where first array
        # is element and second array
        # is position of first element
        arrpos = [*enumerate(arr)]

        # Sort the array by array element
        # values to get right position of
        # every element as the elements
        # of second array.
        arrpos.sort(key=lambda it: it[1])

        # To keep track of visited elements.
        # Initialize all elements as not
        # visited or false.
        vis = {k: False for k in range(n)}

        # Initialize result
        ans = 0
        for i in range(n):

                # alreadt swapped or
                # alreadt present at
                # correct position
                if vis[i] or arrpos[i][0] == i:
                        continue

                # find number of nodes
                # in this cycle and
                # add it to ans
                cycle_size = 0
                j = i
                while not vis[j]:
                        # mark node as visited
                        vis[j] = True

                        # move to next node
                        j = arrpos[j][0]
                        cycle_size += 1

                # update answer by adding
                # current cycle
                if cycle_size > 0:
                        ans += (cycle_size - 1)
                # return answer
        return ans


# Driver Code
arr = [19, 8, 11, 20, 16, 0, 14, 7, 20, 1]
print(minSwaps(arr))

# This code is contributed
# by Dharan Aditya

'''



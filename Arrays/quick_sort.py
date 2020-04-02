

import random

def quickSort(inputList, start, end):
    if end<=start:
        return

    pivot = inputList[random.randint(start, end)]

    i = start
    j = end
    while i<=j:
        while inputList[i]<pivot:
            i+=1
        while inputList[j]>pivot:
            j-=1
        if i<=j:
            inputList[i], inputList[j] = inputList[j], inputList[i]
            i+=1
            j-=1
    quickSort(inputList, start, j)
    quickSort(inputList, i, end)


myList = [54,26,93,17,77,31,44,55,20]
quickSort(myList, 0, len(myList)-1)
print(myList)

def bubbleSort(inputList):
    sz = len(inputList)
    for i in range(sz-1):
        for j in range(i+1,sz):
            if inputList[i]>inputList[j]:
                inputList[i], inputList[j] = inputList[j], inputList[i]
    return inputList


myList = [54,26,93,17,77,31,44,55,20]
bubbleSort(myList)
print(myList)

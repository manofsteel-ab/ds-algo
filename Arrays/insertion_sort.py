def insertionSort(inputList):
    sz = len(inputList)

    if sz<=1:
        return inputList

    for i in range(1,sz):
        temp = inputList[i]
        j = i-1
        k = i
        while j>=0 and inputList[j]>temp:
            inputList[k] = inputList[j]
            j-=1
            k-=1
        inputList[k] = temp




myList = [54,26,93,17,77,31,44,55,20]
insertionSort(myList)
print(myList)

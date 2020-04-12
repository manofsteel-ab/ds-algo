def mergeSort(inputList):
    sz = len(inputList)
    if sz<=1:
        return inputList
    mid = sz//2
    left = inputList[:mid]
    right = inputList[mid:]
    mergeSort(left)
    mergeSort(right)

    i = 0
    j = 0
    k = 0

    while i < len(left) and j<len(right):
        if left[i]<=right[j]:
            inputList[k] = left[i]
            i+=1
        else:
            inputList[k] = right[j]
            j+=1
        k+=1

    while i<len(left):
        inputList[k] = left[i]
        i+=1
        k+=1
    while j<len(right):
        inputList[k] = right[j]
        j+=1
        k+=1
    return inputList

print(mergeSort(inputList=[2,1,3,5,6]))

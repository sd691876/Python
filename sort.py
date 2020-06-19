def selectionSort(lst):
    for i in range(len(lst)-1):
        currentMin = lst[i]
        currentMinIndex = i
        for j in range(i+1,len(lst)):
            if currentMin > lst[j]:
                currentMin = lst[j]
                currentMinIndex = j
        if currentMinIndex != i:
            lst[currentMinIndex] = lst[i]
            lst[i] = currentMin
    return lst

def insertionSort(lst):
    for i in range(1,len(lst)):
        currentElement = lst[i]
        k = i - 1
        while k >= 0 and lst[k] > currentElement:
            lst[k+1] = lst[k]
            k += -1
        lst[k + 1] = currentElement
    return lst
        

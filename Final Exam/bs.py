def Bubble_sort(number):
    length = len(number)
    for i in range(length-1):
        for j in range(length-i-1):
            if number[j] > number[j+1]:
                number[j],number[j+1] = number[j+1],number[j]
    print(number)

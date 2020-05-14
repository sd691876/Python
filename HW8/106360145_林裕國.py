def Countime(integers):
    integers.sort()
    integers.append(-1)
    count = 0
    i = 0
    while(i!=len(integers)-1):
        for j in range(i,len(integers)):
            if(integers[i]==integers[j] ):
                count += 1
            else:
                print('{0} occurs {1} times'.format(integers[i], count))
                count = 0
                i = j
                break
            
def Distinct(numbers):
    dn = []
    for i in range(len(numbers)):
        if(numbers[i] not in dn):
            dn.append(numbers[i])
    print('The distinct number are {0}'.format(dn))

def indexOfSmallestElement (lst):
    minimum = min(lst)
    print('The index of the smallest element is {0}'.format(lst.index(minimum)))
    
def indexOfGreatestElement (lst):    
    maximum = max(lst)
    print('The index of the greatest element is {0}'.format(lst.index(maximum)))

def eliminateDuplicates(lst):
    dn = []
    for i in range(len(lst)):
        if(lst[i] not in dn):
            dn.append(lst[i])
    print('The distinct numbers are: {0}'.format(dn))
 
#Problem 3
integers = [int(num) for num in input('Enter the integers between 1 and 100: ').split(' ')]
Countime(integers)

#Problem 5
numbers = [int(num) for num in input('Enter the numbers: ').split(' ')]
Distinct(numbers)


#Problem 7


#Problem 8
element = [int(num) for num in \
           input('Enter list element separated by spaces from one line: ').split(' ')]
indexOfSmallestElement (element)
indexOfGreatestElement (element)

#Problem 13
numbers = [int(num) for num in input('Enter ten numbers: ').split(' ')]
eliminateDuplicates(numbers)

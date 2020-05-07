def sumDigits(n):
    summation = 0
    for i in range(len(n)):
        summation = int(n[i]) + summation
    print('The sum of digits for %s is '%''.join(n),'%d'%summation)

def reverse(number):
    print(''.join(number[::-1]))

def displaySortedNumvers(num1, num2, num3):
    n = [num1,num2,num3]
    n.sort()
    print('The sorted numbers are: ',end ="")
    for i in range(len(n)):
        print(n[i],end=" ")
    print(" ")
    
def isPrime(number):
    count = 0
    for i in range(2,number):
        if(number%i==0):
            count += 1
    if(count==0):
        return isPalindrome(number)

def isPalindrome(number):
    count  = 0
    number1 = [int(num) for num in str(number)]
    for i in range(len(number1)//2):
        if(number1[i]!=number1[len(number1)-1-i]):
            count = 1
            break
    if(count==0):
        return number

def Credit_card(number):
    oddSum  = 0
    evenSum = 0
    for i in range(0,len(number)):
        if(i%2==0):
            if((number[i]*2)//10 > 0):
                oddSum  += number[i]*2-9
            else:
                oddSum  += number[i]*2
        else:
               evenSum  += number[i]
    if((oddSum+evenSum)%10 == 0):
        print('The credit card %s is valid'%''.join(map(str, number)))
    else:
        print('The credit card %s is invalid'%''.join(map(str, number)))
  
#Problem 2
n = list(input('Enter a number: '))
sumDigits(n)

#Problem 4
number = list(input('Enter a integer: '))
reverse(number)

#Problem 5
num1,num2,num3 = eval(input('Enter three integers: '))
displaySortedNumvers(num1, num2, num3)

#Problem 24
number = []
i = 2
while(len(number)<=50):
    if(isPrime(i)!=None):
        number.append(isPrime(i))
    i = i+1

for i in range(50):
    print('%7d'%number[i], end ="")
    if(i%10==9):
        print()

#Problem 29
number = [int(num) for num in input('Enter a credit card number as long integer: ')]
Credit_card(number)

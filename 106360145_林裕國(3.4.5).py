from   math  import sqrt
from random  import randint
def Standard_deviation(number):
    summation = 0
    N =len(number)
    for i in range(len(number)):
        summation = summation + number[i]
    mean = summation/N
    sum_sd = 0
    for j in range(len(number)):
        sum_sd = sum_sd + (number[j] - mean)**2
    sd  = sqrt(1/(N-1) *sum_sd)
    print('The mean is: %.5f'%mean)
    print('The standard deviation is: %.5f'%sd)
    
def Cd(digit):
    cd = []
    for i in range(1,(digit//2)+1):
        if(digit % i==0):
            cd.append(i)
    if(sum(cd)==digit):
        return digit

def boxing_result(p_boxing, c_boxing):
    boxing = ["scissor", " rock", "paper"]
    user_win = 0
    computer_win = 0
    if(p_boxing==c_boxing):
        print("It is a draw")
    elif((p_boxing-c_boxing)==-2 or (p_boxing-c_boxing)==1):
        user_win = 1
        print("You won")
    else:
        computer_win = 1
        print("You lost")
    return user_win, computer_win

#3    
number = []
for i in range(0,10):
    digit = eval(input('Please enter the {:d} data: '.format(i+1)))
    number.append(digit)
Standard_deviation(number)

#4
t = []
for i in range(1,10000):
    if(Cd(i)!=None):
        t.append(Cd(i))
print('Perfect number less than 10000 is: ',end = "")
for i in range(len(t)):
    print(t[i], end = " ")
print("")

#5
count_user = 0
count_computer = 1
while(1):
    c_boxing = randint(0,2)
    print(c_boxing+1)
    p_boxing = eval(input("scissor(1), rock(2), paper(3): "))
    user_win, computer_win = boxing_result(p_boxing-1, c_boxing)
    count_user += user_win
    count_computer += computer_win
    if(count_user > count_computer*2 ):
        print('You won more than two times')
        break
    
    
    
    





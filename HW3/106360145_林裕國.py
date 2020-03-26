from math import sqrt
from random import choice,randint
def root(coefficient):
    [a,b,c]= coefficient
    discriminant = b**2 - 4*a*c
    if(discriminant>0):
        r1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
        r2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
        print("The roots are {:.5f} and {:.5f}".format(r1,r2))
    elif(discriminant==0):
        r = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
        print("The roots is ",r)
    else:
        print("The equation has no real roots.")
        
def cramer(coefficient):
    [a,b,c,d,e,f]= coefficient
    if((a*d - b*c)==0):
        print("The equation has no solution")
    else:
        x = (e*d - b*f) / (a*d - b*c)
        y = (a*f - e*c) / (a*d - b*c)
        print("x is {:.1f} and y is {:.1f} ".format(x,y))
        
def boxing_result(p_boxing, c_boxing):
    boxing = ["scissor", " rock", "paper"]
    if(p_boxing==c_boxing):
        print("The computer is {:s}. You are {:s}. It is a draw." \
              .format(boxing[c_boxing],boxing[p_boxing]))
    elif((p_boxing-c_boxing)==-2 or (p_boxing-c_boxing)==1):
        print("The computer is {:s}. You are {:s}.  You won!" \
              .format(boxing[c_boxing],boxing[p_boxing]))
    else:
        print("The computer is {:s}. You are {:s} too. You lost!" \
              .format(boxing[c_boxing],boxing[p_boxing]))

#Problem 1
coefficient = [int(num) for num in input("Enter a, b, c: ").split(",")]
while(len(coefficient)!=3):
    coefficient = [int(num) for num in input("Enter a, b, c: ").split(",")]    
root(coefficient)

#Problem 3
coefficient = [int(num) for num in input("Enter a, b, c, d, e, f: ").split(",")]
while(len(coefficient)!=6):
    coefficient = [int(num) for num in input("Enter a, b, c: ").split(",")]
cramer(coefficient)

#Problem 8
integer = [int(num) for num in input("Enter a, b, c: ").split(",")]
integer.sort()
print("The sorted numbers are ",end="")
for i in range(0,len(integer)):
    print(integer[i],end=" ")

#Problem 15
lottery_number = str(randint(100,999))
print("Lottery is ",int(lottery_number))
predict_lottery = input("Enter your lottery pick(three digits): ")
if(lottery_number==predict_lottery):
    print("Exact match: you win $10,000")
else:
    count = 0
    for i in range(0,len(lottery_number)):
        for j in range(0,len(predict_lottery)):
            if(lottery_number[i]==predict_lottery[j]):
                count+=1
                continue
    if(count==3):
      print("Match all digits: you win $3,000")
    elif(count!=0):
      print("Match one digit: you win $1,000")
    else:
      print("Sorry, no match")  

#Problem 17
p_boxing = eval(input("scissor(0), rock(1), paper(2): "))
c_boxing = randint(0,2)
boxing_result(p_boxing, c_boxing)    
     
#Problem 24
Magnitude = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
Type      = ["Clubs", "Diamonds", "Hearts", "Spades"]
print("The card you picked is {:s} of {:s}".format(choice(Magnitude),choice(Type)))

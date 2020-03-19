import random
one=random.randrange(1,7)
two=random.randrange(1,7)
sum_only=one+two
print("You rolled ",one,"+",two,"=",sum_only)
print("point is ",sum_only)
if((sum_only==2) or (sum_only==3) or (sum_only==12)):
    print("you lose")
elif((sum_only==7) or (sum_only==11)):
    print("You win")
else:
    while(True):
        one=random.randrange(1,7)
        two=random.randrange(1,7)
        summ=one+two
        print("You rolled ",one,"+",two,"=",summ)
        if(sum_only==summ):
            print("You win")
            break
        elif(summ==7):
            print("You lose")
            break
        else:
            continue
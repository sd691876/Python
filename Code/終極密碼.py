import random
number=0
secrete=0
while(secrete==0):
    print("please input the secrete number between 1 to 100:")
    secrete=random.randint(1,100)
    
    while(secrete > 0 and secrete < 100):
        number=int(input("please input the number between 1 to 100 by your think:"))   
        
        if(number > secrete):
            print("It's too large, please try again")
            
        elif(number < secrete):
            print("It's too small, please try again")
            
        else:
            print("well done")
            break
    
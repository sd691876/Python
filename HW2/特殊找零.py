while(1):
    money=eval(input("Enter your money: "))
    c=money//4
    b=(money%c)//3
    a=money-c*4-b*3
    if(money%4==0):
        c=money//4
        a=b=0
    elif(money%3==0):
        if(money//3<a+b+c):
            b=money//3
            a=c=0
    print("Your amount ",money," consists of\n", \
          format(str(c)+" four dollars\n",'>20s'), \
          format(str(b)+" three dollars\n",'>18s'), \
          format(str(a)+" one dollars\n",'>19s'))

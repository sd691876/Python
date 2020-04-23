def Loans(amount,year):
    rate = 0.05
    print('Interest Rate        Monthly Payment        Total Payment')
    for i in range((8-5)*8+1):
        print(format(rate*100,">13.3f"),'%',end='')
        monthly_pay = amount * (rate/12)/(1-1/((1+rate/12)**(year*12)))
        print(format(monthly_pay,">21.2f"),end='')
        Total = monthly_pay * year * 12
        print(format(Total,">21.2f"))
        rate = rate +0.00125
    
        
def Commission(amount):
    money =0
    reg = 0
    while(reg <= amount):
        money += 1
        if(money>10000):
            reg = 5000*(0.08+0.1) + (money-10000)*0.12
        elif(money<=10000 and money>5000):
            reg = 5000*0.08 + (money-5000)*0.1
        else:
            reg = money*0.08
    print('The sales amount $',money)
    print('is need to make a commission of $',amount)
    

def Find_max():
    count = 1
    reg   = 1
    integer = eval(input('Please enter a positive integer:  '))
    while(integer!=0 and reg!=0):
        reg = eval(input('Please enter a positive integer:  '))
        if(reg > integer):
            integer = reg
            count = 1
        elif(reg == integer):
            count += 1
    print('The largest number is ', integer)
    print('The occurrence count of the largest number is ',count)

def Base_transform(digit, base=16):
    i=0
    if(type(digit)==str):
        summer = 0
        for i in range(len(digit)-1,-1,-1):
            if(65<=ord(digit[i])<=54+base):
                reg = ord(digit[i])-55
            else:
                reg = ord(digit[i])-48
            summer = summer + reg*(base**(len(digit)-1-i))
        print(summer)
    else:
        out = []
        #print("{:d} use base {:d} is : ".format(digit,base),end="")
        while(digit!=0):
            out.append(digit %  base)        
            digit  = digit // base
            if( out[i] > 9):
                out[i] = chr(out[i]+55)
            else:
                out[i] = chr(out[i]+48)
            i+=1
        #print(''.join(out[::-1]))
    return out
          
#Problem 23
Amount = eval(input('Loan Amount: '))
Year   = eval(input('Number of Years'))
Loans(Amount,Year)

#Problem 39
amount = 25000
Commission(amount)

#Problem 41
Find_max() 

#Problem 44
value = eval(input('Enter a decimal value:'))
out = Base_transform(value, 2)
print('The decimal value {:d} convert to binary is: '.format(value),''.join(out[::-1]))

#Problem 45
value = eval(input('Enter a decimal value:'))
out = Base_transform(value, 16)
print('The decimal value {:d} convert to hexadecimal is: '.format(value),''.join(out[::-1]))


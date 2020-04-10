def Base_transform(digit, base=36):
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
        while(digit!=0):
            out.append(digit %  base)        
            digit  = digit // base
            if( out[i] > 9):
                out[i] = chr(out[i]+55)
            i+=1
        for i in range(len(out)-1,-1,-1):
            print(out[i],end="")
        
while(1):
    choice = eval(input("\nEnter your selection to base_transform(0 or 1): "))
    if(choice==0):
        digit, base = eval(input("Enter the digit and base, respectively: "))
        Base_transform(digit, base)
    elif(choice==1):
        digit = input("Enter the digit to turn hex to dec: ")
        Base_transform(digit)
    




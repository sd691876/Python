def Base_transform(digit, base):
    i=0
    out = []
    while(digit!=0):
        out.append(digit %  base)        
        digit  = digit // base
        if( out[i] > 9):
            out[i] = chr(out[i]+55)
        i+=1
    for i in range(len(out)-1,-1,-1):
        print(out[i],end="")
digit, base = eval(input("\nEnter the digit and base, respectively: "))
Base_transform(digit, base)




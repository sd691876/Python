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
        return summer
    else:
        reg = []
        out = []
        while(digit!=0):
            reg.append(digit %  base)        
            digit  = digit // base
            if( reg[i] > 9):
                reg[i] = reg[i]+55
            else:
                reg[i] = reg[i]+48
            i+=1
        for i in range(len(reg)-1,-1,-1):
            out.append(chr(reg[i]))
        return ''.join(out)
        
def Bin2Dec(digit):
    #digit = input('二進位轉十進位: ')
    out = Base_transform(digit,2)
    return out

def Dec2Bin(digit):
    #digit = eval(input('十進位轉二進位: '))
    out = Base_transform(digit,2)
    return out

def Oct2Dec(digit):
    #digit = input('八進位轉十進位: ')
    out = Base_transform(digit,8)
    return out

def Dec2Oct(digit):
    #digit = eval(input('十進位轉八進位: '))
    out = Base_transform(digit,8)
    return out

def Dec2Hex(digit):
    #digit = eval(input('十進位轉十六進位: '))
    out = Base_transform(digit,16)
    return out

def Hex2Dec(digit):
    #digit = input('十六進位轉十進位: ')
    out = Base_transform(digit,16)
    return out





    




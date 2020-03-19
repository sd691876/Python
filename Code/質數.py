number=int (input('請輸入一個整數 : '))
n=1
t=0
print(number,'的因數有',end=' ')
for n in range(1,number+1):
    if((number%n==0)and(n!=number)):
        print(n,end=' ')
        t=t+1
    elif((n==number and t==1) or number==1):
        print(number)
        print("\n%d 是質數"%number)
    elif(number%n!=0):
        continue
    else:
        print(number,end=' ')
        print("\n%d 不是質數"%number)
        break
number=str(input("Enter the number: "))
s=0
for i in range(0,len(number)):
    s+=int(number[i])
print("The sum of digits for %s is %d"%(number,s))
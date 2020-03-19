number=[]
temp=0
a=0
b=1
for i in range(0,1000000):   
    number.append(int(input("Enter a number (0: for end of input): ")))
    if(number[i]==0):
        a=i
        break
for j in range(0,a):
    if(number[j]>number[j+1]):
        temp=number[j]
        number[j]=number[j+1]
        number[j+1]=temp
print("\nThe largest number is ",number[a])
for k in range(0,a):
    if(number[k]==number[a]):
        b+=1
print("The occurrence count of the largest number is ",b)
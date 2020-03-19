#1000以內不被2跟3整除的數
n=int(input("please input the n:"))
for n in range(0,n,1):
    if(n%2!=0 and n%3!=0):
            print(n)
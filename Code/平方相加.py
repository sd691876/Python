#1 + 2 + ... + n的每個平方相加
n=0
sum_1=0
sum_2=0
i=0
n=int(input("please input the n:"))
for i in range(n+1):
    sum_2=i*i
    sum_1=sum_1+sum_2
print("1^2 + 2^2 + 3^2 + ... + %d^2 = %d" %(n, sum_1))
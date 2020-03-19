i=1
a_0=0
a_n=0
for j in range(0,100001):    
    a_0=((-1)**(i+1))/(2*i-1)
    a_n=a_n+a_0
    if(i%10000==0):
        print("第 ",i," 次 = ",(4*a_n))
    i=i+1
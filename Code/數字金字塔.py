number=int (input('請輸入一個整數 : '))
space_i=number*2
j=number-1
time=0
for slide in range(0,number):
    for space in range(space_i+number,0,-1):
        print(end=' ')
    for up_number in range(j,number):
        print('%2d'%(1+time),end=' ')
        time=time+1  
    for down_number in range(j+1,number):
        print('%2d'%(time-1),end=' ')
        time=time-1 
    time=0
    j=j-1
    space_i=space_i-3
    print('\n')
row=int(input("請輸入行數"))
col=int(input("請輸入列數"))
sm=0
for i in range(1,row+1):
    for j in range(1,col+1):
        print('%3d'%(i*j),end=' ')
        sm += i*j
    print()
print("sum =",sm)
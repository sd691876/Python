print(format('|',">4s"),end = " ")
[print(format(i,'>3d'),end=" ") for i in range(1,10)]
print("\n",'-'*40,end="")
for i in range(1,10):
    print("\n%2d | "%i,end = "")
    for j in range(1,10):
        print(format(i*j,">3d"),end=" ")
    
        

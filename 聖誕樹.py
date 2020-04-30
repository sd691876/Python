from random import shuffle
def Tree(N):
    layer = N//4
    f_layer = N - layer*3
    if(f_layer == layer):
        block = f_layer+1
    else:
        block = f_layer
    print(f_layer)
    print(layer)
    for i in range(f_layer):
        for j in range(block+2-i,0,-1):
            print(" ", end = "")
        for k in range(-i,i+1):
                print('*', end = "")
        print("")
    for i in range(layer):
        for j in range(layer-i,0,-1):
            print(" ", end ="")
        for k in range(-i-(f_layer-3),i+1+f_layer-3):
            print('*', end = "")
        print("")
    for i in range(layer):
        for j in range(layer-i-1,0,-1):
            print(" ", end = "")
        for k in range(-i-(f_layer-2),i+1+f_layer-2):
            print('*', end = "")
        print("")
    for i in range(layer):
        for j in range(layer+1):
            print(" ", end = "")
        for n in range(layer):
            print("*", end = "")
        print("")


def Sixty():
    d = ['0','1','2','3','4','5','6','7','8','9']
    while(1):
        f = d[0]
        o = d[1]
        r = d[2]
        t = d[3]
        y = d[4]
        e = d[5]
        n = d[6]
        s = d[7]
        i = d[8]
        x = d[9]
        summation = int(f+o+r+t+y) + int(t+e+n) + int(t+e+n)
        if(summation == int(s+i+x+t+y)):
            print(f)
            print(i)
            print(f)
            print(t)
            print(y)
            break
        else:
            shuffle(d)
    

N = eval(input('tree: '))
Tree(N)
'''
Sixty()
'''

from math import sqrt
def Length(x1, y1, x2, y2):
    L = sqrt((x1-x2)**2+(y1-y2)**2)
    return L

def Area(L1, L2, L3):
    s = (L1 + L2 + L3)/2
    A = sqrt(s*(s-L1)*(s-L2)*(s-L3))
    return A
            
while(1):
    x1,y1 = [0,100]
    x2,y2 = [200,0]
    x3,y3 = [0,0]
    L12 = Length(x1, y1, x2, y2)
    L13 = Length(x1, y1, x3, y3)
    L23 = Length(x2, y2, x3, y3)
    A1  = Area(L12, L13, L23)
    x,y = [int(num) for num in input('x,y: ').split(" ")]
    Lx1 = Length(x, y, x1,y1)
    Lx2 = Length(x, y, x2,y2)
    Lx3 = Length(x, y, x3,y3)
    Ax1 = Area(Lx1, L12, Lx2)
    Ax2 = Area(Lx2, L23, Lx3)
    Ax3 = Area(Lx1, L13, Lx3)
    if(round(A1) == round(Ax1 + Ax2 + Ax3)):
        print('Great')
    else:
        print('Bad')

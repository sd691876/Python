from math import sqrt
class Rectangle:
    def __init__(self,width = 2,height = 1):
        self.width = width
        self.height = height
    def getArea(self):
        return self.width*self.height
    def getPerimeter(self):
        return 2*(self.width + self.height)

class QuadraticEquation:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def getDiscriminant(self):
        return self.b**2 - 4*self.a*self.c
    def getRoot1(self):
        return (-self.b + sqrt(self.getDiscriminant()))/2/self.a
    def getRoot2(self):
        return (-self.b - sqrt(self.getDiscriminant()))/2/self.a

class LinearEquation:
    def __init__(self,a,b,c,d,e,f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
    def isSlovable(self):
        return (self.a*self.d - self.b*self.c) != 0
    def getX(self):
        return (self.e*self.d - self.b*self.f)/(self.a*self.d - self.b*self.c)
    def getY(self):
        return (self.a*self.f - self.e*self.c)/(self.a*self.d - self.b*self.c)

def Q1():
    rectangle = []
    for i in range(2):
        width  = eval(input('The width of the rectangle is '))
        height = eval(input('The height of the rectangle is '))
        rectangle.append(Rectangle(width,height))
        print('The area of the rectangle is {}'.format(rectangle[i].getArea()))
        print('The perimeter of the rectangle is {}'.format(rectangle[i].getPerimeter()))    

def Q6():
    qe = []
    for i in range(3):
        a,b,c = eval(input('Enter a, b, c: '))
        qe.append(QuadraticEquation(a,b,c))
        if(qe[i].getDiscriminant() > 0):
            print('The roots are {:.5f} and {:.5f}'.format(qe[i].getRoot1(),qe[i].getRoot2()))
        elif(qe[i].getDiscriminant() == 0):
            print('The roots is {}'.format(qe[i].getRoot1()))
        else:
            print('The equation has no roots')

def Q7():
    a,b,c,d,e,f = eval(input('Enter a, b, c, d, e, f: '))
    le = LinearEquation(a,b,c,d,e,f)
    if(le.isSlovable()):
        print('x is {:.1f} and y is {:.1f}'.format(le.getX(),le.getY()))
    else:
        print('The equation has no solution')

#Problem 1
Q1()
'''
#Problem 6
Q6()    

#Problem 7
Q7()
'''

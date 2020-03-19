class QuadraticEquation:
    def __init__(self,a,b,c):
        self.__a=a
        self.__b=b
        self.__c=c
    def get(self):
        print("Enter a, b, c is ", self.__a, ",",self.__b,",",self.__c)
    def getDiscriminant(self):
        return (self.__b**2-4*self.__a*self.__c)
    def getRoot1(self):
        return((self.__b*(-1)+(self.__b**2-4*self.__a*self.__c)**0.5)/(2*self.__a))
    def getRoot2(self):
        return((self.__b*(-1)-(self.__b**2-4*self.__a*self.__c)**0.5)/(2*self.__a))

a=float(input("Enter \na="))
b=float(input("b="))
c=float(input("c="))
QuadraticEquation(a,b,c).get()
if(QuadraticEquation(a,b,c).getDiscriminant()>0):
    print("The roots are %5f and 1
          2
          3
          %5f"%(QuadraticEquation(a,b,c).getRoot1() ,QuadraticEquation(a,b,c).getRoot2()))
elif(QuadraticEquation(a,b,c).getDiscriminant()==0):
    print("The root is ",QuadraticEquation(a,b,c).getRoot1())
else:
    print("The equation has no roots")
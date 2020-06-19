class LinearEquation:
    __a = 0
    __b = 0
    __c = 0
    __d = 0
    __e = 0
    __f = 0
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
        
    def a(self):
        return __a
    def b(self):
        return __b
    def c(self):
        return __c
    def d(self):
        return __d
    def e(self):
        return __e
    def f(self):
        return __f
    def isSlovable(self):
        if (self.__a * self.__d - self.__b * self.__c) != 0:
            return True
        else:
            return "The equation has no solution"

    def getX(self):
        x = (self.__e * self.__d - self.__b * self.__f) / (self.__a * self.__d - self.__b * self.__c)
        return x
    def getY(self):
        y = (self.__a * self.__f - self.__e * self.__c) / (self.__a * self.__d - self.__b * self.__c)
        return y

for _ in range(2):
    s = input('Enter a, b, c, d, e, f:')
    t = s.split(' ')
    LE = LinearEquation(int(t[0]), int(t[1]), int(t[2]), int(t[3]), int(t[4]), int(t[5]))
    if LE.isSlovable() == True:
        print('x is', LE.getX(), 'y is', LE.getY())
    else:
        print(LE.isSlovable())
    print('')




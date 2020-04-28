import numpy as np
from   math  import sqrt
def Standard_deviation(number):
    u   = np.mean(number)
    N   = len(number)
    sd  = sqrt(1/N *sum((number - u)**2))
    var = np.mean((number - u)**2) 
    print('%.2f'%sd)
    print(np.std(number))
    print('%.2f'%var)
    print(np.var(number))
    
    
while(1):
    number = [int(num) for num in input("n's number: ").split()]
    Standard_deviation(number)

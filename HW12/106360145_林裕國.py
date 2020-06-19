import numpy as np
from numpy.linalg import inv
def Q1():
    x = np.array([-2.5, 3.2, 0, 4.4, 6.2])
    print('mean is ',np.mean(x))
    print('median is ',np.median(x))
    print('var is ',np.var(x))
    print('standard deviation is ',np.std(x))
    print('min is ',np.min(x))
    print('max is ',np.max(x))
    print(np.delete(x,-1))
    print(np.append(x,8.8))
    print(x+5)
    print('error')

def Q2():
    x = np.array([1,2,3,4,5])
    y = np.array([-1,-2,-3,-4,-5])
    print('x min is ', np.min(x))
    print('x y min are ', np.minimum(x,y))
    print('y max is ', np.max(y))
    print('x y max are ', np.maximum(x,y))
    print('inner product is ',np.dot(np.transpose(x),x))
    print('x,y product is ',np.dot(np.transpose(y),x))
    print('y shape',y.shape)
    print('x y shape',x.shape)
    print('x sum', np.sum(x))
    print('x y sum', np.sum(x+y))
    print('x*y',x*y)
    print('y*x',y*x)
    print('5*x',5*x)
    print('y*5',y*5)
    print('x,y product is ',np.dot(np.transpose(y),x))
    print('z is',np.concatenate((np.delete(x,2),np.delete(y,-1))))

def Q3():
    A = np.array([[1.5, 1.1, 0],[-4.2, -2, 2.2],[0, 4, 3.3]])
    b = np.transpose(np.array([5,4,3]))
    B = np.dot(np.transpose(A),A)
    print('B is ', B)
    print('A+B is ', (A + B))
    print('A-B is ', (A - B))
    print("A' is ", np.transpose(A))
    print('x is', np.dot(inv(A),b))

def Q4():
    A = np.array([-1,-3,-5,-7,-9,11,13,15,2,4,6,8,10,12,-14,-16]).reshape(4,4)
    B = np.transpose(A)
    print(np.size(A))
    print(A.shape)
    print('A-B',(A-B))
    print('B-A',(B-A))
    print('A+B',(A+B))
    print('A*B',A*B)
    print('B*A',B*A)
    print('dot(A,B)', np.dot(A,B))
    print('dot(B,A)', np.dot(B,A))
    print('[A B] is', np.hstack((A,B)).shape)
    print('[A;B] is', np.vstack((A,B)).shape)
    print("A' is", np.transpose(A))
    print('A dimension is ', np.ndim(A))
    print('A gramian is ', A*np.transpose(A))
    print('A inv is ', inv(A))
#Problem 1
Q1()

#Problem 2
Q2()

#Problem 3
Q3()

#Problem 4
Q4()

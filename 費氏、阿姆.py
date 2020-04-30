def Fibonacci(N):
    if(N == 0 or N == 1):
        return N
    else:
        return Fibonacci(N-1) + Fibonacci(N-2)

def Armstrong(AN):
    list_AN = list(str(AN))
    summation = 0
    for i in range(len(list_AN)):
        summation = int(list_AN[i])**3 + summation
    if(summation == AN):
        print('yes')
    return summation
'''
N = eval(input('Fibonacci: '))
print(Fibonacci(N))
'''
AN = eval(input('Armstrong number: '))
Armstrong(AN)

import numpy as np

a = int(input('Limite inferior: '))
b = int(input('Limite superior: '))
it = 0

def f(x):
    return x**3 - 9*x + 3
while b - a > 0.00001:

    x = np.mean([a,b])

    if f(a) > 0:
        if f(x) > 0:
            a = x
        else:
            b = x
    else:
        if f(x) > 0:
            b = x
        else:
            a = x
    it+=1    
print('Raiz: {}'.format(x))
print('Iterações: {}'.format(it))
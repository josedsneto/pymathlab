a = 2
b = 3
it = 1

def f(x):
    return x**3 - 9*x + 3

x = (a*f(b)-b*f(a))/(f(b) - f(a))

while abs(f(x)) > 0.000001:
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
    x = (a*f(b)-b*f(a))/(f(b) - f(a))
    it+=1

print('Raiz: {}'.format(x))
print('Iterações: {}'.format(it))
print('Intervalo: {}'.format([a,b]))

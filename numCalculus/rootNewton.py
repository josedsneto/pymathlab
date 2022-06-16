import numpy as np
from scipy.misc import derivative

def f(x):
    return x**2 - 4*x + 4

def xf(point):
    dfdx = derivative(f, point, dx=1e-6)
    return point - f(point)/dfdx

chute = 5
root = xf(chute)

while(abs(f(root)) > 1e-6):
    root = xf(root)

print(root)
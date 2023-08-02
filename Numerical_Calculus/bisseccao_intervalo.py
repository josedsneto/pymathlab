import numpy as np

# Creates the upper and lower limits variables
a = int(input('Limite inferior: ')) # Lower limit
b = int(input('Limite superior: ')) # Upper limit
it = 0 

# Defines a function to give a function to approximate the root
def f(x):
    return x**3 - 9*x + 3
while b - a > 0.00001: # Defines the precision of the root approximated

    x = np.mean([a,b]) # Defines a new limit 
                        
                        
    if f(a) > 0:        
        if f(x) > 0:        
            a = x   # if the value of the function on the new limit       
        else:       # is positive, the new value updates the upper limit                
            b = x   # if it is negative, it updates the lower limit   
    else:           
        if f(x) > 0:
            b = x
        else:
            a = x
    it+=1 # Updates the number of iterations

# Prints the approximated root and the number of iterations
print('Raiz: {}'.format(x))
print('Iterações: {}'.format(it))

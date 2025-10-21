import numpy as np
import math as math #I was getting a warning that numpy.math.factorial was going to be removed in the future. This is what google told me to do so it doesn't break in the future. math.factorial()


def factorial(n):
    y=math.factorial(n)
    return y
a=0
x=2
nmax=14
y=np.sin(a)

for n in range(nmax):
    if n==0 or n==4 or n==8 or n==12:
        def function(a):
            y=np.cos(a)
            return y
    elif n==1 or n==5 or n==9 or n==13:
        def function(a):
            y=-np.sin(a)
            return y
    elif n==2 or n==6 or n==10:
        def function(a):
            y=-np.cos(a)
            return y
    else:
        def function(a):
            y=np.sin(a)
            return y
    z=(function(a)/factorial(n+1))*(x-a)**(n+1)
    y+=z
    print(y)

print(np.sin(2))







    



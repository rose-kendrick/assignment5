import numpy as np
import math as math #I was getting a warning that numpy.math.factorial was going to be removed in the future. This is what google told me to do so it doesn't break in the future. math.factorial()


def f(x):
    y=np.sin(x)
    return y

def g(x):
    y=np.cos(x)
    return y

def factorial(x):
    y=math.factorial(x)
    return y


a=0

n=0
nmax=100
tol = 0.0001

p = float(input("give a number, p "))

def tyalor_sin(x):
    nmax=15
    y=f(a)
    for n in range(nmax):
        
    y=f(a)+(g(a)/factorial(1))(x-a)+ 




if f(p)==0:
    print("good guess")
else:
    while abs(f(p)) > tol and n < nmax:
        p=p-(f(p)/g(p))
        n+=1
        print(p,n)


    print(p)
    
     



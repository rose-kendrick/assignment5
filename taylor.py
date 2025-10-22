import numpy as np
import math as math #I was getting a warning that numpy.math.factorial was going to be removed in the future. This is what google told me to do so it doesn't break in the future. math.factorial()


def factorial(n):
    y=math.factorial(n)
    return y
a=0
nmax=14
g=np.sin(a)
x=-10
i=0
while x<10:

    for n in range(nmax):
        if n==0 or n==4 or n==8 or n==12:
            y=np.cos(a)
       
        elif n==1 or n==5 or n==9 or n==13:
            y=-np.sin(a)
     
        elif n==2 or n==6 or n==10:
            y=-np.cos(a)

        else:
            y=np.sin(a)
     
        z=(y/factorial(n+1))*(x-a)**(n+1)
        g+=z
        print(g)
        print("The actual value is {}".format(np.sin(x)))
    x += 0.1
    i += 1
    print(i)

    



import numpy as np
import math as math #I was getting a warning that numpy.math.factorial was going to be removed in the future. This is what google told me to do so it doesn't break in the future. math.factorial()
import matplotlib.pyplot as pp

def factorial(n):
    y=math.factorial(n)
    return y
a=0
nmax=15

x=-10
x_values=[]
i=0
sin_approx=[]
approx=[[],[],[],[],[],[],[],[],[],[],[],[],[],[]]



while x<10:
    g=np.sin(a)
    for n in range(1,nmax):
        r=n%4
        if r==1:
            y=np.cos(a)
       
        elif r==2:
            y=-np.sin(a)
     
        elif r==3:
            y=-np.cos(a)

        else:
            y=np.sin(a)
        
        z=(y/factorial(n))*(x-a)**(n)
        g+=z
        approx[n-1].append(g)
   
    sin_approx.append(g)
    #print(i)

    #print(g)
    #print(np.sin(x))
    x += 0.1
    x_values.append(x)
    i += 1

#there is probably a better way to do this. I do not know how.
pp.plot(x_values, sin_approx, color='blue', ls=':')
pp.plot(x_values, approx[0], color='red')
pp.plot(x_values, approx[1], color='orange')
pp.plot(x_values, approx[2], color='green')
pp.plot(x_values, approx[3], color='blue')
pp.plot(x_values, approx[4], color='purple')
pp.plot(x_values, approx[5], color='red')
pp.plot(x_values, approx[6], color='orange')
pp.plot(x_values, approx[7], color='green')
pp.plot(x_values, approx[8], color='red')
pp.plot(x_values, approx[9], color='purple')
pp.plot(x_values, approx[10], color='red')
pp.plot(x_values, approx[11], color='orange')
pp.plot(x_values, approx[12], color='green')
pp.plot(x_values, approx[13], color='red')


pp.ylim(-2,2) #I added this because with only 15 terms, the approximations close to -10 and 10 were very far off and you could not see the curves at all. 
pp.xlabel("x")
pp.ylabel("Approximation of sin(x)")
pp.savefig("taylor.png")

    

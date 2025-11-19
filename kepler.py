import numpy as np
import datetime

'''
v = true anomaly
E = eccentric anomaly
e = orbit eccentricity
M = mean anomaly [0,2pi]
T = orbital period
tau = time when object is at periapsis
t = time
'''

# M = E-e*sinE
# M(t) = [(2*pi)/T]*(t-tau)
# tan(v/2) = sqrt[(1+e)/(1-e)]*tan(E/2)

# Mars (e = 0.0934) on 6 August 1672 (the day Mars's polar ice cap was discovered). We currently use 1 June 2007, 07:20 UT as Mars's time of periapsis (tau).

# Asteroid Donaldjohanson (e = 0.1876) on 20 April 2025 (date of Lucy mission flyby).  Last periapsis was 3 December 2024

def M(t,tau,T):
    y=((2*np.pi)/T)*(t-tau)
    return y

def m(e,E,M):
    y=E-e*np.sin(E)-M
    return y

def m_prime(e,E,M):
    y=1-e*np.cos(E)
    return y

def kepler(e,M):
    n=0
    nmax=100
    tol = 0.0001

    if m(e,E,M)==0:
        print("no need for Kepler")
    else:
        while abs(m(e,E,M)) > tol and n < nmax:
            E=E-(m(e,E,M)/m_prime(e,E,M))
            n+=1
           
    return E
      


#Mars
e_mars = 0.0934
t_mars = datetime.datetime(1672, 8, 6)
tau_mars = datetime.datetime(2007, 6, 1, 7, 20)
T_mars = 59336800 #s
timeDifference_mars = t_mars - tau_mars
M_mars = M(t_mars, tau_mars, T_mars)
breakpoint()
E_mars = kepler(e_mars, M_mars)

  
    


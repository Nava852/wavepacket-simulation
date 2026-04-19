import numpy as np
import config as c

def Vgj(j):
    return (c.hslash * c.k[j])/c.m

def sigma(t):
    return c.stddev*np.sqrt(1+( (c.hslash*t)/(2*c.m*c.stddev**2))**2)

def ProbPsi(x,y,z,t):
    sig = sigma(t)

    const = 1 / (2*np.pi*(sig)**2)** (1.5)
    exp = np.exp(-1* ( (x-Vgj(0)*t)**2 + (y-Vgj(1)*t)**2 + (z-Vgj(2)*t)**2)/(2*sig**2))
    return const*exp
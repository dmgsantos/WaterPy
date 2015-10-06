__author__ = 'WETpython'

import math
from UnitConversion import *

# Vapor pressure according to Antoine formula
def WATER_antoine_vp(t):
    if t <= 99:
        a = 8.14019
        b = 1810.94
        c = 244.485
    else:
        a = 8.07131
        b = 1730.63
        c = 233.426

    vp= 133.322365 * 10**(a-b/(c+t))

    return(vp);

#Water density
def WATER_density_rho(t,s):
    rho = 1000*(1 - (t+288.9414)/(508929.2*(t+68.12963))*(t-3.9863)**2.0)
    A = 0.824493 - 0.0040899*t + 0.000076438*t**2 -0.00000082467*t**3 + 0.0000000053675*t**4
    B = -0.005724 + 0.00010227*t - 0.0000016546*t**2
    C = 0.00048314
    rhos = rho + A*s + B*s**(3/2) + C*s**2
    return(rhos);

#Water spcecific weight
def WATER_density_gamma(t,s):
    g = 9.80665
    rho = WATER_density_rho(t,s)
    gamma = rho * g
    return(gamma);

#Dynamic viscosity of water
def WATER_viscosity_dvisc(t):
    A = 0.00002414
    B = 247.8
    C = 140.0
    T = UNIT_temperature_c2k(t)
    dvisc = A*10**(B/(T-C))
    return(dvisc);

#Kynematic viscosity of water
def WATER_viscosity_kvisc(t,s):
    dvisc = WATER_viscosity_dvisc(t) # water dynamic viscosity
    rho = WATER_density_rho(t,s) # water density, kg/m3
    kvisc = dvisc/rho
    return(kvisc);

#Reynolds number of water
def WATER_reynoldsnumber_re(q,d,t,s):
    pi = 4*math.atan(1.0)
    a= pi*d**2/4
    v=q/a
    kvisc = WATER_viscosity_kvisc(t,s)
    re=v*d/kvisc
    return(re)
__author__ = 'WETpython'

def WATER_antoine_pv(t):
    if t < 100:
        a = 8.14019
        b = 1810.94
        c = 244.485
        pv= 133.322365 * 10**(a-b/(c+t))
    else:
        a = 8.07131
        b = 1730.63
        c = 233.426
        pv= 133.322365 * 10**(a-b/(c+t))
    return(pv);

def WATER_density_rho(t,s):
    rho = 1000*(1 - (t+288.9414)/(508929.2*(t+68.12963))*(t-3.9863)**2.0)
    A = 0.824493 - 0.0040899*t + 0.000076438*t**2 -0.00000082467*t**3 + 0.0000000053675*t**4
    B = -0.005724 + 0.00010227*t - 0.0000016546*t**2
    C = 0.00048314
    rhos = rho + A*s + B*s**(3/2) + C*s**2
    return(rhos);

def WATER_dviscosity_dvisc(t):
    A = 0.00002414
    B = 247.8
    C = 140.0
    T = t + 273.15
    dvisc = A*10**(B/(T-C))
    return(dvisc);

def WATER_kviscosity_kvisc(t,s):
    dvisc = WATER_dviscosity_dvisc(t) # water dynamic viscosity
    rho = WATER_density_rho(t,s) # water density, kg/m3
    kvisc = dvisc/rho
    return(kvisc);



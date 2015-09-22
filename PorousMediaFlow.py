__author__ = 'WETpython'

from WaterProperties import *

#Darcy law_hydraulic condutivity
# t, temperature (oC)
# s, salinity (g/kg)
# k, intrinsic permeability (m2)
def PMF_darcylaw_kdarcy(t,s,k):
    dvisc = WATER_viscosity_dvisc(t)    #dinamic viscosity (Pa.s)
    gamma = WATER_density_gamma(t,s)    #spcecific weight (N/m3)
    kdarcy = k*gamma/dvisc              #hydraulic condutivity (m/s)
    return (kdarcy)

#Darcy law_specific discharge
def PMF_darcylaw_q(dh,dl,t,s,k):
    kdarcy = PMF_darcylaw_kdarcy(t,s,k) #hydraulic condutivity (m/s)
    dvisc = WATER_viscosity_dvisc(t)    #dinamic viscosity (Pa.s)
    q = -kdarcy*dh/(dvisc*dl)           #specific discharge (m/s)
    return (q)

#Flux velocity in porous media
# n, porosity (0 to 1)
def PMF_darcylaw_v(dh,dl,t,s,k,n):
    q = PMF_darcylaw_q(dh,dl,t,s,k) #specific discarge (m/s)
    v = q/n                         #flux velocity in porous media
    return (v)

#Porous media reynold number
def PMF_darcylaw_re(dh,dl,k,n,t,s):
    q = PMF_darcylaw_q(dh,dl,t,s,k)     #specific discarge (m/s)
    kvisc = WATER_viscosity_kvisc(t,s)  #water dynamic viscosity (Pa.s)
    d = (k/n)**0.5                      #grain diameter for porous media
    re = q*d/kvisc                      #Reynolds number
    return (re)
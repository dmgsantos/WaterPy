__author__ = 'WETpython'

#import math
#from WaterProperties import *
from UniformPressurizedFlow import *

# Power of a pump
#variables:
# p, power, w
# rho, volumic massa, kg/m3
# gamma, volumic weight, N/m3
# h, elevation head, m
# q, flow, m3/s
# y, pump yield.

def EQ_pump_p(q, h, t,s, y):
    g = 9.80665
    gamma = WATER_density_gamma(t,s)
    p = gamma * q * h / y
    return (p);

# power of a pump to elevate a certain flow between two reservoirs
def EQ_pumpstation_p(zr1,zr2,q,ypump,t,s,ds,ns,sumks,ls,dc,nc,sumkc,lc):

    jls = UPF_gms_f(q,ns,ds)*ls # continuos headloss in the suction pipe
    jlc = UPF_gms_f(q,nc,dc)*lc # continuos healoss in the compression pipe
    dhs = UPF_minorloss_dh(q,sumks,ds) # sum of minor losses in the suction pipe
    dhc = UPF_minorloss_dh(q,sumkc,dc) # sum of minor losses in the compression  pipe
    ht = zr2 - zr1 + jls + jlc + dhs + dhc # total elevation head

    p = EQ_pump_p(q, ht, t,s, ypump) # elevation power

    return (p, ht);

def EQ_pumpstation_npshr(zr1,ze,q,t,s,ds,ns,sumks,ls, patm):

    jls = UPF_gms_f(q,ns,ds)*ls # continuos headloss in the suction pipe
    dhs = UPF_minorloss_dh(q,sumks,ds) # sum of minor losses in the suction pipe
    gamma = WATER_density_gamma(t,s)

    vp = WATER_antoine_vp(t) #
    npshr = patm/gamma - vp/gamma - (ze - zr1) - jls - dhs

    return (npshr);

# power of a turbine
def EQ_turbine_p(q, h, t,s, y):
    g = 9.80665
    gamma = WATER_density_gamma(t,s)
    p = gamma * q * h * y
    return (p);


# power and head of a hydropower station
def EQ_hydropower_p(zres,ze,q,yturbine,t,s,d,n,sumk,lpipe):

    jl = UPF_gms_f(q,n,d)*lpipe # continuos headloss in the pipe
    dh = UPF_minorloss_dh(q,sumk,d) # sum of minor losses in the pipe
    h = zres - ze - jl - dh # falling height

    p = EQ_turbine_p(q, h, t,s, yturbine) # elevation power

    return (p, h);
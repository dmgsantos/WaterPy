__author__ = 'WETpython'
# Module: UniformPressurizedFlow.py
# by: WETpython
# version 0.1, September 2015

from WaterProperties import *
from Geometry import *

#minor loss
def UPF_minorloss_dh(q,k,d):
    g = 9.80665
    area= GEO_geometry_acircle(d)
    dh = k*q**2/(2*g*area**2.)
    return (dh);

#friction loss Hazen-Williams
def UPF_hw_f(q,c,d):
    s = 10.67*math.pow(q,1.85)/(math.pow(c,1.85)*math.pow(d,4.87))
    return (s);

#friction loss Gauckler-Manning-Strickler
def UPF_gms_f(q,n,d):
    a= GEO_geometry_acircle(d)
    hr= GEO_geometry_hrcircle(d)
    s = math.pow(q*n/(math.pow(hr,2/3)*a),2.0)
    return (s);

#friction loss Darcy-Weisbach
def UPF_dw_f(q,f,d):
    a= GEO_geometry_acircle(d)
    s = (f/d)*(q**2.0/(2*g*a**2.))
    return (s);

#friction loss Colebrook-White
def UPF_cw_f(q,e,t,s,d):
    re= WATER_reynoldsnumber_re(q,d,t,s)
    f1 = 0.5
    f = 1.0
    while math.fabs(f1-f)>= 0.000001:
        f=f1
        part1 = (e/(3.7*d))
        part2 = (2.51/(re*math.sqrt(f)))
        part3 = -2*math.log10(part1 + part2)
        f1 = math.pow(1/part3,2.0)
    return (f);
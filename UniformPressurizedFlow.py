__author__ = 'WETpython'
# Module: UniformPressurizedFlow.py
# by: WETpython
# version 0.1, September 2015

import math

#minor loss
def UPF_minorloss_dh(q,k,d):
    g = 9.80665
    pi = 4*math.atan(1.0)
    area= pi*d*d/4.0
    dh = k*q**2/(2*g*area**2.)
    return (dh);


#friction loss Hazen-Williams
def UPF_hw_f(q,c,d):
    s = 10.67*math.pow(q,1.85)/(math.pow(c,1.85)*math.pow(d,4.87))
    return (s);

#friction loss Gauckler-Manning-Strickler
def UPF_gms_f(q,n,d):
    pi = 4*math.atan(1.0)
    a= pi*d*d/4.0
    r=d/4.0
    s = math.pow(q*n/(math.pow(r,2/3)*a),2.0)
    return (s);

#friction loss Darcy-Weisbach
def UPF_dw_f(q,f,d):
    pi = 4*math.atan(1.0)
    g = 9.80665
    a= pi*d*d/4
    s = (f/d)*(q*q/(2*g*a*a))
    return (s);

#friction loss Colebrook-White
def UPF_cw_f(q,k,kvisc,d):
    pi = 4*math.atan(1.0)
    a= pi*d*d/4
    r=d/4.0
    v=q/a
    re=v*d/kvisc
    f1 = 0.5
    f = 1.0
    while math.fabs(f1-f)>= 0.000001:
        f=f1
        part1 = (k/(3.7*d))
        part2 = (2.51/(re*math.sqrt(f)))
        part3 = -2*math.log10(part1 + part2)
        f1 = math.pow(1/part3,2.0)
    return (f);
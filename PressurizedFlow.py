# Module: PressurizedFlow.py
# by: Davide Manuel dos Santos
# version 0.0, August 2015

import math

#friction loss Hazen-Williams
def HW_f(q,c,d):
    s = 10.67*math.pow(q,1.85)/(math.pow(c,1.85)*math.pow(d,4.87))
    return (s);

#friction loss Gauckler-Manning-Strickler
def GMS_f(q,n,d):
    pi = 4*math.atan(1.0)
    a= pi*d*d/4
    r=d/4.0
    s = math.pow(q*n/(math.pow(r,2/3)*a),2)
    return (s);

#friction loss Darcy-Weysbach
def DW_f(q,f,d):
    pi = 4*math.atan(1.0)
    g = 9.80665
    a= pi*d*d/4
    s = (f/d)*(q*q/(2*g*a*a))
    return (s);

#friction loss Colebrook-White
def CW_f(q,k,cvisc,d):
    pi = 4*math.atan(1.0)
    a= pi*d*d/4
    r=d/4.0
    v=q/a
    re=v*d/cvisc
    f1 = 0.5
    f = 1.0
    while math.fabs(f1-f)>= 0.000001:
        part1 = (k/(3.7*d))
        part2 = (2.51/(re*math.sqrt(f)))
        part3 = -2*math.log10(part1 + part2)
        f1 = math.pow(1/part3,2)
        f=f1
    return (f);
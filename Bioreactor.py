__author__ = 'WETpython'

import math

def BIO_eckenfelder_se(sf,r, k, t, n, q,h, area):
    se = 1.0
    se1 = 2.0
    while math.fabs(se1-se)>= 0.001:
        se = se1
        b = (k*h*1.035**(t-20))/(q*60.0/area)**n
        se1 = ((sf+r*se)/(1+r))*math.exp(-b)
    return (se)

def BIO_eckenfelder_area(sf,se,r, k, t, n, q, h):
    a = ((sf+r*se)/(1+r))
    b = math.log(se/a)
    c = (k*h*1.035**(t-20))
    area = q*60.0/(c/b)**(1/n)
    return (area)




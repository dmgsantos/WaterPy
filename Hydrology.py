__author__ = 'WETpython'

import sys
# Time of concentration according to Z.P. KIRPICH
#variables:
# l, km
# s, %
# tc, hours
def HYD_kirpich_tc(l,s):
    tc = 0.39*(l*l/s)**0.385
    return (tc);

#CN transformation according to AMC I,II or III
def HYD_scs_cn(cn2,amc):
    if amc == 1:
        cn = cn2/(2.3-0.013*cn2)
    elif amc == 2:
        cn = cn2
    elif amc == 3:
        cn = cn2/(0.43+0.0057*cn2)
    else:
        print("Inputted AMC:", amc)
        sys.exit("Incorrect AMC, should be: 1, 2 or 3!")
    return (cn);

# determina)on of potential storage according to SCS
def HYD_scs_s(cn2,amc):
    cn = HYD_SCS_cn(cn2,amc)
    s = 25400/cn - 254
    return (s);

# determination of initial abstraction according to SCS
def HYD_scs_ia(cn2,amc):
    s = HYD_scs_s(cn2,amc)
    ia = 1.33*(0.2*s)**1.15
    return (ia);

# determination of efective rain according to SCS
def HYD_scs_q(p,cn2,amc):
    ia = HYD_scs_ia(cn2,amc)
    s = HYD_scs_s(cn2,amc)
    if (p-ia) <=0.0:
        q = 0-0
    else:
        q = (p-ia)**2/(p-ia+s)
    return (q);

# determination of Infiltration
def HYD_scs_inf(p,cn2,amc):
    q = HYD_scs_q(p,cn2,amc)
    inf = p - q
    return (inf);
__author__ = 'WETpython'

# Time of concentration according to Z.P. KIRPICH
#variables:
# l, km
# s, %
# tc, hours
def HYD_kirpich_tc(l,s):
    tc = 0.39*(l*l/s)**0.385
    return (tc);

# determination of initial losses according to SCS
def HYD_scs_ia(p,cn):
    ia = p-5080/cn +50.8
    return (ia);

# determination of efective rain according to SCS
def HYD_scs_pe(p,cn):
    ia = HYD_scs_ia(p,cn)
    if (ia)>0.0:
        pe = ia**2/(p+20320/cn-203.2)
    else:
        pe =0.0
    return (pe);


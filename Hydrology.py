__author__ = 'Davide Manuel dos Santos'

# Time of concentration according to Z.P. KIRPICH
#variables:
# l, km
# s, %
# tc, hours
def HYD_kirpich_tc(l,s):
    tc = 0.39*(l*l/s)**0.385
    return (tc);


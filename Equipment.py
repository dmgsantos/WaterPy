__author__ = 'WETpython'

# Power of a pump
#variables:
# p, power, w
# rho, volumic massa, kg/m3
# gamma, volumic weight, N/m3
# h, elevation head, m
# q, flow, m3/s
# y, pump yield.

def EQ_pump_p(q, h, rho, y):
    g = 9.80665
    gamma = rho * g

    p = gamma * q * h / y
    return (p);
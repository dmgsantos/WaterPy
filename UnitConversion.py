__author__ = 'WaterPython'

# converte temperature from Kelvin to Celcius
def UNIT_temperature_k2c(tkelvin):
    tcelcius = tkelvin - 273.15
    return (tcelcius)

# converte temperature from Celcius to Kelvin
def UNIT_temperature_c2k(tcelcius):
    tkelvin = tcelcius + 273.15
    return (tkelvin)

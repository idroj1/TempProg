Temp_C = float(input("input a Celsius number of Temperature:"))

Cel = Temp_C
Kel = Temp_C + 273.15
Fah = Temp_C * (9/5) + 32

print("Las diferentes temperaturas que resultan de %0.2f ºC son:" % (Cel))
print("En Kelvin: %0.2f ºK" % (Kel))
print("En Farenheit: %0.2f ºF" % (Fah))
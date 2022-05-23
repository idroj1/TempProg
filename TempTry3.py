
Tempnum = float(input("Ingrese una cantidad de temperatura: "))

print("Para grado kelvin: k")
print("Para grado celcius: c")
print("Para grado fahrenheit: f")

TempType = (input("ingrese una letra de tipo de temperatura: "))

def TempCalc(Tempnum, TempType):
    if (TempType == "k"):
        K = Tempnum
        C = Tempnum - 273.15
        F = ((Tempnum - 273.15) * 9 / 5) + 32
        return print("De los %0.2f ºK pueden tambien ser: %0.2f ºC o %0.2f ºF" %(K, C, F))
        
    elif (TempType == "c"):
        K = Tempnum + 273.15
        C = Tempnum
        F = Tempnum * (9/5) + 32
        return print("De los %0.2f ºC pueden tambien ser: %0.2f ºK o %0.2f ºF" %(C, K, F))
        
    elif (TempType == "f"):
        K = ((Tempnum - 32) * 5 / 9) + 273.15
        C = (Tempnum - 32) * 5 / 9
        F = Tempnum
        return print("De los %0.2f ºF pueden tambien ser: %0.2f ºC o %0.2f ºK" %(F, C, K))
        
    else:
        return print("Error, por favor ponga en el tipo de temperatura solo k, c, o f.")
TempCalc(Tempnum, TempType)
Temp_K = float(input("Ponga un numero de temperatura Kelvin:"))

def Temp_changer(Temp_K):
    kel = Temp_K
    K = print(kel, "ºK")
    
    cel = Temp_K - 273.15
    C = print(cel, "ºC")
    
    far = ((Temp_K - 273.15) * 5 / 9) + 32
    F = print(far, "ºF")
    return print(K, C, F)

print(Temp_changer(Temp_K))

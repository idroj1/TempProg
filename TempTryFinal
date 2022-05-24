
Tempn= float(input("Ingrese una cantidad de temperatura: "))

print("Para grado kelvin: k")
print("Para grado celcius: c")
print("Para grado fahrenheit: f")

TempT = (input("ingrese una letra de tipo de temperatura: "))

def TempC(Tempn, TempT):
    if (TempT == "k"):
        K = Tempn
        C = Tempn - 273.15
        F = ((Tempn - 273.15) * 9 / 5) + 32
        return K, C, F
        
    elif (TempT == "c"):
        K = Tempn + 273.15
        C = Tempn
        F = Tempn * (9/5) + 32
        return K, C, F
        
    elif (TempT == "f"):
        K = ((Tempn - 32) * 5 / 9) + 273.15
        C = (Tempn - 32) * 5 / 9
        F = Tempn
        return K, C, F
        
    else:
        return print("error")


import unittest

class TTF_test(unittest.TestCase):
    
    def TTF_t1(self):
        self.assertEqual(TempC(320, "k"), (320, 46.85, 116.33))

if __name__ == '__main__':
    unittest.main()
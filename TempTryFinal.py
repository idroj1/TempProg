
def TempC(Tempn, TempT):
    if (TempT == "k"):
        K = float(Tempn)
        C = float(Tempn) - 273.15
        F = ((float(Tempn) - 273.15) * 9 / 5) + 32
        return K, C, F
        
    elif (TempT == "c"):
        K = float(Tempn) + 273.15
        C = float(Tempn)
        F = float(Tempn) * (9/5) + 32
        return K, C, F
        
    elif (TempT == "f"):
        K = ((float(Tempn) - 32) * 5 / 9) + 273.15
        C = (float(Tempn) - 32) * 5 / 9
        F = float(Tempn)
        return K, C, F
        
    else:
        return print("error")


from mmap import ALLOCATIONGRANULARITY
import unittest
from TempTryFinal import TempC

class TTF_test(unittest.TestCase):
    
    def TTF_t1(self):
        Actual = TempC(320, "k")
        Expected = (K, C, F) = (320, 46.85, 116.33)
        self.assertEqual(Actual , Expected)
        
    def TTF_t2(self):
        Actual = TempC(49, "f")
        Expected = (K, C, F) = (282.594, 9.44444, 49)
        self.assertEqual(Actual , Expected)
    
    def TTF_t3(self):
        Actual = TempC(19, "c")
        Expected = (K, C, F) = (292.15, 19, 66.2)
        self.assertEqual(Actual , Expected)

if __name__ == '__main__':
    unittest.main()
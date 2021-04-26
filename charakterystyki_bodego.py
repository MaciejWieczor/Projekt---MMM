import math

class Charakterystyki_bodego:

    def __init__(self,  ilosc_krokow, krok, a1, a0, b2, b1 , b0, T):

        self.a1 = a1
        self.a0 = a0
        self.b2 = b2
        self.b1 = b1
        self.b0 = b0
        self.T = T
        self.ilosc_krokow = ilosc_krokow
        self.krok = krok
        self.amplitudowa_x = []
        self.amplitudowa_y = []
        self.fazowa_y = []
        self.fazowa_x = []
        if(b0 == 0 and b2 == 0 and b1 == 0):
            self.fazowa_y = [0]
            self.amplitudowa_x = [0]
        else:
            self.amplitudowa_wartosci()
            self.fazowa_wartosci()
    
    def amplitudowa_wartosci(self):
        for i in range(1, self.ilosc_krokow+1): ##dla i = 0 moze sie popsuc, gdy b0 = 0, dlatego licze od 1 probki, a nie od 0
            self.amplitudowa_y.append(math.sqrt(math.pow(self.a1*self.krok*i,2)+math.pow(self.a0,2))
                                      /(math.sqrt(math.pow(self.b0-self.b2*math.pow(self.krok*i,2),2)+math.pow(self.b1*self.krok*i,2))))
            self.amplitudowa_x.append(i*self.krok)

    def fazowa_wartosci(self):
        for i in range(1, self.ilosc_krokow+1):
            tmp = math.sqrt(math.pow(self.b0-self.b2*math.pow(self.krok*i,2),2)+math.pow(self.b1*self.krok*i,2))
            self.fazowa_y.append(math.degrees(-math.atan2(math.sin(self.T*self.krok*i),math.cos(self.T*self.krok*i))
                                 -math.atan2(self.b1*self.krok*i/tmp,(self.b0-self.b2*math.pow(self.krok*i,2))/tmp)
                                 +math.atan2(self.a1*self.krok*i,self.a0)))
            self.fazowa_x.append(i*self.krok)

    def return_values_amplitude(self):
        return self.amplitudowa_y

    def return_values_phase(self):
        return self.fazowa_y

    def return_indexes_amplitude(self):
        return self.amplitudowa_x
    
    def return_indexes_phase(self):
        return self.fazowa_x
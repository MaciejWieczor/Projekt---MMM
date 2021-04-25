class Rownanie_rozniczkowe:

    def __init__(self, pobudzenie, ilosc_krokow, krok, a1, a0, b2, b1 , b0, w0, w1, T): ## w0 i w1 to warunki poczatkowe
        self.wynik = []
        if(b2 == 0): ##b2 musi być różne od 0
            self.wynik = 0
        else:
            self.alfa = a0/b2
            self.beta = a1/b2
            self.gamma = b0/b2
            self.delta = b1/b2
            self.w0 = w0
            self.w1 = w1
            self.krok = krok
            self.wejscie = pobudzenie
            self.ilosc_krokow = ilosc_krokow
            self.symulacja()
            self.T = T
            if(self.T < 0):
                self.T = 0
            self.przesuniecie()

    class  Integrator:

        def __init__(self, warunek_poczatkowy, krok):

            self.krok = krok
            self.akumulator = warunek_poczatkowy
            self.wejscie = 0

        def calkowanie(self, wejscie):
            self.wejscie = wejscie
            self.akumulator = self.akumulator + self.wejscie * self.krok
    
        def zwroc_wartosc(self):
            return self.akumulator

    def symulacja(self):

        ##inicjalizacja
        x0prim = 0
        x1prim = 0
        S0 = self.Integrator(self.w0, self.krok)
        S1 = self.Integrator(self.w1, self.krok)

        ##symulacja
        for t in range(0, self.ilosc_krokow):

            S0.calkowanie(x0prim)
            S1.calkowanie(x1prim)
            x0prim = self.alfa * self.wejscie[t] - self.gamma * S1.zwroc_wartosc()
            x1prim = self.beta * self.wejscie[t] - self.delta * S1.zwroc_wartosc() + S0.zwroc_wartosc()
            self.wynik.append(S1.zwroc_wartosc())

    def przesuniecie(self):
        n = 0
        while(self.T > n*self.krok):
            self.wynik.insert(0,0)
            self.wynik.pop()
            n += 1

    def value_return(self):
        return self.wynik



from pobudzenie import Pobudzenie

sygnal = []

for i in range(0,1000):
    sygnal.append(1)

wynik = Rownanie_rozniczkowe(sygnal, 1000, 0.01, 1, 1, 1, 1, 10, 0, 0, 1)

print(wynik.value_return())
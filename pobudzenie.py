class Pobudzenie:
    def __init__(self, length, type, amplitude, width, phase_shift):
        self.length = length
        self.type = type
        self.values = []
        self.amplitude = amplitude
        self.width = width
        self.phase_shift = phase_shift
        self.y = self.create_list_value()


    def phase(self):                                                #phase shift - dla ujemnych int w prawo, dla dodatnich w lewo
        if(self.phase_shift < 0):                                   #jeśli self.phase_shift = 0, zwraca niezmienioną listę
            for i in range(0, abs(self.phase_shift)):
                self.values.insert(0, 0)
                self.values.pop()
        if(self.phase_shift > 0):
            for i in range(0, self.phase_shift):
                self.values.append(0)
                self.values.pop(0)
        return self.values

    def create_list_value(self):                                    #tworzenie listy pobudzenia
                                                                    #opcje : "square", "triangle"
        if(self.type == "square"):
            for i in range (0,self.width):
                self.values.append(self.amplitude)
            for i in range (self.width, self.length):
                self.values.append(0)

        if(self.type == "triangle"):
            self.values.append(0)
            loop_num = int(self.length / self.width) + 1                        #określenie ile pół okresów ma się wykonać + 1 który zostanie na końcu poprawiony
            for i in range (0, loop_num):
                if(self.width % 2 == 0):
                    half = int((self.width)/2)
                else:
                    half = int((self.width - 1)/2)
                for i in range(1, half+1):
                    self.values.append(self.amplitude * i / (half + 1))
                self.values.append(self.amplitude)
                for i in range(-half, 0):
                    self.values.append(self.amplitude * (-i) / (half + 1))
                self.values.append(0)                                           #zero na koniec każdego pół okresu
            reszta = len(self.values) - self.length                             #dopełnienie ostatniego okresu
            for i in range(0, reszta):
                self.values.pop()

        self.values = self.phase()
        return self.values

    def value_return(self):                                                     #hermetyzacja czy coś
        return self.y



import numpy as np
import matplotlib.pyplot as plt

range_var = 50
sygnal = Pobudzenie(range_var, "triangle", 3, 15, -15)
x = []
for i in range(0, range_var):
    x.append(i)
y = sygnal.value_return()
print(sygnal.value_return())
plt.plot(x,y)
plt.show()
import math

class Pobudzenie:
    def __init__(self, length, type, amplitude, freq, step, phase_shift = 0):
        self.length = length
        self.type = type
        self.values = []
        self.indexes = []
        self.amplitude = amplitude
        self.freq = freq
        self.step = step
        self.phase_shift = phase_shift
        self.x = self.declare_index()
        self.y = self.create_list_value()

    def declare_index(self):
        if(self.type == "sine"):
            for n in range(0, self.length):
                self.indexes.append(n * 2 * math.pi * self.freq * self.step)

        if(self.type == "triangle" or self.type == "square"):
            for n in range(0, self.length):
                self.indexes.append(n*self.step)

        return self.indexes

    def create_list_value(self):
        if(self.type == "sine"):
            for n in range(0, self.length):
                self.values.append(math.sin(self.indexes[n]))

        if(self.type == "triangle"):
            T = 1/self.freq
            liczba_okresow = int(self.length * self.step / T) + 1
            for i in range(0, liczba_okresow):
                for n in range(0, int(T/4/self.step)):
                    self.values.append(self.amplitude * self.indexes[n] * 4 / T)
                for n in range(0, int(T/2/self.step)):
                    self.values.append(self.amplitude + (-self.amplitude) * self.indexes[n] * 4 / T)
                for n in range(0, int(T/4/self.step)):
                    self.values.append(self.amplitude * self.indexes[n] * 4 / T - self.amplitude)
            reszta = len(self.values) - self.length
            for i in range(0, reszta):
                self.values.pop()

        if(self.type == "square"):
            for i in range(0, int(1/self.freq/self.step)):
                self.values.append(self.amplitude)
            for i in range(int(1/self.freq/self.step), self.length):
                self.values.append(0)

        self.values = self.phase()
        return self.values


    def phase(self):                                                #phase shift - dla ujemnych int w prawo, dla dodatnich w lewo
        actual_phase = int(self.phase_shift/self.step)
        if(self.phase_shift < 0):                                   #jeśli self.phase_shift = 0, zwraca niezmienioną listę
            for i in range(0, abs(actual_phase)):
                self.values.insert(0, 0)
                self.values.pop()
        if(self.phase_shift > 0):
            for i in range(0, abs(actual_phase)):
                self.values.append(0)
                self.values.pop(0)
        return self.values


    def value_return(self):                                                     #hermetyzacja czy coś
        return self.y

    def index_return(self):                                                     #hermetyzacja czy coś
        return self.x



import numpy as np
import matplotlib.pyplot as plt

range_var = 500                                                                 
sygnal = Pobudzenie(range_var, "square", 5, 10, 0.001, -0.1)                    #opcje "square", "triangle", "sine"
x = sygnal.index_return()
y = sygnal.value_return()
print(sygnal.value_return())
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x,y)
ax.set_xlabel('czas')
ax.set_ylabel(f"{sygnal.type}(t)")
ax.set_title('Pobudzenie')

ax.text(0.95, 0.07, f'Frequency = {sygnal.freq}',
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='blue', fontsize=12)

ax.text(0.95, 0.01, f'Step size = {sygnal.step}',
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='blue', fontsize=12)

plt.show()

#def __init__(self, length, type, amplitude, freq, step, phase_shift = 0):      #ściąga co gdzie wpisać w sygnal = Pobudzenie
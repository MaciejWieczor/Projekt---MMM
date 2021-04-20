from pobudzenie import Pobudzenie

class Convolution:
    def __init__(self, function1, function2):

        if(len(function1) < len(function2)):
            self.function1 = function2
            self.function2 = function1
        else:
            self.function1 = function1
            self.function2 = function2
        self.values = []
        self.y = self.calculate_convolution()

    def calculate_convolution(self):
        self.tmp = 0
        self.t1 = 0
        self.t2 = 0
        self.t3 = 0
        for i in range(0, len(self.function1) + len(self.function2) - 1):
            if(self.t1 < len(self.function2)):
                self.t1 += 1
            else:
                self.t2 += 1
            if(self.t1 + self.t2 > len(self.function1)):
                self.t3 += 1 
            for m in range(0, self.t1 - self.t3):
                self.tmp += self.function1[m + self.t2] * self.function2[self.t1 - 1 - m]
            self.values.append(self.tmp)
            self.tmp = 0
        return self.values

    def value_return(self):
        return self.y

import numpy as np
import matplotlib.pyplot as plt

range_var = 500
step = 0.001
sygnal1 = Pobudzenie(range_var, "square", 5, 10, step, -0.2)
sygnal2 = Pobudzenie(range_var, "square", 5, 10, step, -0.05)
splot = Convolution(sygnal1.value_return(), sygnal2.value_return())
print(splot.value_return())
fig, axs = plt.subplots(3)
axs[0].plot(sygnal1.index_return(), sygnal1.value_return())
axs[1].plot(sygnal2.index_return(), sygnal2.value_return())
x = []
for i in range(0, len(splot.value_return())):
    x.append(i*step)
axs[2].plot(x,splot.value_return())
plt.show()




from pobudzenie import Pobudzenie
import numpy as np
import matplotlib.pyplot as plt

range_var = 20
kwadrat = Pobudzenie(range_var, "triangle", 3, 7)
x = []
for i in range(0, range_var):
    x.append(i)
y = kwadrat.value_return()
print(kwadrat.value_return())
plt.plot(x,y)
plt.show()
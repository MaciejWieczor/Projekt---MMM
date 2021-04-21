import tkinter
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from pobudzenie import Pobudzenie
from odpowiedz_impulsowa import Odpowiedz_impulsowa
from splot import Convolution
import numpy as np

class GUI:
    def __init__(self):
        self.window = self.window_init()
        self.fig = self.fig_ini()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.window)
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.window)

    def window_init(self):
        return tkinter.Tk()

    def fig_ini(self):
        fig = Figure(figsize=(5, 4), dpi=100)
        return fig

    def canvas_toolbar_init(self):
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

        self.toolbar.update()
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    #prawie jak static function ale potrzebuje obiektu Figure
    #rysuje trzy wykresy, pobudzenie, g(t) i splot dwóch poprzednich
    def rysowanie(self, range_var, step, param, amp, freq, phase, type):
        sygnal1 = Pobudzenie(range_var, type, amp, freq, step, phase) 
        sygnal2 = Odpowiedz_impulsowa(range_var, step, param[0],param[1],param[2],param[3],param[4])
        splot = Convolution(sygnal1.value_return(), sygnal2.value_return())

        fig = self.fig
        fig.add_subplot(221).plot(sygnal1.index_return(), sygnal1.value_return())
        fig.add_subplot(222).plot(sygnal2.index_return(), sygnal2.value_return())
        x = []
        for i in range(0, len(splot.value_return())):
            x.append(i*step)
        fig.add_subplot(313).plot(x, splot.value_return())
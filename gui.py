import tkinter
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from pobudzenie import Pobudzenie
from odpowiedz_impulsowa import Odpowiedz_impulsowa
from splot import Convolution
import numpy as np
import math


class GUI:
    def __init__(self):
        self.window = self.window_init()
        self.fig = self.fig_ini()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.window)
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.window)

    def window_init(self):
        return tkinter.Tk()

    def fig_ini(self):
        fig = Figure(figsize=(11, 6), dpi=100)
        return fig

    def canvas_toolbar_init(self):
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

        self.toolbar.update()
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    #prawie jak static function ale potrzebuje obiektu Figure
    #rysuje trzy wykresy, pobudzenie, g(t) i splot dwóch poprzednich
    def rysowanie(self, range_var, step, param, amp, freq, phase, type, T):
        sygnal1 = Pobudzenie(range_var, type, amp, freq, step, phase) 
        sygnal2 = Odpowiedz_impulsowa(range_var, step, param[0],param[1],param[2],param[3],param[4], T)
        splot = Convolution(sygnal1.value_return(), sygnal2.value_return())
        x_pob = sygnal1.index_return()[:int(2*range_var/freq)+int(abs(phase/step))]
        y_pob = sygnal1.value_return()[:int(2*range_var/freq)+int(abs(phase/step))]
        fig = self.fig
        gs = fig.add_gridspec(2,2, hspace=0.5, wspace=0.3)
        
        ax1 = fig.add_subplot(gs[0, 0])
        ax1.plot(x_pob, y_pob)
        ax1.title.set_text(f"Pobudzenie typu {type}")
        ax1.set_xlabel("czas (t = n * krok)")
        ax1.set_ylabel("x[t]")
        ax2 = fig.add_subplot(gs[0, 1])
        ax2.plot(sygnal2.index_return(), sygnal2.value_return())
        ax2.title.set_text("Transmitancja g(t)")
        ax2.set_xlabel("czas (t = n * krok)")
        ax2.set_ylabel("g[t]")
        ax3 = fig.add_subplot(gs[1, :])
        x = []
        for i in range(0, int(len(splot.value_return())/2)):
            x.append(i*step)
        ax3.plot(x, splot.value_return()[:int(len(splot.value_return())/2)])
        ax3.title.set_text(f"Odpowiedź układu czyli splot transmitancji g(t) i pobudzenia typu {type}")
        ax3.set_xlabel("czas (t = n * krok)")
        ax3.set_ylabel("x[t] ⁕ g[t]")
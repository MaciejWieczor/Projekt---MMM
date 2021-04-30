import tkinter
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from pobudzenie import Pobudzenie
from odpowiedz_impulsowa import Odpowiedz_impulsowa
from splot import Convolution
from rownanie_rozniczkowe import Rownanie_rozniczkowe
from charakterystyki_bodego import Charakterystyki_bodego
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
        y = []
        y.append(1/step)
        for i in range(0, range_var-1):
            y.append(0)
        sygnal1 = Pobudzenie(range_var, type, amp, freq, step, phase) 
        sygnal2 = Rownanie_rozniczkowe(y, range_var, step, param[0], param[1], param[2], param[3], param[4], 0, 0, T)
        charakterystyki = Charakterystyki_bodego(range_var, step, param[0], param[1], param[2], param[3], param[4], T)  #dodaj do rysowania na grid z boku
        #sygnal2 = Odpowiedz_impulsowa(range_var, step, param[0],param[1],param[2],param[3],param[4], T)
        splot = Rownanie_rozniczkowe(sygnal1.value_return(), range_var, step, param[0], param[1], param[2], param[3], param[4], 0, 0, T)
        x_pob = sygnal1.index_return()[:int(2*range_var/freq)+int(abs(phase/step))]
        y_pob = sygnal1.value_return()[:int(2*range_var/freq)+int(abs(phase/step))]
        fig = self.fig
        gs = fig.add_gridspec(2,3, hspace=0.5, wspace=0.5)
        z = []
        for i in range(0, range_var):
            z.append(i*step)
        ax1 = fig.add_subplot(gs[0, 0])
        ax4 = fig.add_subplot(gs[0, 2])
        ax4.title.set_text("Charakterystyka amplitudowa odpowiedzi")
        ax4.plot(charakterystyki.return_indexes_amplitude(), charakterystyki.return_values_amplitude())
        ax5 = fig.add_subplot(gs[1, 2])
        ax5.title.set_text("Charakterystyka częstotliwościowa odpowiedzi")
        ax5.plot(charakterystyki.return_indexes_phase(), charakterystyki.return_values_phase())
        ax1.plot(x_pob, y_pob)
        ax1.title.set_text(f"Pobudzenie typu {type}")
        ax1.set_xlabel("czas (t = n * krok)")
        ax1.set_ylabel("x[t]")
        ax2 = fig.add_subplot(gs[0, 1])
        ax2.plot(z, sygnal2.value_return())
        ax2.title.set_text("Odpowiedź impulsowa układu")
        ax2.set_xlabel("czas (t = n * krok)")
        ax2.set_ylabel("h[t]")
        ax3 = fig.add_subplot(gs[1, :2])
        x = []
        for i in range(0, len(splot.value_return())):
            x.append(i*step)
        ax3.plot(x, splot.value_return())
        ax3.title.set_text(f"Odpowiedź układu na pobudzenie typu {type}")
        ax3.set_xlabel("czas (t = n * krok)")
        ax3.set_ylabel("y[t]")
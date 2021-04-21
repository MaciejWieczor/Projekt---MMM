from pobudzenie import Pobudzenie
import numpy as np
from odpowiedz_impulsowa import Odpowiedz_impulsowa
from splot import Convolution
from gui import GUI
import tkinter
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

range_var = 500
step = 0.01
param = [1.6, -3, 0.4, 0.6, 1.4]    #a1, a0, b2, b1, b0
amp = 5
frequency = 10
phase = -0.1
type = "square"
root = GUI()
root.window.wm_title("Embedding in Tk")
root.rysowanie(range_var, step, param, amp, frequency, phase, type)
root.canvas_toolbar_init()


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, root.canvas, root.toolbar)


root.canvas.mpl_connect("key_press_event", on_key_press)


def _quit():
    root.window.quit()     # stops mainloop
    root.window.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


button = tkinter.Button(master=root.window, text="Quit", command=_quit)
button.pack(side=tkinter.BOTTOM)
tkinter.mainloop()


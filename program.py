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
step = 0.1
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

#A1 = tkinter.Text(root.window, height = 1, width = 3)
#A1.pack()

def update():
    range_var = int(name_var.get())
    root.fig.clear()
    root.rysowanie(range_var, step, param, amp, frequency, phase, type)
    root.canvas_toolbar_init()
    print(f"New range_var is {range_var}")


name_var=tkinter.StringVar()
passw_var=tkinter.StringVar()
name_label = tkinter.Label(root.window , text = 'Username', font=('calibre',10, 'bold'))
name_entry = tkinter.Entry(root.window ,textvariable = name_var, font=('calibre',10,'normal'))
sub_btn=tkinter.Button(root.window ,text = 'Update', command = update)
name_entry.pack()
sub_btn.pack()

tkinter.mainloop()


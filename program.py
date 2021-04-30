from pobudzenie import Pobudzenie
import numpy as np
from odpowiedz_impulsowa import Odpowiedz_impulsowa
from splot import Convolution
from gui import GUI
import tkinter
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

range_var = 1000
step = 0.01
param = [1.6, -3, 0.4, 0.6, 1.4]    #a1, a0, b2, b1, b0
amp = 1
frequency = 0.01
phase = 0
T = 0
type = "square"
root = GUI()
frame = tkinter.Frame(root.window)
frame.pack()
root.window.wm_title("Embedding in Tk")
root.rysowanie(range_var, step, param, amp, frequency, phase, type, T)
root.canvas_toolbar_init()


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, root.canvas, root.toolbar)


root.canvas.mpl_connect("key_press_event", on_key_press)


def _quit():
    root.window.quit()     # stops mainloop
    root.window.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate




#A1 = tkinter.Text(root.window, height = 1, width = 3)
#A1.pack()

def update():
    try:
        frequency = float(freq_var.get())
        range_var = int(range_varr.get())
        amp = float(amp_var.get())
        step = float(step_var.get())
        param = [float(a1_var.get()), float(a0_var.get()), float(b2_var.get()), float(b1_var.get()), float(b0_var.get())]
        phase = float(phase_var.get())
        T = float(T_var.get())
    except:
        return None
    root.fig.clear()
    root.rysowanie(range_var, step, param, amp, frequency, phase, type, T)
    root.canvas_toolbar_init()

def square():
    global type
    type = "square"
    try:
        frequency = float(freq_var.get())
        range_var = int(range_varr.get())
        amp = float(amp_var.get())
        step = float(step_var.get())
        param = [float(a1_var.get()), float(a0_var.get()), float(b2_var.get()), float(b1_var.get()), float(b0_var.get())]
        phase = float(phase_var.get())
        T = float(T_var.get())
    except:
        return None
    root.fig.clear()
    root.rysowanie(range_var, step, param, amp, frequency, phase, "square", T)
    root.canvas_toolbar_init()

def triangle():
    global type 
    type = "triangle"
    try:
        frequency = float(freq_var.get())
        range_var = int(range_varr.get())
        amp = float(amp_var.get())
        step = float(step_var.get())
        param = [float(a1_var.get()), float(a0_var.get()), float(b2_var.get()), float(b1_var.get()), float(b0_var.get())]
        phase = float(phase_var.get())
        T = float(T_var.get())
    except:
        return None
    root.fig.clear()
    root.rysowanie(range_var, step, param, amp, frequency, phase, "triangle", T)
    root.canvas_toolbar_init()

def sine():
    global type
    type = "sine"
    try:
        frequency = float(freq_var.get())
        range_var = int(range_varr.get())
        amp = float(amp_var.get())
        step = float(step_var.get())
        param = [float(a1_var.get()), float(a0_var.get()), float(b2_var.get()), float(b1_var.get()), float(b0_var.get())]
        phase = float(phase_var.get())
        T = float(T_var.get())
    except:
        return None
    root.fig.clear()
    root.rysowanie(range_var, step, param, amp, frequency, phase, "sine", T)
    root.canvas_toolbar_init()

def square_wave():
    global type
    type = "square_wave"
    try:
        frequency = float(freq_var.get())
        range_var = int(range_varr.get())
        amp = float(amp_var.get())
        step = float(step_var.get())
        param = [float(a1_var.get()), float(a0_var.get()), float(b2_var.get()), float(b1_var.get()), float(b0_var.get())]
        phase = float(phase_var.get())
        T = float(T_var.get())
    except:
        return None
    root.fig.clear()
    root.rysowanie(range_var, step, param, amp, frequency, phase, "square_wave", T)
    root.canvas_toolbar_init()

bottomframe = tkinter.Frame(root.window)
bottomframe.pack(side = tkinter.BOTTOM)

bottomframe0 = tkinter.Frame(root.window)
bottomframe0.pack(side = tkinter.BOTTOM)

textframe = tkinter.Frame(root.window)
textframe.pack(side = tkinter.BOTTOM)
textframe1 = tkinter.Frame(root.window)
textframe1.pack(side = tkinter.BOTTOM)
textframe2 = tkinter.Frame(root.window)
textframe2.pack(side = tkinter.BOTTOM)
textframe3 = tkinter.Frame(root.window)
textframe3.pack(side = tkinter.BOTTOM)


range_varr=tkinter.StringVar(value=str(range_var))
range_label = tkinter.Label(textframe , text = 'Długość sygnałów', font=('calibre',10, 'bold'))
range_entry = tkinter.Entry(textframe ,textvariable = range_varr, font=('calibre',10,'normal'))
range_label.pack(side = tkinter.LEFT)
range_entry.pack(side = tkinter.LEFT)

freq_var=tkinter.StringVar(value=str(frequency))
freq_label = tkinter.Label(textframe , text = 'Częstotliwość pobudzenia', font=('calibre',10, 'bold'))
freq_entry = tkinter.Entry(textframe ,textvariable = freq_var, font=('calibre',10,'normal'))
freq_label.pack(side = tkinter.LEFT)
freq_entry.pack(side = tkinter.LEFT)


amp_var=tkinter.StringVar(value=str(amp))
amp_label = tkinter.Label(textframe , text = 'Amplituda pobudzenia', font=('calibre',10, 'bold'))
amp_entry = tkinter.Entry(textframe ,textvariable = amp_var, font=('calibre',10,'normal'))
amp_label.pack(side = tkinter.LEFT)
amp_entry.pack(side = tkinter.LEFT)

step_var=tkinter.StringVar(value=str(step))
step_label = tkinter.Label(textframe1 , text = 'Krok sygnałów', font=('calibre',10, 'bold'))
step_entry = tkinter.Entry(textframe1 ,textvariable = step_var, font=('calibre',10,'normal'))
step_label.pack(side = tkinter.LEFT)
step_entry.pack(side = tkinter.LEFT)


phase_var=tkinter.StringVar(value=str(phase))
phase_label = tkinter.Label(textframe1 , text = 'Faza pobudzenia', font=('calibre',10, 'bold'))
phase_entry = tkinter.Entry(textframe1 ,textvariable = phase_var, font=('calibre',10,'normal'))
phase_label.pack(side = tkinter.LEFT)
phase_entry.pack(side = tkinter.LEFT)

T_var=tkinter.StringVar(value=str(T))
T_label = tkinter.Label(textframe1 , text = 'Faza transmitancji', font=('calibre',10, 'bold'))
T_entry = tkinter.Entry(textframe1 ,textvariable = T_var, font=('calibre',10,'normal'))
T_label.pack(side = tkinter.LEFT)
T_entry.pack(side = tkinter.LEFT)

width_param = 18

a1_var=tkinter.StringVar(value=str(param[0]))
a1_label = tkinter.Label(textframe2 , text = 'a1', font=('calibre',10, 'bold'))
a1_entry = tkinter.Entry(textframe2 ,textvariable = a1_var, font=('calibre',10,'normal'), width = width_param)
a1_label.pack(side = tkinter.LEFT)
a1_entry.pack(side = tkinter.LEFT)

a0_var=tkinter.StringVar(value=str(param[1]))
a0_label = tkinter.Label(textframe2 , text = 'a0', font=('calibre',10, 'bold'))
a0_entry = tkinter.Entry(textframe2 ,textvariable = a0_var, font=('calibre',10,'normal'), width = width_param)
a0_label.pack(side = tkinter.LEFT)
a0_entry.pack(side = tkinter.LEFT)

b2_var=tkinter.StringVar(value=str(param[2]))
b2_label = tkinter.Label(textframe2 , text = 'b2', font=('calibre',10, 'bold'))
b2_entry = tkinter.Entry(textframe2 ,textvariable = b2_var, font=('calibre',10,'normal'), width = width_param)
b2_label.pack(side = tkinter.LEFT)
b2_entry.pack(side = tkinter.LEFT)

b1_var=tkinter.StringVar(value=str(param[3]))
b1_label = tkinter.Label(textframe2 , text = 'b1', font=('calibre',10, 'bold'))
b1_entry = tkinter.Entry(textframe2 ,textvariable = b1_var, font=('calibre',10,'normal'), width = width_param)
b1_label.pack(side = tkinter.LEFT)
b1_entry.pack(side = tkinter.LEFT)

b0_var=tkinter.StringVar(value=str(param[4]))
b0_label = tkinter.Label(textframe2 , text = 'b0', font=('calibre',10, 'bold'))
b0_entry = tkinter.Entry(textframe2 ,textvariable = b0_var, font=('calibre',10,'normal'), width = width_param)
b0_label.pack(side = tkinter.LEFT)
b0_entry.pack(side = tkinter.LEFT)


sub_btn=tkinter.Button(bottomframe0 ,text = 'Update', command = update)
square_btn=tkinter.Button(bottomframe ,text = 'square', command = square)
triangle_btn=tkinter.Button(bottomframe ,text = 'triangle', command = triangle)
sine_btn=tkinter.Button(bottomframe ,text = 'sine', command = sine)
square_wave_btn=tkinter.Button(bottomframe ,text = 'square wave', command = square_wave)
button = tkinter.Button(bottomframe0, text="Quit", command=_quit)
sub_btn.pack(side = tkinter.LEFT, ipadx = 6)
button.pack(side = tkinter.LEFT, ipadx = 6)
square_btn.pack(side = tkinter.LEFT, ipadx = 6)
triangle_btn.pack(side = tkinter.LEFT, ipadx = 6)
sine_btn.pack(side = tkinter.LEFT, ipadx = 6)
square_wave_btn.pack(side = tkinter.LEFT, ipadx = 6)

tkinter.mainloop()


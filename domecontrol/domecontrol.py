""" Dome Controller

Opens and closes Astrohaven domes.

This Python script relies on Tkinter to provide a GUI.  If it's not installed on
your system, you're in trouble.
"""

import domecontrolui
import astrohaven
from tkinter import Tk


gui = domecontrolui.DomeList(master=Tk())
gui.master.title("Dome Control")
gui.mainloop()
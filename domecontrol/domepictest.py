# Domepictest: test dome picture class

import domecontrolui
import astrohaven
from tkinter import *


gui = Frame(master=Tk())
gui.grid()
domepic = domecontrolui.DomePic(state=3,motionA='O',motionB='C',master=gui)
domepic.grid()
gui.master.title("Dome Control")
gui.mainloop()
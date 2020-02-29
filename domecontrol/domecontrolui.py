""" DomeControlUI

Tkinter user interface for Astrohaven dome control.

"""
import time
import astrohaven
import serialist

from tkinter import *

class Log(Text):
    """A text widget that can't be edited by the user."""
    def __init__(self,master=None):
        Text.__init__(self,master)
        self.config(state=DISABLED,wrap=WORD)
    def insert(self, index, chars, *args):
        """Add text to the widget without letting the user type in it."""
        self.config(state=NORMAL)
        Text.insert(self,index, chars, args)
        self.config(state=DISABLED)        
    def delete(self, index1, index2=None):
        """Delete text from the widget without letting the user type in it."""
        self.config(state=NORMAL)
        Text.delete(self, index1, index2)
        self.config(state=DISABLED)
    def log(self, chars):
        """Add text to the end of the widget and make sure it's visible."""
        self.insert(END, chars+'\n')
        self.see(END)
        self.update()

class DomeList(Frame):
    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.domepanellist = []
        self.grid()
        self.createWidgets()
        
    def createWidgets(self):
        self.controlframe = Frame (self)
        self.controlframe.grid(row=1,column=1)
        self.portscanbutton = Button (self.controlframe, text='Scan for Domes', command = self.portscan)
        self.portscanbutton.grid(row=1,column=1)
        self.quitbutton = Button (self.controlframe, text='Quit', command = self.quit)
        self.quitbutton.grid(row=1,column=2)
        self.messages = Log(self.controlframe)
        self.messages.config(width=35,height=6)
        self.messages.grid(row=2,column=1,columnspan=2)
        self.portscan()
        
    def quit(self):
        self.closeall()
        self.domepanellist = []
        Frame.quit(self)
        
    def closeall(self):
        for domepanel in self.domepanellist:
            domepanel.dome.closeconn()
            domepanel.grid_forget()
        self.update_idletasks()        

    def portscan(self):
        self.messages.log('Searching for domes on all serial ports.  Please wait...')
        self.closeall()
        self.domepanellist = [];
        serlist = serialist.Serialist()
        i = 1
        for port in serlist:
            dome = astrohaven.Astrohaven(port)
            self.messages.log('Searching for dome at '+port+'...')
            self.update_idletasks()
            self.messages.update()
            if (dome.ready):
                domepanel = DomePanel(dome,master=self)
                self.domepanellist.append(domepanel)
                domepanel.grid(row=int(i/3)+1,column=(i%3)+1)
                i = i + 1
                self.messages.log('Found...')
            else:
                self.messages.log('Not found...')
                dome.closeconn()
            self.update_idletasks()
        self.messages.log('Scan complete.')


# A single dome panel
class DomePanel(Frame):
    def __init__(self, domeobj, master=None):
        """Create UI for a single dome panel.  Required argument "domeobj", a valid
        ready astrohaven.Astrohaven dome object."""
        Frame.__init__(self,master,bd=1)
        if domeobj.ready:
            self.dome = domeobj
        else:
            return False
        self.grid()
        self.createWidgets()
        
    def createWidgets(self):
        self.portlabel = Label (self, text=self.dome.ser.port)
        self.alabel = Label(self, text='Side A')
        self.aopenButton = Button (self, text='Open', command = self.aopen)
        self.acloseButton = Button (self, text='Close', command = self.aclose)
        self.blabel = Label(self, text='Side B')
        self.bopenButton = Button (self, text='Open', command = self.bopen)
        self.bcloseButton = Button (self, text='Close', command = self.bclose)
        
        self.statepic = DomePic(master=self,state=int(self.dome.state()))
        
        self.fullopenButton = Button (self, text='Open Both Sides', command = self.fullopen)
        self.fullcloseButton = Button (self, text='Close Both Sides', command = self.fullclose)        
                
        # Grid 'em all up
        self.portlabel.grid(column=2,row=1)
        self.alabel.grid(column=1,row=2)
        self.aopenButton.grid(column=1,row=3)
        self.acloseButton.grid(column=1,row=4)
        
        self.statepic.grid(column=2,row=2,rowspan=3,columnspan=2)
        
        self.blabel.grid(column=4,row=2)
        self.bopenButton.grid(column=4,row=3)
        self.bcloseButton.grid(column=4,row=4)

        self.fullopenButton.grid(column=1,row=5,columnspan=2)
        self.fullcloseButton.grid(column=3,row=5,columnspan=2)        
        if isinstance(self.master,DomeList):
            self.messages = self.master.messages
        else:
            self.messages = Log(self)
            self.messages.config(width=20,height=4)
            self.messages.insert(END,'Dome on '+self.dome.ser.port+' ready.\n')
            self.messages.grid(column=1,row=5,columnspan=4)


    def aopen(self, event=None):
        self.messages.log(self.dome.ser.port+': Opening side A...')
        self.statepic.drawdome(self.dome.laststate,motionA='Open')
        self.dome.fullmove('A','Open')
        self.messages.log(self.dome.ser.port+': '+self.dome.statetxt())
        self.statepic.drawdome(self.dome.laststate)

    def bopen(self, event=None):
        self.messages.log(self.dome.ser.port+':Opening side B...')
        self.statepic.drawdome(self.dome.laststate,motionB='Open')
        self.dome.fullmove('B','Open')
        self.messages.log(self.dome.ser.port+': '+self.dome.statetxt())
        self.statepic.drawdome(self.dome.laststate)

    def aclose(self, event=None):
        self.messages.log(self.dome.ser.port+': Closing side A...')
        self.statepic.drawdome(self.dome.laststate,motionA='Close')
        self.dome.fullmove('A','Close')
        self.messages.log(self.dome.ser.port+': '+self.dome.statetxt())
        self.statepic.drawdome(self.dome.laststate)

    def bclose(self, event=None):
        self.messages.log(self.dome.ser.port+': Closing side B...')
        self.statepic.drawdome(self.dome.laststate,motionB='Close')
        self.dome.fullmove('B','Close')
        self.messages.log(self.dome.ser.port+': '+self.dome.statetxt())
        self.statepic.drawdome(self.dome.laststate)

    def fullclose(self, event=None):
        self.messages.log(self.dome.ser.port+': Closing both sides...')
        self.statepic.drawdome(self.dome.laststate,motionB='Close',motionA='Close')
        self.dome.fullclose()
        self.messages.log(self.dome.ser.port+': '+self.dome.statetxt())
        self.statepic.drawdome(self.dome.laststate)

    def fullopen(self, event=None):
        self.messages.log(self.dome.ser.port+': Opening both sides...')
        self.statepic.drawdome(self.dome.laststate,motionB='Open',motionA='Open')
        self.dome.fullopen()
        self.messages.log(self.dome.ser.port+': '+self.dome.statetxt())        
        self.statepic.drawdome(self.dome.laststate)

import math

class DomePic(Canvas):
    def __init__(self, state=0, motionA=None,motionB=None, master=None):
        Canvas.__init__(self,master,width=110,height=100)
        self.drawdome(state,motionA,motionB)
        

    def drawdome(self,state=0,motionA=None,motionB=None):
        self.delete(ALL)
        self.create_rectangle(21,55,89,85,fill='#fff')
        if motionA:   # Side A in motion
            self.create_arc(18,18,92,92,start=145,extent=55,fill='#fff')
            self.create_arc(16,16,94,94,start=115,extent=55,fill='#fff')
        else:
            if (state & 2):   # Side A open
                self.create_arc(18,18,92,92,start=155,extent=55,fill='#fff')
                self.create_arc(16,16,94,94,start=155,extent=55,fill='#fff')
            else:
                self.create_arc(18,18,92,92,start=135,extent=55,fill='#fff')
                self.create_arc(16,16,94,94,start=90,extent=55,fill='#fff')

        if motionB:   # Side B in motion
            self.create_arc(18,18,92,92,start=-20,extent=55,fill='#fff')
            self.create_arc(16,16,94,94,start=10,extent=55,fill='#fff')
        else:
            if (state & 1):   # Side B open
                self.create_arc(18,18,92,92,start=-30,extent=55,fill='#fff')
                self.create_arc(16,16,94,94,start=-30,extent=55,fill='#fff')
            else:
                self.create_arc(18,18,92,92,start=-15,extent=55,fill='#fff')
                self.create_arc(16,16,94,94,start=35,extent=55,fill='#fff')

        self.create_oval(50,50,60,60,fill='#fff')
        
        if motionA and (motionA[0].capitalize()[0] == 'O'):   # Open side B
            self.create_line(15,10,15,30,width=3,arrow=LAST)
        elif motionA and (motionA[0].capitalize()[0] == 'C'): # Close side B
            self.create_line(15,10,15,30,width=3,arrow=FIRST)
        if motionB and (motionB[0].capitalize() == 'O'):   # Open side A
            self.create_line(95,10,95,30,width=3,arrow=LAST)
        elif motionB and (motionB[0].capitalize() == 'C'): # Close side A
            self.create_line(95,10,95,30,width=3,arrow=FIRST)
        
        
        self.update()
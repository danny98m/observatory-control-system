"""
Domecontrol.py    -- Controls Astrohaven domes, allowing user to open and close
		     their clamshell doors.
		     
Note: this is Python 3 code.  It runs on Python 2.6 or greater, but the print
output is weird.

Usage:
   domecontrol.py   <Serial Port>   open|close
   <Serial Port> should be the serial port to which the dome is attached.  Should work on Mac, 
		Linux, or PC, but you're responsible for naming the serial port
		properly.  Non-existent or busy serial ports are not handled gracefully.
   open|close should be self-evident.
"""

import time
import serial
import sys

# Handle command-line arguments.  Defaults to COM4, open.
if len(sys.argv) < 2:
	comport = 'COM4'
	open = True
elif len(sys.argv) < 3:
	comport = sys.argv[1]
	open = True
else:
	comport = sys.argv[1]
	open = (sys.argv[2].lower().strip() == 'open')

""" 
Set constants depending on whether we're opening or closing.  When the dome 
receives a lowercase 'a' or 'b', it lowers (opens) the clamshell on the 
left or right side.  Uppercase 'A' and 'B' raises (closes) each clamshell.  
The dome sends 'x' and 'y' when opening is complete on each side, 'X' and 'Y' 
when closing is complete.

The b preceding each string is a Python 3 thing, forcing Python to encode the
characters as literal 8-bit ASCII, rather than some Unicode funkiness.
"""
if (open):
	action = 'opening'
	acmd = b'a'
	bcmd = b'b'
	aresp = b'x'
	bresp = b'y'
else:
	action = 'closing'
	acmd = b'A'
	bcmd = b'B'
	aresp = b'X'
	bresp = b'Y'

# How long to attempt to open/close before giving up, in seconds.
timeout = 10

# Open serial port
ser = serial.Serial(comport,9600,timeout=0)
ser.flushInput()
print('Established connection on port ',comport)
"""If creating the serial port object fails, the program crashes and the above 
   message isn't printed.  That's what I call "graceful error handling."
"""

# Open side A
print(action.capitalize(),' side A')
startime = time.time()
while (True):    # By god, Python, I'll write an infinite loop if I damn well want to!
	ser.write(acmd)
	time.sleep(0.1)
	feedback = ser.read()
	if(feedback==aresp):    # Fully opened/closed, stop 
		print('Done ',action,' Side A, ','%.2f'%(time.time()-startime),'seconds.')
		break
	if(time.time() > (startime + timeout)):
		print('Timed out!  Check for hardware or communications problem.')
		break

ser.flushInput()

# Open side B
print(action.capitalize(),' side B')
startime = time.time()
while (True):
	ser.write(bcmd)
	time.sleep(0.1)
	feedback = ser.read()
	if(feedback==bresp):
		print('Done ',action,' Side B, ','%.2f'%(time.time()-startime),'seconds.')
		break
	if(time.time() > (startime + timeout)):
		print('Timed out!  Check for hardware or communications problem.')
		break

"""
Check dome open/close status.  Once a second while idle, dome sends '0' for both 
sides closed, '1' and '2' for half open/half closed, and '3' for both sides open.
"""

startime = time.time()
while(True):
	fback = ser.read()
	if(fback == b'0'):
		print("Both sides closed")
		break
	elif(fback==b'1'):
		print('Side A open, side B closed')
		break
	elif(fback==b'2'):
		print('Side B open, side A closed')
		break
	elif(fback==b'3'):
		print('Both sides open')
		break
	elif(time.time() > (startime + timeout)):
		print('No response from dome.  Check for communications problem.')
		break

ser.close()
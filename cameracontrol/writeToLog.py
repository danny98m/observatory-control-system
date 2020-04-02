# writeToLog.py
# JP
# Description: writing to an output log instead of sending serial communications to a hardware device
#            : This function will be used by all of our controlling scripts

import os

def writeToLog(outputCommand):
# Description  : Writes to log by appending to the end of the file
# Precondition : outputCommand is a string
# Postcondition: appends outputCommand to fakeOutputLog.txt
    log = open("fakeOutputLog.txt", "a")
    log.write(outputCommand+"\n")
    log.close()

def resetLog():
# Description  : deletes the log 
# Precondition : fakeOutputLog.txt must have been created
# Postcondition: fakeOutputLog.txt was deleted
    os.remove("fakeOutputLog.txt")
# sbigUtil.py
# JP
# Description: set of commands to be able to control an sbig ccd with python/command line
#            : This set of functions will contain the abilies such as:
#            : sbig find - Finding an attached camera
#            : sbig info - Info about vairous pieces of the CCD ADD MORE HERE
#            : sbig cooler - setting the cooling device of the camera on and at what temperature
#            : sbig focus -  set the ccd to focusing mode
#            : sbig cfw - controlling the filter wheel
#            : sbig snap - taking pictures with the ccd MANY COMMANDS HERE

from writeToLog import *

#decision to make is how to structure the commands
#first two thoughts are either every command gets its own function
#or every base command gets a function and the rest of the sub command is dealt with inside the function
#DECISION is to write individual functions for big things but pass paramters for others

#command usage is sbig-"command name"


def isEmpty(stringToCheck):
# Description  : helper function to determine if strings (parameters) are empty
# Precondition : stringTocheck is a string
# Postcondition: returns 1 if stringToCheck == "" else return 0
    if (stringToCheck == ""):
        return 1
    else:
        return 0

def sbigFind():
# Description  : finds the camera if it is plugged in or on local ethernet
# Precondition : camera is connected and on
# Postcondition: camera is found and ready for use
    writeToLog("sbig find")

def sbigInfoDriver():
# Description  : gets info on the driver
# Precondition : camera is connected and on
# Postcondition: info would be displayed/logged
    writeToLog("sbig-info driver")

def sbigInfoCcd(option=""):
# Description  : provides information about the camera with two possible additional options
#              : tracking or imaging
#              : checks for incorrect data DONT KNOW HOW TO ERROR THO?
# Precondition : option has been given no arguements or one argument that is either the string "tracking" or "imaging"
# Postcondition: info would be displayed/logged
    if (option == "tracking"):
        writeToLog("sbig-info ccd tracking")
    elif(option == "imaging"):
        writeToLog("sbig-info ccd imaging")
    elif(option==""):
        writeToLog("sbig-info ccd")
    else:
        writeToLog("error wrong parameter - sbigInfoCcd")

def sbigInfoCfw():
# Description  : provides info about the color filter wheel(cfw)
# Precondition : cfw is attached to the camera and powered
# Postcondition: info would be displayed/logged
    writeToLog("sbig-info cfw")

def sbigInfoCooler():
# Description  : provides info about the cooler
# Precondition : camera is attached and on
# Postcondition: info would be displayed/logged
    writeToLog("sbig-info cooler")

def sbigInfoFov(option1="",option2="", option3=""):
# Description  : provides info about the fov following this argument structure
#              : {tracking|imaging} {lo|med|hi} [focal-length]
# Precondition : option1, option2, option3 are given the appropriate options
# Postcondition: info would be displayed/logged according to the specified set of arguments
    if(isEmpty(option1) and isEmpty(option2) and isEmpty(option3)):
        #none
        writeToLog("sbig-info fov")
    elif((not isEmpty(option1)) and isEmpty(option2) and isEmpty(option3)):
        #opt1
        writeToLog("sbig-info fov "+option1)
    elif((not isEmpty(option1)) and (not isEmpty(option2)) and isEmpty(option3)):
        #opt1 and opt2
        writeToLog("sbig-info fov "+option1+" "+option2)
    elif((not isEmpty(option1)) and (not isEmpty(option2)) and (not isEmpty(option3))):
        #opt1 and opt2 and opt2
        writeToLog("sbig-info fov "+option1+" "+option2+" "+option3)
    elif((not isEmpty(option1)) and isEmpty(option2) and (not isEmpty(option3))):
        #opt1 and opt3
        writeToLog("sbig-info fov "+option1+" "+option3)
    elif(isEmpty(option1) and (not isEmpty(option2)) and (not isEmpty(option3))):
        #opt2 and opt3
        writeToLog("sbig-info fov "+option2+" "+option3)
    elif(isEmpty(option1) and (not isEmpty(option2)) and isEmpty(option3)):
        #opt2
        writeToLog("sbig-info fov "+option2)
    elif(isEmpty(option1) and isEmpty(option2) and (not isEmpty(option3))):
        #opt3
        writeToLog("sbig-info fov "+option3)
    else:
        #should never get here
        writeToLog("ERROR how the hell did you get here - sbigInfoFov")


def sbigCooler(toggle, temp=""):
# Description  : operators the cooling fans in the camera allows to set temperature
# Precondition : camera is on and connected, toggle is given "on" | "off", if set to "on" temp must contain a valid floating point value
# Postcondition: camera is set to the appropriate state
    if((toggle=="on") and (temp != "")):
        writeToLog("sbig-cooler on "+str(temp))
    elif((toggle=="on") and (temp == "")):
        writeToLog("Error no temp specified shutting off cooler - sbigCooler")
        writeToLog("sbig-cooler off")
    elif(toggle=="off"):
        writeToLog("sbig-cooler off")
    else:
        #shouldnt get here
        writeToLog("ERROR shouldnt have gotten here - sbigCooler")

def sbigCfwQuery():
# Description  : queries the filter wheel to ask it its status and position
# Precondition : filter wheel may or may not be present
# Postcondition: info would be displayed/logged
    writeToLog("sbig-cfw query")

def sbigCfwGoTo(filterN):
# Description  : changes filter to desired filter in filter wheel with 1 through N filters
# Precondition : filter wheel is on and connected and filterN is the number of a filter between 1 and N
# Postcondition: the filter wheel is now at filterN
    writeToLog("sbig-cfw goto "+str(filterN))


#still need sbig-focus and sbig-snap THE UGLY ONES
def sbigFocus(optionsArray=[]):
# Description  : puts the camera in focusing mode. This is a continuous stream of photos set at a certain exposure time
# Precondition : camera is on and connected [the desired filter in which you want to focus the telescope should be selected]
#              : optionsArray is an array that contains none,some, or all the options as follows with their associated values
# Postcondition: The camera will continue to take photos as the set duration
# Usage: sbig-focus [OPTIONS]
#   -t, --exposure-time SEC exposure time in seconds (default 1.0)
#   -C, --ccd-chip CHIP     use imaging, tracking, or ext-tracking
#   -r, --resolution RES    select hi, med, or lo resolution
#   -p, --partial N         take centered partial frame (0 < N <= 1.0)
    cmd = "sbig-focus"
    if (len(optionsArray)<=4):
        for option in optionsArray:
            cmd+= " "+option
        writeToLog(cmd)
    else:
        writeToLog("ERROR too many options -sbigFocus")

def sbigSnap(optionsArray=[]):
# Description  : takes a picture
# Precondition : camera is on and connected [the desired filter in which you want to focus the telescope should be selected]
#              : optionsArray is an array that contains none,some, or all the toptions as follows with thier associated values
# Postcondition: the camera will take a picture as specified by the options
# Usage: sbig-snap [OPTIONS]
#   -t, --exposure-time SEC    exposure time in seconds (default 1.0)
#   -d, --image-directory DIR  where to put images (default /tmp)
#   -C, --ccd-chip CHIP        use imaging, tracking, or ext-tracking
#   -r, --resolution RES       select hi, med, or lo resolution
#   -n, --count N              take N exposures
#   -D, --time-delta N         increase exposure time by N on each exposure
#   -m, --message string       add COMMENT to FITS file
#   -O, --object NAME          name of object being observed (e.g. M33)
#   -f, --force                press on even if FITS header will be incomplete
#   -p, --partial N            take centered partial frame (0 < N <= 1.0)
#   -T, --image-type TYPE      take df, lf, or auto (default auto)
#   -c, --no-cooler            allow TE to be disabled/
    cmd = "sbig-snap"
    if(len(optionsArray)<=12):
        for option in optionsArray:
            cmd+= " "+option
        writeToLog(cmd)
    else:
        writeToLog("ERROR too many options -sbigSnap")
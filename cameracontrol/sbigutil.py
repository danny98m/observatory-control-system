"""A set of python function that interacts with the sbig camera library from https://github.com/garlick/sbig-util"""

from writetolog import *


def is_empty(string_to_check):
    """Determines if string_to_check is an empty string."""
    if (string_to_check == ""):
        return 1
    else:
        return 0


def sbig_find():
    """Looks for a CCD."""
    write_to_log("sbig find")


def sbig_info_driver():
    """Gets info about the CCD's driver."""
    write_to_log("sbig-info driver")


def sbig_info_ccd(option=""):
    """Provides information about the camera.

    Keyword arguments:
    option -- { "tracking" | "imaging" }
    """
    if (option == "tracking"):
        write_to_log("sbig-info ccd tracking")
    elif(option == "imaging"):
        write_to_log("sbig-info ccd imaging")
    elif(option == ""):
        write_to_log("sbig-info ccd")
    else:
        write_to_log("error wrong parameter - sbigInfoCcd")


def sbig_info_cfw():
    """Provides info about the color filter wheel(cfw)."""
    write_to_log("sbig-info cfw")


def sbig_info_cooler():
    """Provides info about the cooler."""
    write_to_log("sbig-info cooler")


def sbig_info_fov(option1="", option2="", option3=""):
    """Provides info about the fov.

    Keyword arguments:
    option1 -- { "tracking" | "imaging" }
    option2 -- { "lo" | "med" | "hi" }
    option3 -- [ "focal-length" ]
    """
    if(is_empty(option1) and is_empty(option2) and is_empty(option3)):
        # none
        write_to_log("sbig-info fov")
    elif((not is_empty(option1)) and is_empty(option2) and is_empty(option3)):
        # opt1
        write_to_log("sbig-info fov "+option1)
    elif((not is_empty(option1)) and (not is_empty(option2)) and is_empty(option3)):
        #opt1 and opt2
        write_to_log("sbig-info fov "+option1+" "+option2)
    elif((not is_empty(option1)) and (not is_empty(option2)) and (not is_empty(option3))):
        #opt1 and opt2 and opt2
        write_to_log("sbig-info fov "+option1+" "+option2+" "+option3)
    elif((not is_empty(option1)) and is_empty(option2) and (not is_empty(option3))):
        #opt1 and opt3
        write_to_log("sbig-info fov "+option1+" "+option3)
    elif(is_empty(option1) and (not is_empty(option2)) and (not is_empty(option3))):
        #opt2 and opt3
        write_to_log("sbig-info fov "+option2+" "+option3)
    elif(is_empty(option1) and (not is_empty(option2)) and is_empty(option3)):
        # opt2
        write_to_log("sbig-info fov "+option2)
    elif(is_empty(option1) and is_empty(option2) and (not is_empty(option3))):
        # opt3
        write_to_log("sbig-info fov "+option3)
    else:
        # should never get here
        write_to_log("ERROR how the hell did you get here - sbigInfoFov")


def sbig_cooler(toggle, temp=""):
    """Controls the camera's cooling system.

    Keyword arguments:
    toggle -- "on" | "off"
    temp -- the temperature for the cooling system in degrees C
    """
    if((toggle == "on") and (temp != "")):
        write_to_log("sbig-cooler on "+str(temp))
    elif((toggle == "on") and (temp == "")):
        write_to_log(
            "Error no temp specified shutting off cooler - sbigCooler")
        write_to_log("sbig-cooler off")
    elif(toggle == "off"):
        write_to_log("sbig-cooler off")
    else:
        # shouldnt get here
        write_to_log("ERROR shouldnt have gotten here - sbigCooler")


def sbig_cfw_query():
    """Queries the filter wheel to ask it its status and position."""
    write_to_log("sbig-cfw query")


def sbig_cfw_go_to(filterN):
    """Changes filter to desired filter in filter wheel with 1 through N filters."""
    write_to_log("sbig-cfw goto "+str(filterN))


def sbig_focus(options_array=[]):
    """Puts the camera in focusing mode.

    Keyword arguments:
    options_array -- contains none, some, or all of the following options with thier associated values
                     -t, --exposure-time SEC exposure time in seconds (default 1.0)
                     -C, --ccd-chip CHIP     use imaging, tracking, or ext-tracking
                     -r, --resolution RES    select hi, med, or lo resolution
                     -p, --partial N         take centered partial frame (0 < N <= 1.0)
    """
    cmd = "sbig-focus"
    if (len(options_array) <= 4):
        for option in options_array:
            cmd += " "+option
        write_to_log(cmd)
    else:
        write_to_log("ERROR too many options -sbigFocus")


def sbig_snap(options_array=[]):
    """Takes a picture.

    Keyword arguments:
    options_array -- contains none, some, or all of the following options with thier associated values
                     -t, --exposure-time SEC    exposure time in seconds (default 1.0)
                     -d, --image-directory DIR  where to put images (default /tmp)
                     -C, --ccd-chip CHIP        use imaging, tracking, or ext-tracking
                     -r, --resolution RES       select hi, med, or lo resolution
                     -n, --count N              take N exposures
                     -D, --time-delta N         increase exposure time by N on each exposure
                     -m, --message string       add COMMENT to FITS file
                     -O, --object NAME          name of object being observed (e.g. M33)
                     -f, --force                press on even if FITS header will be incomplete
                     -p, --partial N            take centered partial frame (0 < N <= 1.0)
                     -T, --image-type TYPE      take df, lf, or auto (default auto)
                     -c, --no-cooler            allow TE to be disabled/
    """
    cmd = "sbig-snap"
    if(len(options_array) <= 12):
        for option in options_array:
            cmd += " "+option
        write_to_log(cmd)
    else:
        write_to_log("ERROR too many options -sbigSnap")

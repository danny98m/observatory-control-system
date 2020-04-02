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

import os
import subprocess

#decision to make is how to structure the commands
#first two thoughts are either every command gets its own function
#or every base command gets a function and the rest of the sub command is dealt with inside the function
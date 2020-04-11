import os
import subprocess
from writetolog import *
from sbigutil import *

# a function to list the files in 
# the current directory and  
# parse the output. 
def list_command(args = '-l'): 
  
    # the ls command 
    cmd = 'ls'
  
    # using the Popen function to execute the 
    # command and store the result in temp. 
    # it returns a tuple that contains the  
    # data and the error if any.
    # resetLog()
    write_to_log(cmd+" "+args)
    temp = subprocess.Popen([cmd, args], stdout = subprocess.PIPE)
      
    # we use the communicate function 
    # to fetch the output 
    output = str(temp.communicate()) 
      
    # splitting the output so that 
    # we can parse them line by line 
    output = output.split("\n") 
      
    output = output[0].split('\\') 
  
    # a variable to store the output 
    res = [] 
  
    # iterate through the output 
    # line by line 
    for line in output: 
        res.append(line) 
  
    # print the output 
    for i in range(1, len(res) - 1): 
        print(res[i]) 
  
    # return res 

def main():
    # list_command('-al')
    reset_log()
    sbig_find()
    sbig_info_driver()
    sbig_info_ccd()
    sbig_info_ccd("tracking")
    sbig_info_ccd("imaging")
    sbig_info_cfw()
    sbig_info_cooler()
    sbig_info_fov("tracking", "med", "focal-length")
    sbig_info_fov("","","focal-length")
    sbig_info_fov("imaging")
    sbig_cooler("on",-31.2)
    sbig_cooler("off")
    sbig_cfw_query()
    sbig_cfw_go_to(5)
    sbig_focus()
    sbig_focus(["-t 5"])
    sbig_focus(["-t 5", "-r hi"])
    sbig_snap()
    sbig_snap(["-t 20", "-n 10","-r hi"])

main()
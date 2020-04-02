import os
import subprocess
from writeToLog import *

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
    writeToLog(cmd+" "+args)
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
    list_command('-al')

main()
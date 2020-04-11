"""Interacts with an output log instead of sending serial communications to a hardware device"""
import os

def write_to_log(output_command):
    """Writes to log.

    Keyword arguments:
    output_command -- the command to be outputted
    """
    log = open("fakeOutputLog.txt", "a")
    log.write(output_command+"\n")
    log.close()

def reset_log():
    """Deletes the log."""
    os.remove("fakeOutputLog.txt")
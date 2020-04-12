"""ScopeControl for meade scopes.

    Python functions that will operate meade telescopes
"""

import meade
import radec
import time
import serialist
import log
import inspect



class scope_control:
    """A single scope to be controlled."""
    def __init__(self):
        self.scope = None
        self.connect()
        self.starlock = 0
        self.safe_mode = 0
        self.flip = 'East'
        self.speed = 9
        self.go_to_pos = ''


    def connect(self):
        """Locate and connect to a scope."""
        port_list=serialist.Serialist()
        for port in port_list:
            self.scope=meade.Meade(port)
            if (not self.scope.ready):
                self.scope.close()
    
    def disconnect(self):
        """Safetly disconnect from the scope."""
        if self.scope is not None and self.scope.ready:
            self.scope.set_safe(True)
            if not self.scope.is_safe():
                time.sleep(3)
            self.scope.close()

    def toggle_starlock(self):
        """Toggles the scopes starlock."""
        if (self.starlock == 0):
            self.scope.setstarlock(True)
            self.scope.sethighprecision(True)
            self.starlock = 1
        else:
            self.scope.setstarlock(False)
            self.scope.sethighprecision(False)
            self.starlock = 0

    def focus_in(self):
        """Focuses in."""
        self.scope.focusin()

    def focus_out(self):
        """Focuses out."""
        self.scope.focusout()

    def focus_halt(self):
        """Stops focus movement."""
        self.scope.focushalt()

    def focus_speed(self, speed):
        """Sets the focus speed from 1 to 4."""
        self.scope.focusspeed(speed)

    def go_to(self,ra,dec):
        """Go to the coords specified in standard RA and DEC format"""
        self.go_to_pos = radec.RADec.fromStr(ra,dec)
        if self.scope is not None and self.scope.ready:
            self.scope.goto(self.go_to_pos)

    def sync(self):
        """Sync the scope to its current pos."""
        if self.scope is not None and self.scope.ready:
            self.scope.sync(self.go_to_pos)

    def undo_sync(self):
        """Undo the sync of the scope."""
        self.scope.undosync()

    def flip_pier(self):
        """Flips the direction of pier."""
        if (self.flip == 'East'):
            self.flip = 'West'
        else:
            self.flip = 'East'

    def north(self):
        """Command scope to slew north.  Annoyingly, when the scope is pointed west
        the north/south directions are backward, so use the "Pier Flip" setting to
        reverse directions."""
        if self.scope is not None and self.scope.ready:
            if (self.flip == 'East'):
                self.scope.slewnorth(self.speed)
            else:
                self.scope.slewsouth(self.speed)

    def south(self):
        """Command scope to slew north.  Annoyingly, when the scope is pointed west
        the north/south directions are backward, so use the "Pier Flip" setting to
        reverse directions."""
        if self.scope is not None and self.scope.ready:
            if (self.flip == 'East'):
                self.scope.slewsouth(self.speed)
            else:
                self.scope.slewnorth(self.speed)

    def east(self, event=None):
        """Command scope to slew east."""
        if self.scope is not None and self.scope.ready:
            self.scope.sleweast(self.speed)
        

    def west(self, event=None):
        """Command scope to slew east."""
        if self.scope is not None and self.scope.ready:
            self.scope.slewwest(self.speed)

    def stop(self, event=None):
        """Command scope to stop slewing."""
        if self.scope is not None and self.scope.ready:
            self.scope.stop()

    def toggle_safe_mode(self):
        """Handle a change in the state of the "Safe Mode" radio buttons."""
        if self.scope is not None and self.scope.ready:
            self.scope.set_safe(self.safe_mode)
            self.safe_mode = not self.safe_mode
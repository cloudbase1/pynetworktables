#!/usr/bin/env python3
#
#   This program pretends to be a robot, and you can view these values
#   using the SmartDashboard program. Just launch the Smartdashboard
#   like so:
#   
#       SmartDashboard.jar ip 127.0.0.1
#

import time
from pynetworktables import *

# wpilib crashes if you don't do this.. 
SmartDashboard.init()

i = 0
while True:
    SmartDashboard.PutNumber('test', i)
    time.sleep(1)
    i += 1


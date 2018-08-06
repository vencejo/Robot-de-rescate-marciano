#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dbus
import dbus.mainloop.glib
import gobject
from optparse import OptionParser
import os
import time


def initNetwork():
	
	os.system("asebamedulla \"ser:device=/dev/ttyACM0\" &")
	time.sleep(1) #Da tiempo al S.O. a ejecutar la orden anterior

	parser = OptionParser()
	parser.add_option("-s", "--system", action="store_true", dest="system", default=False,help="use the system bus instead of the session bus")
	
	(options, args) = parser.parse_args()
	
	dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
	
	if options.system:
		bus = dbus.SystemBus()
	else:
		bus = dbus.SessionBus()
	
	#Create Aseba network 
	network = dbus.Interface(bus.get_object('ch.epfl.mobots.Aseba', '/'), dbus_interface='ch.epfl.mobots.AsebaNetwork')
	
	#print in the terminal the name of each Aseba NOde
	print network.GetNodesList()
	
	return network
       

    
if __name__ == '__main__':
	pass 


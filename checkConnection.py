#!/usr/bin/python
import socket
import time
import platform

osex = platform.system()
if(osex=="Linux"):
	import os
	while True:
		try:
			socket.create_connection(("www.google.com", 80))
		except:
			os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (1, 440))
		time.sleep(5)
elif(osex=="Windows"):
	import winsound
	while True:
		try:
			socket.create_connection(("www.google.com", 80))
		except:
			winsound.Beep(440, 1000)
		time.sleep(5)

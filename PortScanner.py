#!/bin/python3
import socket
import sys
from datetime import datetime

#define a target
if len(sys.argv)==2:
	target = socket.gethostbyname(sys.argv[1])
else:
	print('Invalid amount of arguments.')
	print('SYNTAX: Python3 portscanner.py <ip address>')

#add a banner
print("-" * 60)
print ("*" * 60)
'\n'
print('SCANNING TARGET: '+target)
print('TIME STARTED AT: '+str(datetime.now()))
'\n'
print("*" *60)
print('-'*60)

try:
	for port in range(20,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		if result == 0:
			print(f'Port {port} is OPEN')
		s.close()
except KeyboardInterrupt:
	print('\n Exiting Program.')
	sys.exit()
except socket.gaierror:
	print('Hotname could not be resolved.')
	sys.exit()
except socket.error():
	print('could not connect to server.')
	sys.exit()

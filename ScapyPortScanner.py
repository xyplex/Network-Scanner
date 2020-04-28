# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 23:08:11 2020

@author: nmist

YouTube Video 
https://www.youtube.com/watch?v=AtzRsJ4ba68&list=FLG4IMKVkWJ1h-O464F608gQ

"""
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

import sys
from scapy.all import *
import time

# if len(sys.argv) != 4 :
#     print("Usage: %s host_address startpoint endpoint"%(sys.argv[0]))
#     sys.exit(0)

# host_address = str(sys.argv[1])
# startpoint = int(sys.argv[2])
# endpoint =  int(sys.argv[3])

host_address = "www.google.com"
startpoint = 1
endpoint = 81
open_ports = []

# common_ports = {21, 22, 23, 25, 53, 69, 80, 88, 109, 119,
#                 123, 137, 138, 139, 143, 156, 161, 389, 443,
#                 445, 500, 546, 547, 587, 660, 995, 993, 2086,
#                 2087, 2082, 2083, 3306, 8443, 8080, 10000
#                 }

common_ports = [80, 443]

print('Scanning '+host_address+' for open TCP ports')
start_time = time.time()

if startpoint == endpoint:
    endpoint += 1

for x in common_ports:
    packet = IP(dst=host_address)/TCP(dport=x, flags='S')
    response = sr1(packet,timeout=0.5,verbose=0)
    if response != None:
        if TCP in response and response[TCP].flags == 'SA':
            print('\nPort '+str(x)+' is open')
            open_ports.append(x)
            sr1(IP(dst=host_address)/TCP(dport=response.sport,flags='R'),timeout=0.5,verbose=0)
            time.sleep(7)

print('\nScan is Complete !!!!!\n')

if open_ports:
    print("\n\nOpen Ports Found: -----> ", sorted(open_ports))
else:
    print("Sorry, No open ports found.!!!")

print('\nTotal Time to Execute = %s' % (time.time() - start_time) + ' Seconds')

        
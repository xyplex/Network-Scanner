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
#     print("Usage: %s target startpoint endpoint"%(sys.argv[0]))
#     sys.exit(0)

# target = str(sys.argv[1])
# startpoint = int(sys.argv[2])
# endpoint =  int(sys.argv[3])

target = "www.google.com"
startpoint = 1
endpoint = 81

print('Scanning '+target+' for open TCP ports')
start_time = time.time()

if startpoint == endpoint:
    endpoint += 1

for x in range(startpoint, endpoint):
    packet = IP(dst=target)/TCP(dport=x, flags='S')
    response = sr1(packet,timeout=0.2,verbose=0)
    if response != None:
        if TCP in response:
            if response[TCP].flags == 'SA':
                print('Port '+str(x)+' is open')
                sr(IP(dst=target)/TCP(dport=response.sport,flags='R'),timeout=0.5,verbose=0)

print('Scan is Complete !!!!!\n')
print('\nTotal Time to Execute = %s' % (time.time() - start_time) + ' Seconds')
        
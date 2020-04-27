# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 09:38:52 2020
    
@author: nmist

Directory:
C:/Users/nmist/Google Drive/Python Programs/Hacking/My Port Scanner

YouTube Video: 
https://www.youtube.com/watch?v=AtzRsJ4ba68&list=FLG4IMKVkWJ1h-O464F608gQ

"""
hello
from scapy.all import *
import socket
import time
import pandas as pd
import numpy as np
import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

csv_file_path = 'C:/Users/nmist/Google Drive/Python Programs/Hacking/My Port Scanner/'
csv_input_file = 'service-names-port-numbers.csv'
csv_output_file = 'service-names-port-numbers_clean.csv'

my_csv_file = csv_file_path + csv_input_file

df = pd.read_csv(my_csv_file)  # Open CSV file using panda read_csv and add to panda frame named df

df = df.drop(['Assignee', 'Contact', 'Registration Date',
              'Modification Date', 'Reference', 'Service Code',
              'Unauthorized Use Reported', 'Assignment Notes'
              ], axis=1)

# df print(df.loc[np.logical_and(df['Service Name'] == "echo", df['Transport Protocol'] == "tcp")])     # Select row
# for column "Service Name" = "echo" and column "Transport Protocol" == "tcp"

# if len(sys.argv) != 4 :
#     print("Usage: %s host start_port end_port"%(sys.argv[0]))
#     sys.exit(0)

# host = str(sys.argv[1])
# start_port = int(sys.argv[2])
# end_port =  int(sys.argv[3])


host_address = "www.google.com"
start_port = 1
end_port = 85
open_ports = []

common_ports = {21, 22, 23, 25, 53, 69, 80, 88, 109, 119,
                123, 137, 138, 139, 143, 156, 161, 389, 443,
                445, 500, 546, 547, 587, 660, 995, 993, 2086,
                2087, 2082, 2083, 3306, 8443, 8080, 10000
                }

ip = socket.gethostbyname(host_address)

print('\nScanning ' + host_address + ' for all Common Ports\n')
print(socket.getfqdn(host_address))
print(socket.gethostname())
print(socket.gethostbyaddr(host_address))
print(socket.getaddrinfo(host_address, 80))


# print('\nScanning '+host_address+' for open TCP ports from port '+str(start_port)+' to '+str(end_port)+'\n')

start_time = time.time()

def prob_port(host_address, port, result=1):
    try:
        sock_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock_obj.settimeout(0.5)
        r = sock_obj.connect_ex((host_address, port))
        if r == 0:
            result = r
        sock_obj.close()

    except Exception as e:
        pass

    return


# for p in range(start_port, end_port + 1):
for p in sorted(common_ports):

    sys.stdout.flush()
    # print (p)     
    response = prob_port(host_address, p)
    if response == 0:
        open_ports.append(p)

        # print('Port '+str(p)+' is >>>>>>> Open') print(df.loc[np.logical_and(df['Port Number'] == str(p),
        # df['Transport Protocol'] == "tcp")])     # Select row for column "Port Number" = (p) and column "Transport
        # Protocol" == "tcp"

        df2 = (df.loc[np.logical_and(df['Port Number'] == str(p), df['Transport Protocol'] == "tcp")])  # Select row
        # for column "Port Number" = (p) and column "Transport Protocol" == "tcp"

        m_Port_Number = df2.loc[:, ["Port Number"]].to_string(index=None, header=None)
        m_Transport_Protocol = df2.loc[:, ["Transport Protocol"]].to_string(index=None, header=None)
        m_Service_Name = df2.loc[:, ["Service Name"]].to_string(index=None, header=None)
        m_Description = df2.loc[:, ["Description"]].to_string(index=None, header=None)

        print(f'{m_Port_Number:6} ---> {m_Transport_Protocol:5} ---> {m_Service_Name:10} ---> {m_Description}')

    else:
        # print('Port ' +str(p)+' is Closed')
        pass

    #     if not p == end_port:
#         sys.stdout.write('\b' * len(str(p)))

if open_ports:
    print("\n\nOpen Ports Found: -----> ", sorted(open_ports))
else:
    print("Sorry, No open ports found.!!")

print('\nTotal Time to Execute = %s' % (time.time() - start_time) + ' Seconds')

# for x in range(start_port, end_port+1):
#     packet = IP(dst=host_address)/TCP(dport=x, flags='S')
#     response = sr1(packet,timeout=0.5,verbose=0)
#     if response == None:
# print('Port ' +str(x)+' is Closed')
#            continue
#     else:
# print('Port '+str(x)+' is >>>>>>> Open')
#         if response.haslayer(TCP) and response.getlayer(TCP).flags==0x12:
#             print('Port '+str(x)+' is open')
#         sr(IP(dst=host_address)/TCP(dport=response.sport,flags='R'),timeout=0.5,verbose=0)
# except Exception as e:
#     print(e)

print('\nScan is Complete !!!!!\n')

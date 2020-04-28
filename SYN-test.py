from scapy.all import *

# common_ports = [21, 22, 23, 25, 53, 69, 80, 88, 109, 119,
#                 123, 137, 138, 139, 143, 156, 161, 389, 443,
#                 445, 500, 546, 547, 587, 660, 995, 993, 2086,
#                 2087, 2082, 2083, 3306, 8443, 8080, 10000
#                 ]

common_ports = [21, 80, 443]

sr(IP(dst="72.14.207.99")/TCP(dport=common_ports,flags="S"))

ans, unans = _
ans.summary()

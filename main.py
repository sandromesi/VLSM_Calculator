
#https://docs.python.org/3/library/ipaddress.html

#print host available
""" net4 = ipaddress.ip_network("192.0.2.0/28")

for x in net4.hosts():
    print(x) """

from subnet import Subnet
import ipaddress
import math

""" #PRINT SUBNET
def printSubnet(hostBit, cidr, name, network, broadcast, firstHost, lastHost, totalHosts):
    print(f"\nHost Bits: {hostBit}")
    print(f"\nName: {name}")
    print(f"Network address: {network}/{cidr}")
    print(f"Broadcast address: {broadcast}/{cidr}")
    print(f"First usable address: {firstHost}/{cidr}")
    print(f"Last usable address: {lastHost}/{cidr}")
    print(f"Total number of usable hosts addresses: {totalHosts}")
    print("__________________________________________________________________")

########## INPUTS ##########
assignedNetwork = ipaddress.ip_network("192.168.1.0/24")
maxAddresses = assignedNetwork.num_addresses

name = "Tokyo LAN A"
numHosts = 110

hostBit = math.ceil(math.log((numHosts + 2), 2))

cidr = 32 - hostBit

subnet = ipaddress.ip_network(str(assignedNetwork.network_address) + "/" + str(cidr)) 
network = subnet.network_address
broadcast = subnet.broadcast_address
firstHost = ipaddress.IPv4Address(network + 1)
lastHost = ipaddress.IPv4Address(broadcast - 1)
totalHosts = subnet.num_addresses - 2

nextSubnet = ipaddress.IPv4Address(broadcast + 1)

#########################################################################################################

name2 = "Toronto LAN B"
numHosts2 = 45

hostBit2 = math.ceil(math.log((numHosts2 + 2), 2))

cidr2 = 32 - hostBit2

subnet2 = ipaddress.ip_network(str(ipaddress.IPv4Address(broadcast + 1)) + "/" + str(cidr2)) 
network2 = subnet2.network_address
broadcast2 = subnet2.broadcast_address
firstHost2 = ipaddress.IPv4Address(network2 + 1)
lastHost2 = ipaddress.IPv4Address(broadcast2 - 1)
totalHosts2 = subnet2.num_addresses - 2

nextSubnet2 = ipaddress.IPv4Address(broadcast2 + 1)

#########################################################################################################

name3 = "Toronto LAN A"
numHosts3 = 29

hostBit3 = math.ceil(math.log((numHosts3 + 2), 2))

cidr3 = 32 - hostBit3

subnet3 = ipaddress.ip_network(str(ipaddress.IPv4Address(broadcast2 + 1)) + "/" + str(cidr3)) 
network3 = subnet3.network_address
broadcast3 = subnet3.broadcast_address
firstHost3 = ipaddress.IPv4Address(network3 + 1)
lastHost3 = ipaddress.IPv4Address(broadcast3 - 1)
totalHosts3 = subnet3.num_addresses - 2

nextSubnet3 = ipaddress.IPv4Address(broadcast3 + 1)

#########################################################################################################

name4 = "Tokyo LAN B"
numHosts4 = 8

hostBit4 = math.ceil(math.log((numHosts4 + 2), 2))

cidr4 = 32 - hostBit4

subnet4 = ipaddress.ip_network(str(ipaddress.IPv4Address(broadcast3 + 1)) + "/" + str(cidr4)) 
network4 = subnet4.network_address
broadcast4 = subnet4.broadcast_address
firstHost4 = ipaddress.IPv4Address(network4 + 1)
lastHost4 = ipaddress.IPv4Address(broadcast4 - 1)
totalHosts4 = subnet4.num_addresses - 2

nextSubnet4 = ipaddress.IPv4Address(broadcast4 + 1)

#########################################################################################################

name5 = "Point-to-point connection"
numHosts5 = 2

hostBit5 = math.ceil(math.log((numHosts5 + 2), 2))

cidr5 = 32 - hostBit5

subnet5 = ipaddress.ip_network(str(ipaddress.IPv4Address(broadcast4 + 1)) + "/" + str(cidr5)) 
network5 = subnet5.network_address
broadcast5 = subnet5.broadcast_address
firstHost5 = ipaddress.IPv4Address(network5 + 1)
lastHost5 = ipaddress.IPv4Address(broadcast5 - 1)
totalHosts5 = subnet5.num_addresses - 2

nextSubnet5 = ipaddress.IPv4Address(broadcast5 + 1)

#########################################################################################################

print(f"\nAssigned Network: {assignedNetwork}")
print("__________________________________________________________________")

printSubnet(hostBit, cidr, name, network, broadcast, firstHost, lastHost, totalHosts)
printSubnet(hostBit2, cidr2, name2, network2, broadcast2, firstHost2, lastHost2, totalHosts2)
printSubnet(hostBit3, cidr3, name3, network3, broadcast3, firstHost3, lastHost3, totalHosts3)
printSubnet(hostBit4, cidr4, name4, network4, broadcast4, firstHost4, lastHost4, totalHosts4)
printSubnet(hostBit5, cidr5, name5, network5, broadcast5, firstHost5, lastHost5, totalHosts5) """

Lan1 = Subnet.createSubnet("Tokyo LAN A", 110)
Lan2 = Subnet.createSubnet("Toronto LAN B", 45)
Lan3 = Subnet.createSubnet("Toronto LAN A", 29)
Lan4 = Subnet.createSubnet("Tokyo LAN B", 8)
Lan5 = Subnet.createSubnet("Point-to-point connection", 2)

Subnet.printSubnet(Lan1)
Subnet.printSubnet(Lan2)
Subnet.printSubnet(Lan3)
Subnet.printSubnet(Lan4)
Subnet.printSubnet(Lan5)




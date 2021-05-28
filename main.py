
#https://docs.python.org/3/library/ipaddress.html

from subnet import Subnet
import ipaddress
import math
import operator

""" Lan1 = Subnet.createSubnet("Tokyo LAN A", 110)
Lan2 = Subnet.createSubnet("Toronto LAN B", 45)
Lan3 = Subnet.createSubnet("Toronto LAN A", 29)
Lan4 = Subnet.createSubnet("Tokyo LAN B", 8)
Lan5 = Subnet.createSubnet("Point-to-point connection", 2)

Subnet.printSubnet(Lan1)
Subnet.printSubnet(Lan2)
Subnet.printSubnet(Lan3)
Subnet.printSubnet(Lan4)
Subnet.printSubnet(Lan5) """

Subnet.system()

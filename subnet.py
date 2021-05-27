
import ipaddress
import math 

assignedNetwork = ipaddress.ip_network("192.168.1.0/24")
maxAddresses = assignedNetwork.num_addresses
nextSubnet = ""
subnetCounter = maxAddresses
vlsm = {}

class Subnet:

    def __init__(self, name, cidr, network, broadcast, firstHost, lastHost, totalHosts):
        self.name = name
        self.cidr = cidr
        self.network = network
        self.broadcast = broadcast
        self.firstHost = firstHost
        self.lastHost = lastHost
        self.totalHosts = totalHosts

    #CREATE SUBNET
    def createSubnet(name, numHosts):
        global nextSubnet
        global subnetCounter
        global vlsm

        if 0 > subnetCounter - 6:
            print("\nYou have no more hosts left to assign!")

        elif numHosts > subnetCounter - 6:
            print(f"\nYou just have {subnetCounter - 6} host left to assign!")

        else: 
            hostBit = math.ceil(math.log((numHosts + 1), 2))

            cidr = 32 - hostBit

            if nextSubnet == "":
                subnet = ipaddress.ip_network(str(assignedNetwork.network_address) + "/" + str(cidr))
            
            else:
                subnet = ipaddress.ip_network(str(nextSubnet) + "/" + str(cidr))

            network = subnet.network_address
            broadcast = subnet.broadcast_address
            firstHost = ipaddress.IPv4Address(network + 1)
            lastHost = ipaddress.IPv4Address(broadcast - 1)
            totalHosts = subnet.num_addresses - 2

            nextSubnet = ipaddress.IPv4Address(broadcast + 1)

            newSubnet = Subnet(name, cidr, network, broadcast, firstHost, lastHost, totalHosts)

            subnetCounter = subnetCounter - subnet.num_addresses

            return newSubnet

    #PRINT SUBNET
    def printSubnet(object):
        print(f"\nName: {object.name}")
        print(f"Network address: {object.network}/{object.cidr}")
        print(f"Broadcast address: {object.broadcast}/{object.cidr}")
        print(f"First usable address: {object.firstHost}/{object.cidr}")
        print(f"Last usable address: {object.lastHost}/{object.cidr}")
        print(f"Total number of usable hosts addresses: {object.totalHosts}")
        print("__________________________________________________________________")    
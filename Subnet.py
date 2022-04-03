
import ipaddress
import math
import operator
from db import Db

assignedNetwork = "" #ipaddress.ip_network("192.168.1.0/24")
maxAddresses = "" #assignedNetwork.num_addresses
nextSubnet = ""
subnetCounter = "" #maxAddresses - 2
subnetDict = {}
subnetList = []

class Subnet:
    #CONSTRUCTOR
    def __init__(self, name, cidr, network, broadcast, firstHost, lastHost, totalHosts):

        self.name = name
        self.cidr = cidr
        self.network = network
        self.broadcast = broadcast
        self.firstHost = firstHost
        self.lastHost = lastHost
        self.totalHosts = totalHosts

    #NETWORK INPUT
    def networkInput():

        global assignedNetwork
        global maxAddresses
        global subnetCounter

        while True:
            try:
                print("\nPlease, enter the IpV4 network address with the subnet mask in CIDR notation to be assigned.")
                assignedNetwork = ipaddress.ip_network(input("     example: 192.168.1.0/24\n"))
                maxAddresses = assignedNetwork.num_addresses
                subnetCounter = maxAddresses - 2
                break                                 
            except:
                print("\nIpV4 Network Address and/or Subnet mask Address invalid!")

    #ADD NAME AND HOST NUMBER TO A DICTIONARY
    def addToDict(name, numHosts):

        global subnetDict

        subnetDict.update({name:numHosts})

    #SORT A DICTIONARY BY VALUE IN DECREASING ORDER
    def sortDict():
        global subnetDict

        sortedSubnetDict = dict( sorted(subnetDict.items(), key=operator.itemgetter(1),reverse=True))

        return sortedSubnetDict

    #CREATE SUBNET
    def createSubnet(subnetDict):

        global nextSubnet
        global subnetList

        for key, value in subnetDict.items():
            
            name = key
            numHosts = value    
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

            subnetList.append(newSubnet)
            
            Subnet.printSubnet(newSubnet)

            Db.writeFile(newSubnet)

    #NAME INPUT      
    def nameInput():

        name = input("\nType the subnet name: ")

        return name
    
    #HOST NUMBERS INPUT
    def hostNumInput(name):

        global subnetCounter

        while True:

            try:
                numHosts = int(input(f"\nHow many hosts does {name} need? "))

                if numHosts <= 0:
                    print("\nPlease, type numbers greater than zero.")

                elif numHosts > subnetCounter:
                    print(f"\nYou just have {subnetCounter} host left to assign!")
                
                else:
                    subnetCounter = subnetCounter - (2**(math.ceil(math.log((numHosts + 1), 2))))
                    subnetDict.update({name:numHosts})
                                       
                    break                                 
            except:
                print("\nOnly numbers are allowed.")

        Subnet.addQuestion()

    #ASK TO ADD ANOTHER SUBNET
    def addQuestion():

        answer = input("Do you want add another subnet? (s/n): ")

        if answer == "s":

            if subnetCounter < 2:
                print("\nYou have no more hosts left to assign!")
                sortedSubnetDict = Subnet.sortDict()
                Subnet.createSubnet(sortedSubnetDict)

            else:
                name = Subnet.nameInput()
                Subnet.hostNumInput(name)
            
        elif answer == "n":
            sortedSubnetDict = Subnet.sortDict()
            Subnet.createSubnet(sortedSubnetDict)

        else:
            print("Please, type \"s\" or \"n\" only.")
  
    #PRINT SUBNET
    def printSubnet(object):
        print(f"\nName: {object.name}")
        print(f"Network address: {object.network}/{object.cidr}")
        print(f"Broadcast address: {object.broadcast}/{object.cidr}")
        print(f"First usable address: {object.firstHost}/{object.cidr}")
        print(f"Last usable address: {object.lastHost}/{object.cidr}")
        print(f"Total number of usable hosts addresses: {object.totalHosts}")
        print("__________________________________________________________________")    


import ipaddress
import math
import operator

assignedNetwork = ipaddress.ip_network("192.168.1.0/24")
maxAddresses = assignedNetwork.num_addresses
nextSubnet = ""
subnetCounter = maxAddresses
subnetDict = {}
subnetList = []

class Subnet:

    def __init__(self, name, cidr, network, broadcast, firstHost, lastHost, totalHosts):
        self.name = name
        self.cidr = cidr
        self.network = network
        self.broadcast = broadcast
        self.firstHost = firstHost
        self.lastHost = lastHost
        self.totalHosts = totalHosts

    #ADD NAME AND HOST NUMBER TO A DICTIONARY
    def addToDict(name, numHosts):
        global subnetDict
        subnetDict.update({name:numHosts})

    #SORT A DICTIONARY BY VALUE IN DECREASING ORDER
    def sortDict():
        global subnetDict
        print("---------------------------------------------- inside sortDict")
        sortedSubnetDict = dict( sorted(subnetDict.items(), key=operator.itemgetter(1),reverse=True))
        return sortedSubnetDict

    #CREATE SUBNET
    def createSubnet(subnetDict):
        global nextSubnet
        global subnetList

        #for i in subnetDict:
            #name = list(subnetDict)[i]
            #numHosts = list(subnetDict.values())[i]

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

    #SYSTEM
    def system():
        global subnetCounter
        global subnetDict
        Subnet.sysInput()
            
    def sysInput():
        global subnetCounter
        print(f"couter: {subnetCounter}")
        name = input("\nType the subnet name: ")
        
        while True:
            try:
                print("---------------------------------------------- inside while - sysInput")
                numHosts = int(input(f"\nHow many hosts does {name} need? "))

                if numHosts <= 0:
                    print("---------------------------------------------- inside while  - sysInput - if")
                    print("\nPlease, type numbers greater than zero.")

                elif numHosts > subnetCounter - 6:
                    print("---------------------------------------------- inside while - sysInput - elif")
                    print(f"\nYou just have {subnetCounter - 6} host left to assign!")
                
                else:
                    print("---------------------------------------------- inside while - sysInput - else")
                    subnetCounter = subnetCounter - (2**(math.ceil(math.log((numHosts + 1), 2))))
                    print(f"couter: {subnetCounter}")
                    subnetDict.update({name:numHosts})
                    print(f"subnetDict: {subnetDict}")
                    break                                 
            except:
                print("---------------------------------------------- inside - sysInput - except")
                print("\nOnly numbers are allowed.")

        Subnet.addQuestion()

    def addQuestion():
        print("---------------------------------------------- inside addQuestion")

        answer = input("Do you want add another subnet? (s/n): ")

        if answer == "s":
            print(answer)
            print("---------------------------------------------- inside addQuestion - s if")
            if subnetCounter - 6 < 0:
                print("\nYou have no more hosts left to assign!")
                print(f"subnetDict: {subnetDict}")
                sortedSubnetDict = Subnet.sortDict()
                print(f"SORTED subnetDict: {sortedSubnetDict}")
                Subnet.createSubnet(sortedSubnetDict)

            else:
                Subnet.sysInput()
            
        elif answer == "n":
            print(answer)
            print("---------------------------------------------- inside addQuestion - n elif")
            print(f"subnetDict: {subnetDict}")
            sortedSubnetDict = Subnet.sortDict()
            print(f"SORTED subnetDict: {sortedSubnetDict}")
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
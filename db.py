class Db:

    def writeFile(object):
        file = open("vlsm.txt", "a+")
        file.write(f"Name: {object.name}\n")
        file.write(f"Network address: {object.network}/{object.cidr}\n")
        file.write(f"Broadcast address: {object.broadcast}/{object.cidr}\n")
        file.write(f"First usable address: {object.firstHost}/{object.cidr}\n")
        file.write(f"Last usable address: {object.lastHost}/{object.cidr}\n")
        file.write(f"Total number of usable hosts addresses: {object.totalHosts}\n")
        file.write("__________________________________________________________________\n")  
        file.close()


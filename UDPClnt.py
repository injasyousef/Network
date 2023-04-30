from socket import * 
import time 
# set the initial time 
startTime = time.time()

# define the server Port , Name(IP)  and address (IP,Port)
serverPort = 12000
serverName = '127.0.0.1'
serverAddress = (serverName,serverPort)

# create the client udp socket
clientSocket = socket(AF_INET,SOCK_DGRAM)

# continouslysend the data into the server
for i in range(1000001) :
    clientSocket.sendto(str(i).encode("UTF-8"),serverAddress)
    print(f" {i} SENT")

# get the final time 
endTime = time.time()
finalTime = endTime - startTime 
print(f"DATA SENT AFTER APPROXIMATELY {finalTime} SECONDS")

end = input("Enter to Exit")

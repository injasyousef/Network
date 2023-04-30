# This Is For Part Two - TCP Client (Abdullah Sami Naser 1201952 - Yousef Ali&Ahmad Jabra)
from socket import *
import time 

# define the server Name(IP) and the Server Port 
serverName = '192.168.1.215'
serverPort = 12000

# get the start time 
startTime = time.time()

# for each number , open a TCP Connection Socket 
# Send the Number , and wait for a response from the server with the number that sent 
# after that close the TCP for the number and repeat these steps again for a new number 
for i in range(1000001) :
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    clientSocket.send(str(i).encode())
    AcceptMSG = clientSocket.recv(1024).decode()
    print(AcceptMSG)
    clientSocket.close()

finalTime = time.time() - startTime
print("*" *50)
print(f"PROCESS DONE AFTER ABOUT {finalTime} SECONDS ")
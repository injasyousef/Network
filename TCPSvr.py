# This is For Part Two - TCP Server 
from socket import *

# Define the server Port 
serverPort = 12000

# create the server TCP Welcoming Socket and bind it to the port Num.
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))

# listen for incoming connections 
serverSocket.listen(1)
print ("TCP Server Is Ready To Receive")

# counter that will count the number of received messages 
count =0 
# deal with the connections 
# accept the connetion TCP 
# receive the data (number) and if the data is not empty increment the counter 
# and send this number to the client (ack)
# each number requires open a tcp connection socket and then close it 

while True:
     connectionSocket, addr = serverSocket.accept()
     data = connectionSocket.recv(1024).decode()
     if not data:
        break 
     count+=1
     print(f"RECEIVE {data} ==> COUNTER ==> {count} ")
     connectionSocket.send(f"ACCEPT THE MESSAGE {data.encode()} ".encode())
     connectionSocket.close()

serverSocket.close()
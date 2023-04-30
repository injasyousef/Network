from socket import * 

# create the server port and socket then bind the socket to it 
serverPort = 12000 
serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',serverPort))

# The server is ready 
print("The UDP Server Is Ready To Receive")
print("*" *50)

# counter that will incremented if a data reached 
count = 0

# Deal with data received 
while True : 
    data,addr=serverSocket.recvfrom(2048)
    data = data.decode("UTF-8")
    count+=1
    print(f"RECEIVED : {data} ===> COUNTER = {count} ")







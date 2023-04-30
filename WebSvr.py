from socket import * 
import os 
# change the current working directory into this directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# create server socket and the port 
serverPort = 7788
serverSocket = socket(AF_INET,SOCK_STREAM)

# bind the socket to the port 
serverSocket.bind(('',serverPort))

# listen to connections 
serverSocket.listen(1)
print("The Server Is Ready To Receive Connections")

# List of main files 
arList = ["main_ar.html" , "ar"]
enList = ["main_en.html" , "en" , "index.html" , ""]
otherList = ["go" , "so" , "bzu"]

# links dictionary
linksDict = {
    "go" : "https://google.com/",
    "so" : "https://stackoverflow.com/",
    "bzu" : "https://www.birzeit.edu/"
}
# Flag Tell If the file is opened 
fFlag = False 
# deal with connections 
while True: 
    print("Waiting for TCP connection")
    print("*" *50)
    connectionSocket,addr = serverSocket.accept()
    print(f"CONNECTED With Client With (IP = {addr[0]} , Port = {addr[1]}) ")
    print(">" *50)

    # read the data --> 2048 Byte Max
    data = connectionSocket.recv(2048)
    print(f"Receive From : (IP = {addr[0]} , Port = {addr[1]}) ")
    print(">" *50)

    # check if the data is sent data is empty or not 
    try:
        data = data.decode("UTF-8")
        print(f"Received Data :\n{data}")
    except: 
        print("No DATA Recieved")

    print("*" *50)
    # open the file specified in GET request and form response MSG 

    # if the request message is as usual then split it to get the file
    try:
        dataLine = data.split(" ")
        req = dataLine[1][1:]
    # otherwise, handle the exception and make the requested is anything "en for example"
    except:
        req ="en"
    print("*" *50)
    print(f"This is The Request:  {req}")

    # check to find the file name
    if req in enList:
        fName = "main_en.html"
    elif req in arList:
        fName = "main_ar.html"
    # if the request is the redirect
    elif req in otherList:
        fName = "main_en.html"
    # if the request is only .css or .jpg then return any css file and any image
    elif req == '.css':
        fName="enStyling.css"
    elif req == '.jpg':
        fName=='space.jpg'
    # otherwise, then receive the request and make the file name to it
    else : 
        fName =req 
    
    # try to open the file 
    try:
        file = open(fName,"rb") #if file does not exist it will produce error so i handle it
        fFlag = True #the file opened successfylly
    # the handle is to display a simple webpage error 404
    except : 
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode("UTF-8"))
        connectionSocket.send("Content-Type: text/html \r\n".encode("UTF-8"))
        responseMsg = ("""
        <html>
    <head>
        <title> Error Page</title>
        <link rel="icon" href="data:,">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Seymour+One&display=swap" rel="stylesheet">
        <style>
            * {
                padding: 0;
                margin: 0;
                
            }
            .main {
                width: 100%;
                text-align: center;
                color: red;
                margin-top: 80px;
                padding-bottom: 40px;
                font-family: 'Seymour One', sans-serif;

            }
            .main-img {
                width: 80px;
                height: 80px;
            }
            .line {
                border: 2px solid black;
            }

            .ids {
                font-family: Arial, Helvetica, sans-serif;
                font-size: 16px;
                font-weight: bold;
                margin-top: 20px;
                text-align: center;
                margin-bottom: 20px;
            }
        </style>
    </head>
    <body>
        <div class="main">
            <img class="main-img" src="error.png" alt="ERROR">
            <h1>ERROR: 404 Not Found</h2>
        </div>
        <hr class="line" />
        <div class="ids">
            <a href="main_en.html" title="Main Page">Did You mean English WebPage?</a>
            <p>Abdullah Sami Naser - 1201952</p>
            <p>Yousef Ali Injas - 1200643</p>
            <p>Ahmad Jabra - 1202450</p>
        </div>
        <hr class="line" />
        <div class="ids">
            <p>Client Adders (IP,PORT) : 
       
       
        """+ f"({addr[0] , addr[1]})" +"</p> </div> </body> </html>").encode("UTF-8")
    else: 
        responseMsg = file.read() #form the response msg body 
    
    #  send the proper headers only if the file is opened succefylly
    if fFlag :
        if req in otherList:
            connectionSocket.send("HTTP/1.1 307 Temporary Redirect\r\n".encode("UTF-8"))
            connectionSocket.send(f"Location: {linksDict.get(req)} \r\n".encode("UTF-8"))
        else : 
            connectionSocket.send("HTTP/1.1 200 OK\r\n".encode("UTF-8"))

        # send the proper headers in the HTTP response MSG
        if req.endswith(".jpg") :
            connectionSocket.send("Content-Type: image/jpeg \r\n".encode("UTF-8"))
        elif req.endswith(".png") :
            connectionSocket.send("Content-Type: image/png \r\n".encode("UTF-8"))
        elif req.endswith(".css") :
            connectionSocket.send("Content-Type: text/css \r\n".encode("UTF-8")) 
        else :
            connectionSocket.send("Content-Type: text/html \r\n".encode("UTF-8")) 
    # end the headers
    connectionSocket.send("\r\n".encode("UTF-8"))
    # send the message body
    connectionSocket.send(responseMsg)
    connectionSocket.close()


    


   























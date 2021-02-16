# Packages
import socket
import threading

# Protocol Using
myprotocol = socket.AF_INET

# Family Network Name 
myFamilyNetworkName = socket.SOCK_DGRAM

# Create a socket Format like Netwrk protocol and family
s = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )

ip = "192.168.43.246"
port = 1231

# Bind(Connect Port to IP) IP and PORT
#s.bind(( ip, port ))

print("\n\t\t\tGroup Chat\n")

# This will sends a message to mentioned OS 
def sendToAll1():
    # this will tune on even after sending message
    while True:
        # Type a messgae
        x = input("")
        # Give a OS IP in string  and PORT in digit numbers
        # Example s.sendto( "message".encode(), ( "IP", PORT_Number )
        # message should be encoded(message should be BYTE TYPE) due to network can only recieve byte type
        s.sendto("{}".format(x).encode(), ("172.17.0.2", 2222))
        #s.sendto("{}".format(x).encode(), ("192.168.43.254", 1234))
        s.sendto("{}".format(x).encode(), ("192.168.43.89", 1234))
                
# Sends Message If first thread is busy this helps like can sends multiple images or chats if one takes time to load than rest messages will be  sending
# Optional Extra Added
def sendToAll2():
    # this will tune on even after sending message
    while True:
        # Type a messgae
        x = input("")
        # Give a OS IP in string  and PORT in digit numbers
        # Example s.sendto( "message".encode(), ( "IP", PORT_Number )
        # message should be encoded(message should be BYTE TYPE) due to network can only recieve byte type
        #s.sendto("{}".format(x).encode(), ("192.168.43.254", 32768))
        s.sendto("{}".format(x).encode(), ("172.17.0.2", 2222))
        #s.sendto("{}".format(x).encode(), ("192.168.43.89", 1234))
        
        
# Recieves Message
def recieve1():
    # Create a socket Format like Netwrk protocol and family
    s = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )

    ip = "192.168.43.246"
    port = 1231

    # Bind(Connect Port to IP) IP and PORT
    s.bind(( ip, port ))
    while True:
        # Recieves message of  max 2MiB(1024Bytes) of message
        x = s.recvfrom(1024)
        # x[1][0] => IP of message Sender( even we can give name instead of IP)
        # x[0] => Message sent by Client (needs to be decoded due to client send in byte type so needs to convert orginal format)
        msg = "Message from {} : {}".format(x[1][0],x[0].decode())
        # Printing Message (Even we can return this to web page n can make a API chat app)
        print(msg)
        
        
# Multi Threading 
# one threads to recieve
recieving1 = threading.Thread( target = recieve1 )
# Two threads to send
sendChat1 = threading.Thread( target = sendToAll1 )
sendChat2 = threading.Thread( target = sendToAll2 )

# To start Threads  
sendChat1.start()
sendChat2.start()
recieving1.start()
                                           
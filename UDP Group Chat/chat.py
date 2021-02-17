# Packages
import socket
import threading
import os
import subprocess
myprotocol = socket.AF_INET # Protocol Using
myFamilyNetworkName = socket.SOCK_DGRAM  # Family Network Name 
previus = str()
os.system("tput setaf 39")
# Create a socket Format like Netwrk protocol and family
s = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
print("\n{}Group Chat\n".format("\t"*5))
def sendToAll1():  # This will sends a message to mentioned OS 
    while True: # this will tune on even after sending message
        global previus
        message = input("")   # Type a messgae
        print("\t"*2+subprocess.getoutput('date "+%I:%M %p"'))
        previus = " "
        if message == "" or message == " ":
            print("You are trying to send Empty Message")
            print("If you wanna stop CPNVERSATION press CTRL+C")
        # Give a OS IP in string  and PORT in digit numbers
        # Example s.sendto( "message".encode(), ( "IP", PORT_Number )
        # message should be encoded(message should be BYTE TYPE) due to network can only recieve byte type
        #s.sendto("{}".format(message).encode(), ("172.17.0.2", 2222))
        #s.sendto("{}".format(message).encode(), ("192.168.43.254", 1234))
        s.sendto("{}".format(message).encode(), ("192.168.43.89", 1234))
        os.system("tput setaf 39")
                
# Sends Message If first thread is busy this helps like can sends multiple images or chats if one takes time to load than rest messages will be  sending
# Optional Extra Added
def sendToAll1():  # This will sends a message to mentioned OS 
    while True: # this will tune on even after sending message
        global previus
        message = input("")   # Type a messgae
        print("\t"*2+subprocess.getoutput('date "+%I:%M %p"'))
        previus = " "
        if message == "" or message == " ":
            print("You are trying to send Empty Message")
            print("If you wanna stop CPNVERSATION press CTRL+C")
        # Give a OS IP in string  and PORT in digit numbers
        # Example s.sendto( "message".encode(), ( "IP", PORT_Number )
        # message should be encoded(message should be BYTE TYPE) due to network can only recieve byte type
        #s.sendto("{}".format(message).encode(), ("172.17.0.2", 2222))
        #s.sendto("{}".format(message).encode(), ("192.168.43.254", 1234))
        s.sendto("{}".format(message).encode(), ("192.168.43.89", 1234))
        
def recieve():   # Recieves Message
    # Create a socket Format like Netwrk protocol and family
    s = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
    ip = "192.168.43.149"
    port = 1111
    s.bind(( ip, port ))    # Bind(Connect Port to IP) IP and PORT
    while True:
        os.system("tput setaf 46")
        global previus
        message = s.recvfrom(1024)        # Recieves message of  max 2MiB(1024Bytes) of message
        time = subprocess.getoutput('date "+%I:%M %p"')
        if previus == message[1][0]:
            msg = "{}{}\n{}{}{}".format("\t"*5,message[0].decode(),"\t"*8,"\b"*2,time)
        else:
            # x[1][0] => IP of message Sender( even we can give name instead of IP)
            # x[0] => Message sent by Client (needs to be decoded due to client send in byte type so needs to convert orginal format)
            previus = message[1][0]
            msg = "{}Message from \U0001F464 {} \n{}{}\n{}{}{}".format("\t"*5,previus,"\t"*5,message[0].decode(),"\t"*8,"\b"*2,time)
            
        # Printing Message (Even we can return this to web page n can make a API chat app)
        print(msg)
        os.system("tput setaf 39")
        
# Multi Threading 
# one threads to recieve
recieving = threading.Thread( target = recieve )
# Two threads to send
sendChat1 = threading.Thread( target = sendToAll1 )
sendChat2 = threading.Thread( target = sendToAll2 )
# Threads To start  
sendChat1.start()
sendChat2.start()
recieving.start()
threading.Event().set() #Stop all Threads
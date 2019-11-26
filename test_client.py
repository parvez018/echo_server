# Import socket module
import socket               
import sys
# Create a socket object
s = socket.socket()         
 
# Define the port on which you want to connect
port = 1234           
 
# connect to the server on local computer
s.connect(('127.0.0.1', port))
 
# receive data from the server
msg=raw_input("Enter your message >>> ")
while True:
    try:
        s.sendall(msg)
        # print s.recv(1024)
        msg=raw_input("Enter your message >>> ")
    except socket.error:
        print 'Send failed'
        sys.exit()
# close the connection
s.close()      


def clientthread(conn):
    #Sending message to connected client
    conn.send('Welcome to the server. Type something and hit enter\n') #send only takes string
     
    #infinite loop so that function do not terminate and thread do not end.
    while True:
         
        #Receiving from client
        data = conn.recv(1024)
        reply = 'OK...' + data
        if not data: 
            break
     
        conn.sendall(reply)
    #came out of loop
    conn.close()
# message = raw_input('Sladu inn skipun :')
#     try :
#         s.sendall(message)
#         print s.recv(1024)
#     except socket.error:
#         print 'Send failed'
#         sys.exit()
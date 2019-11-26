# sudo kill -9 PID
# lsof -i :PORT

# first of all import the socket library
import socket 
from thread import start_new_thread              
 
# next create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)       
print "Socket successfully created"
 
# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 1234               
 
# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests 
# coming from other computers on the network
s.bind(('', port))        
print "socket binded to %s" %(port)
 
# put the socket into listening mode
# max
s.listen(5)     
print "socket is listening"           
 
# a forever loop until we interrupt it or 
# an error occurs
# c = 0
# Establish connection with client.
def clientthread(conn,addr):
    #Sending message to connected client
    conn.sendall('Welcome to the localhost server.\n') #send only takes string
    #infinite loop so that function do not terminate and thread do not end.
    while True:
        #Receiving from client
        try:
            msg=conn.recv(1024)
            if(not msg): 
                break
            print "received -- "+addr[0]+":"+str(addr[1])+" -- msg:"+msg
            conn.send(msg)
        except socket.error:
            print "socket error"
            break
        # data = conn.recv(1024)
        # reply = 'OK...' + data
        # if not data: 
        #     break
     
        # conn.sendall(reply)
    #came out of loop
    conn.close()


while True:
    connection, addr = s.accept()
    print 'Connection from ', addr[0],":",addr[1]
    start_new_thread(clientthread ,(connection,addr))
# while True:   
#     try:     
#         msg=c.recv(1024)
#         if(not msg): 
#             break
#         print "received -- "+msg
#         c.send(msg)
#     except socket.error:
#         print "socket error"
#         break
    # send a thank you message to the client. 
 
# Close the connection with the client
# c.close()


    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
     
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    
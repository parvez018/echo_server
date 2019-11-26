# python server.py [portno]
# Message from [client IP, client Port]: [msg]
import socket 
from thread import start_new_thread 
class Server:
    def __init__(self,port):
        self.port=port
    def clientthread(self,connection,addr):
        connection.sendall('Welcome to the localhost server.\n')
        while True:
            try:
                msg=connection.recv(1024)
                if(not msg): 
                    break
                print "Message from [",addr[0]," : ",addr[1],"]: [",msg,"]"
                connection.send(msg)
            except socket.error:
                print "socket error"
                break
        connection.close() 
    def start_listening(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
        self.sock.bind(('', self.port))
        self.sock.listen(5) 
        print "Server started at port: ",self.port
        while True:
            connection, addr = self.sock.accept()
            print 'Connection from ', addr[0],":",addr[1]
            start_new_thread(self.clientthread ,(connection,addr))
    


if __name__ == '__main__':
    import sys
    if(len(sys.argv)!=2):
        print("python server.py [portno]")
    else:
        s1=Server(int(sys.argv[1]))
        s1.start_listening()
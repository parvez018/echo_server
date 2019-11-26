# python client.py [serverIP] [serverPort]
import socket               
import sys
class Client:
    def __init__(self,ip,port):
        self.ip=ip
        self.port=int(port)
    def send(self):
        # msg=raw_input("Enter your message >>> ")
        self.sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.ip, self.port))
        msg=""
        while True:
            try:
                print self.sock.recv(1024)
                msg=raw_input("Enter your message >>> ")
                if(msg!="exit"):
                    self.sock.sendall(msg)
                else:
                    break        
            except socket.error:
                print 'Send failed'
                sys.exit()
        self.sock.close()
    def describe(self):
        print("ip:"+self.ip+" port:"+str(self.port))


if __name__ == '__main__':
    import sys
    if(len(sys.argv)!=3):
        print("python client.py [serverIP] [serverPort]")
    else:
        c1=Client(sys.argv[1],sys.argv[2])
        c1.send()
from Client import Client
from Server import Server

c1=Client(1)
c1.send("hello")

c2=Server(2)
c2.recv("hello world")

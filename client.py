import os

import socket

ip="192.168.43.161"
port=1234

while True:
    os.system("stty -echo")
    message=input()
    os.system("stty echo")
    clientsock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    clientsock.sendto(message.encode(),(ip,port))
    print("\t\t\t{}\n\t\t\t {}".format(ip,message))
    data,addr=clientsock.recvfrom(1024)
    output=data.decode()
    print("{}\n{}".format(ip,output))
    clientsock.close()


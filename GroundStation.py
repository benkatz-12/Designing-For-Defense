from scapy.all import *
import socket

port = 55555
file_num = 0

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as e:
    print("Socket Creation Failed with Error %s" %(e))

try:
    s.bind(('',port))
except socket.error as e:
    print("Socket Bind Failed with Error %s" %(e))

s.listen(5)

while 1:
    c, addr = s.accept()
    print('Connection from', addr)
    
    while 1:
        data = c.recv(4096).decode()
        if data.startswith('SIZE'):
            size = data
            size = size.strip('SIZE ')
            print(size)
            c.send('Size Recieved'.encode())
            fd = open('./GSImages/%s-%d.jpg' % (addr[0], file_num), 'wb')

            bytesrec = 0
            while bytesrec < int(size):
                data = c.recv(4096)
                if not data:
                    break
                bytesrec += len(data)
                fd.write(data)
            fd.close()
            file_num += 1
            break
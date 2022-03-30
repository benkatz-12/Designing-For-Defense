from scapy.all import *
import socket
import os
import time

host = '127.0.0.1'
port = 55555

def main():
    images = os.listdir('./SATImages')
    for i in images:
        send_image(i)
        time.sleep(10)

def send_image(image):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print("Socket Creation Failed with Error %s" %(e))

    try:
        s.connect((host, port))
    except socket.error as e:
        print("Connect Failed with Error %s" %(e))

    try:
        fd = open('./SATImages/%s' % image, 'rb')
        bytes = fd.read()
        size = len(bytes)

        msg = 'SIZE ' + str(size)
        s.sendall(msg.encode())
        rec = s.recv(1024)
        print(rec.decode())

        s.sendall(bytes)
    finally:
        s.close()

if __name__=="__main__":
    main()
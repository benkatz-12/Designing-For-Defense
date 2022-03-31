import socket
import os
import time
import hashlib

host = '127.0.0.1'
port = 55555

def main(): #iterate though SATImages and send one image every 10 seconds
    images = os.listdir('./SATImages')
    for i in images:
        send_image(i)
        time.sleep(10)

def send_image(image): #send image to Ground Station
    #connect to Ground Station
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print("Socket Creation Failed with Error %s" %(e))

    try:
        s.connect((host, port))
    except socket.error as e:
        print("Connect Failed with Error %s" %(e))

    #send Image
    try:
        #read in image from SATImages
        fd = open('./SATImages/%s' % image, 'rb')
        bytes = fd.read()

        #build packet
        size = len(bytes)
        msg = 'SIZE ' + str(size) + '\r\n'

        hash = hashlib.md5(bytes)
        msg += 'HASH ' + str(hash.hexdigest()) + '\r\n\r\n'

        #send packet
        s.sendall(msg.encode().ljust(128) + bytes) # pad to 128
    finally:
        s.close()

if __name__=="__main__":
    main()
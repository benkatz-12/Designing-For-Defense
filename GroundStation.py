import socket
import hashlib



def check_hash(file, hash): # String check sent hash to homemade hash
    fd = open(file, 'rb')
    bytes = fd.read()
    fd.close()
    if hashlib.md5(bytes).hexdigest() == hash:
        print('integrity is good')

def main():
    recv_all()

def recv_all():
    port = 55555
    file_num = 0

    try: # create listen socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print("Socket Creation Failed with Error %s" %(e))

    try: # bind socket
        s.bind(('',port))
    except socket.error as e:
        print("Socket Bind Failed with Error %s" %(e))

    s.listen(5) # up to 5 (# of sats) pending connections

    while 1: # accept loop
        c, addr = s.accept() # block unitl connection
        print('Connection from', addr)
        
        while 1:
            data = c.recv(128).decode() # decode header
            header = data.split('\r\n')
            size = header[0].strip('SIZE ')
            hash = header[1].strip('HASH ')
                    
            # create new file for storage
            file = './GSImages/%s-%d.jpg' % (addr[0], file_num)
            fd = open(file, 'wb')

            bytesrec = 0
            while bytesrec < int(size): # read in image data and save
                data = c.recv(4096)
                if not data:
                    break
                bytesrec += len(data)
                fd.write(data)
            fd.close()

            check_hash(file, hash) # integrity check

            file_num += 1
            break

if __name__ == "__main__":
    main()
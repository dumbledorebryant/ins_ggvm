"""
COSC435

Boning Zhang <bz176@georgetown.edu>
netid: bz176
Georgetown University

"""

import argparse
import socket


def main():
    parser = argparse.ArgumentParser()

    # add a required argument, which can either be specified
    # via -n or --name.  Store the result in a variable called "name"
    parser.add_argument('-p', '--port', dest = 'port', 
                                        help = 'connects to this port', 
                                        type = int, 
                                        required=True)

    # add a command-line argument that has no parameter -- i.e., it's true iff it's specified
    # note that "store_true" is a special string that tells argparse what to store if this
    # command-line argument is provided
    parser.add_argument('-r', '--reverse', dest='reverse', 
                                           help='reverse the input', 
                                           action="store_true")
    
    args = parser.parse_args()
    
    port = args.port
    reverse = args.reverse

    host = "127.0.0.1"
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (host, port)
    server.bind(address)
    server.listen(5)
    
    while(True):
        print("waiting")
        conn, addr = server.accept()
        while(True): 
            print("receving")
            data = conn.recv(1024)
            if data == b'': 
                break
            output = data.decode('utf-8')
            if reverse is True:
                output = output[::-1]
                bytesss = bytes(output, encoding='utf-8')
                bytesss = bytesss + '\n'.encode('utf-8')
                newbytes = bytesss[1:]
                conn.send(newbytes)
            else:
                conn.send(data)
            print("one message done")
    
    server.close()
    print("end")

if __name__ == '__main__':
    main()
    

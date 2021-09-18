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

    # via -p. Store the result in a variable called "port"
    parser.add_argument('-p', dest = 'port', 
                              help = 'connects to this port', 
                              type = int, 
                              required=True)

    # add a command-line argument that has no parameter -- i.e., it's true iff it's specified
    # note that "store_true" is a special string that tells argparse what to store if this
    parser.add_argument('-r', dest='reverse', 
                              help='reverse the input', 
                              action="store_true")
    
    # get all the args
    args = parser.parse_args()
    
    # get port number
    port = args.port

    # get reverse flag
    reverse = args.reverse

    # make the server waiting for a upcoming client
    host = "127.0.0.1"
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (host, port)
    server.bind(address)
    server.listen(5)
    
    while(True):

        # waiting start
        print("waiting")
        conn, addr = server.accept()

        while(True): 
            # receving start
            print("receving")
            data = conn.recv(1024)

            # check if the connection is broken
            if data == b'': 
                break

            # get the data from client
            output = data.decode('utf-8')

            # check if the output should be reversed or not
            if reverse is True:

                # reverse it
                output = output[::-1]

                bytesss = bytes(output, encoding='utf-8')
                bytesss = bytesss + '\n'.encode('utf-8')
                newbytes = bytesss[1:]
                conn.send(newbytes)
            
            else:
                # just send the original msg back
                conn.send(data)

            print("one message done")
    
    # shut down the server
    server.close()
    print("end")

if __name__ == '__main__':
    main()
    

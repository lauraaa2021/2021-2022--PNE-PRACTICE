import socket

# Configure the Server's IP and PORT
PORT = 22000
IP = "0000"
MAX_OPEN_REQUESTS = 5

# Counting the number of connections
number_con = 0

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # given that there are some types of sockets, we say that its an Ip socket and to connect to internet
try:
    serversocket.bind((IP, PORT)) # we bind the socket to one ip address existing in the computer and a port you want
    # become a server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        # accept connections from outside
        print("Waiting for connections at {}, {} ".format(IP, PORT))
        (clientsocket, address) = serversocket.accept() # that is going to print the clientsocket to communicate with the client and also the address of the client

        # Another connection!e
        number_con += 1

        # Print the conection number
        print("CONNECTION: {}. From the IP: {}".format(number_con, address))

        # Read the message from the client, if any and th 2048 is a number of bytes created in a server and we store info sent by client
        #we have received the info, y memory is 2048 and we decode that bytes into a string
        msg = clientsocket.recv(2048).decode("utf-8")
        print("Message from client: {}".format(msg)) # .format is just to separate  by commas, so you print message separated by commas

        # Send the message, we already have received the info from client and then we can send the info back to him through client socket, whcih can be used both for reading or writig info
        message = "Hello from the teacher's server"
        send_bytes = str.encode(message) # the string we want to send through client socket needs to be encoded into bytes and we use a method
        # We must write bytes, not a string
        clientsocket.send(send_bytes)
        clientsocket.close()

except socket.error:
    print("Problems using port {}. Do you have permission?".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()
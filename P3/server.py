import socket
from Seq1 import Seq

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Configure the Server's IP and PORT
PORT = 8080
IP = "127.0.0.1"

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")

while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listenning socket
        ls.close()

        # -- Exit!
        exit()

    # -- Execute this part if there are no errors
    else:

        print("A client has connected to the server!")

        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)

        # -- We decode it for converting it
        # -- into a human-redeable string
        msg = msg_raw.decode().replace("\n", "").strip()
        #remove spaces to the right and left

        splitted_command = msg.split(' ')
        cmd = splitted_command[0]
        print(splitted_command)
        if cmd != "PING":
            arg = splitted_command[1]
            print(arg)

        # -- Print the received message
        print(f"Message received: {msg}")

        # -- Send a response message to the client

        if cmd == "PING":
            response = "ok\n"
            print(response,"Ping command")
        elif cmd == "GET":
            seq_list = ["ACGTCT", "GGGGTTTC", "ACTACTAG","ATGCTGCT", "GCTCCCC"]
            response = seq_list[int(arg)]
            print(response)

        elif cmd == "INFO":
            response = Seq(arg).percentages()
            response_1 = Seq(arg).count_base()
            response = str(response) + str(response_1)


        elif cmd == "COMP":
            response = Seq(arg).complement()
            response = str(response)
            print(response)

        elif cmd == "REV":
            response = Seq(arg).reverse()
            response = str(response)
            print(response)

        elif cmd == "GENE":
            response = Seq()
            response.read_fasta(arg)
            response = str(response)
            print(response)

        elif cmd == "ADD":
            response = Seq(arg).add()
            response = str(response)
            print(response)

        else:
            response = "Hello from happy server"



        # -- The message has to be encoded into bytes
        cs.send(response.encode())


        # -- Close the data socket
        cs.close()
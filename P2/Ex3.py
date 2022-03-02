from Client0 import Client


PRACTICE = 2
EXERCISE = 1

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)
print(c)
print("Sending a message to the server...")
msg = "Testing!!!!"
response = c.talk(msg)
print(f"Response: {response}")

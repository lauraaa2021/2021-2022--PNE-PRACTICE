from Seq1 import Seq
from Client0 import Client

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8080
PORT1 = 8081

c = Client(IP, PORT)
c1 = Client(IP, PORT1)

s = Seq()
filename = "FRAT1"
s.read_fasta(filename)
msg = str(s)

i = 0
for e in range(1,11):
    i += 10
    msg_1 = msg[i-10:i]
    if e%2 == 0:
        response_1 = (f"Frag {e}: {msg_1}")
        response = c1.talk(response_1)
        print(filename + f"Response: {response}")
    else:
        response_1 = (f"Frag {e}: {msg_1}")
        response = c.talk(response_1)
        print(filename + f"Response: {response}")

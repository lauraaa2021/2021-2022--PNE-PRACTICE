from Seq1 import Seq
from Client0 import Client

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8080
c = Client(IP, PORT)
s = Seq()
filename = "FRAT1"
s.read_fasta(filename)
msg = str(s)

i = 0
for e in range(5):
    i += 10
    msg_1 = msg[i-10:i]
    response = c.talk(msg_1)
    print(filename + f"Response: {response}")
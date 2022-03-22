from Seq1 import Seq
from Client0 import Client


PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8081
c = Client(IP, PORT)

filename = ["U5","FRAT1", "ADA"]




for file in filename:
    msg = ("Sending " + file + " to the server")
    response_1 = c.talk(msg)
    s = Seq()
    s.read_fasta(file)
    print("Sending the", file, "to the server...")
    msg = str(s)
    response = c.talk(msg)
    print(file, f"Response: {response}")
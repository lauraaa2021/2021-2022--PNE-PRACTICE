from Client0 import Client
import termcolor

PRACTICE = 2
EXERCISE = 1

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)


ping = c.talk("PING")
termcolor.cprint("Print the ping command "+ ping, "green")


numbers = [0,1,2,3,4]
for n in numbers:
    response = c.talk("GET " + str(n))
    print(str(n) + ": " + response)

get_0 = c.talk("GET 0")
info = c.talk("INFO " + get_0)
print(info)

complement = c.talk("COMP " + get_0)
print("The complement sequence of: " + get_0 + "is " + complement)
reverse = c.talk("REV " + get_0)
print("The reverse sequence of: " + get_0 + "is " + reverse)

seq_list_1 = [ "ADA", "U5", "FRAT1", "RNU6_269P", "FXN"]
for name in seq_list_1:
    gene = c.talk("GENE " + name)
    print( "Printing " + name + ": " + gene)

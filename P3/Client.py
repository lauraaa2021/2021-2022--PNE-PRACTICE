from Client0 import Client

PRACTICE = 2
EXERCISE = 1

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)


ping = c.talk("PING")
print(ping)


numbers = [0,1,2,3,4]
for n in numbers:
    response = c.talk("GET " + str(n))
    print(response)

get_0 = c.talk("GET 0")
info = c.talk("INFO " + get_0)
print(info)
complement =c.talk("COMP " + get_0)
print(complement)
reverse = c.talk("REV " + get_0)
print(reverse)

seq_list_1 = []
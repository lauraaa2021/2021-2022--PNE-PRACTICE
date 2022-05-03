
# -- for requesting the main page from the server
import http.client
import json

SERVER = 'rest.ensembl.org'   #we always need these 3 strings
ENDPOINT = "/info/ping"
PARAMS = '?content-type=application/json'
print(f"\n Connecting to the server: {SERVER}\n")
#we don´t need the port because as we are working with an external server, then we just need the server to whcih we are going to be redirected to

# Connect with the server
conn = http.client.HTTPConnection(SERVER)
# -- Example of a client that uses the HTTP.client library
# -- for requesting the main page from the server

print(f"\nConnecting to server: {SERVER}\n")

# Connect with the server
conn = http.client.HTTPConnection(SERVER)


# do we need
# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", ENDPOINT + PARAMS)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode("utf-8")

# -- Print the received data
print(f"CONTENT: {data1}")
# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
data1 = json.loads(data1)  # we transform our previous data 1 string into a idctionary
# -- Print the received data
if data1["ping"] == 1:
    print("Ping ok")
else:
    print("Error")

# json loads
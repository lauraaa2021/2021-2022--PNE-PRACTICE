#Example of a client that uses the HTTP.client library
# -- for requesting the main page from the server
import http.client
import json
from Seq1 import Seq




gene_input = input("Gene: ")
#we don´t need the port because as we are working with an external server, then we just need the server to whcih we are going to be redirected to
genes_dict = {"SRCAP": "ENSG00000080603", "FRAT1":"ENSG00000165879", "ADA": "ENSG00000196839", "FXN": "ENSG00000165060", "RNU6_269P":"ENSG00000212379" , "MIR633" : "ENSG00000207588" , "TTTY4C": "ENS00000228296", "RBMY2YP": "ENSG00000227633","FGFR3":"ENSG00000068078", "KDR":"ENSG00000128052","ANK2":"ENSG00000145362"}
# Connect with the server
SERVER = 'rest.ensembl.org'   #we always need these 3 strings
ENDPOINT = '/sequence/id/' + genes_dict[gene_input]
PARAMS = '?content-type=application/json'
conn = http.client.HTTPConnection(SERVER)
# -- Example of a client that uses the HTTP.client library
# -- for requesting the main page from the server


print(f"\nConnecting to server: {SERVER}\n")
print("URL: " + ENDPOINT)

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
data1 = json.loads(data1)



print("GENE: " + gene_input)
print("Description: " + data1["desc"])
length = Seq(data1["seq"]).len()
print("Total length: " + str(length))
base_count = Seq(data1["seq"]).count()
percentage = Seq(data1["seq"]).percentages()
listing = ["A", "C", "G", "T"]
new_list = list(zip(base_count, percentage))
new_list_1 = list(zip(listing, new_list))
for k,v in new_list_1:
    print(k , ": " , v)
most_freq = base_count.seq_process(data1)
print(most_freq)






# -- Print the received data

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
 # we transform our previous data 1 string into a idctionary
# -- Print the received data

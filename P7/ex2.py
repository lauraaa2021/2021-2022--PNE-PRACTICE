# Example of a client that uses the HTTP.client library
# -- for requesting the main page from the server
import http.client
import json

SERVER = 'rest.ensembl.org'   #we always need these 3 strings
ENDPOINT = '/sequence/id/ENSG00000157764'
PARAMS = '?text/plain'


genes_dict = {"SRCAP": "ENSG00000080603", "FRAT1":"ENSG00000165879", "ADA": "ENSG00000196839", "FXN": "ENSG00000165060", "RNU6_269P":"ENSG00000212379" , "MIR633" : "ENSG00000207588" , "TTTY4C": "ENS00000228296", "RBMY2YP": "ENSG00000227633","FGFR3":"ENSG00000068078", "KDR":"ENSG00000128052","ANK2":"ENSG00000145362"}

for k,v in genes_dict.items():
    print( k +  " ---> "+ v)

    # Connect with the server
    conn = http.client.HTTPConnection(SERVER)
    # -- Example of a client that uses the HTTP.client library
    # -- for requesting the main page from the server



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


    # -- Read the response's body
    data1 = r1.read().decode("utf-8")

    # -- Print the received data

    # -- Send the request message, using the GET method. We are
    # -- requesting the main page (/)
     # we transform our previous data 1 string into a idctionary
    # -- Print the received data





import http.server
import socketserver
import termcolor
import pathlib
from Seq1 import Seq
import jinja2
from urllib.parse import urlparse, parse_qs
import http.client
import json

PORT = 8081



def server_call(url_parse, params=""):  #empleamos dos comillas porque los valores que le vamos a pasar pueden no ser de tio string
    SERVER = 'rest.ensembl.org' #el servidor de ensemble al que me conecto para coger la info
    params = '?content-type=application/json' + params    #los parámetros son valores que la función espera recibir cuando se la llame
    conn = http.client.HTTPConnection(SERVER) #establece la conexión
    print(f"\nConnecting to server: {SERVER}\n")
    print("URL: " + url_parse)
    try:
        conn.request("GET", url_parse + params)  #establecer conexión al endpoint dado y los parámetros que forman el url
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()
    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")
    data1 = r1.read().decode("utf-8")
    #decodifica el mensaje traído desde ensemble y lo convierte a un json que es un diccionario
    data1 = json.loads(data1)
    return data1   # el diccionario con los valores cogidos de ensemble



def read_html_file(filename):
    contents = pathlib.Path(filename).read_text()
    contents = jinja2.Template(contents)          # funcionalidad igual que con .format en string / es un objeto de clase template
    return contents                         #.format para strings y para jinja2 usamos render.


socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""
        print("GET received! Request line:")

        termcolor.cprint("  " + self.requestline, 'green')
        print("  Command: " + self.command)
        print("  Path: " + self.path)
        routes = self.requestline.split(" ")[1]

        url_parse = urlparse(self.path)  #el módulo url sirve para descomponer el url en partes y como una de las partes es path que es la ruta que queremos porque empieza por / pues seleccionamos self.path
        #print("urlparse", url_parse)
        arguments = parse_qs(url_parse.query)    # devuelve un diccionario con los valores de los argumentos
        print("arguments", arguments)
        path = url_parse.path    # el módulo url_parse coge la ruta sin la interrogación
        print("path: ", path)

        #try:
        if path == "/":
            contents = read_html_file("html/index.html").render()
        elif path == "/listSpecies":
            list_species = []
            ensemble_answer = server_call("/info/species")
            try:
                n_species = int(arguments["n_species"][0])
            except KeyError:
                n_species = len(ensemble_answer["species"])
            #print(ensemble_answer)
            for i in range(n_species):
                list_species.append(ensemble_answer["species"][i]["name"])
            contents = read_html_file("html/species.html").render(context={"species":list_species})
            #print(contents)
            print(list_species)
        elif path == "/karyotype":
            list_karyotypes = []
            species_karyo = arguments["species_karyo"][0]
            ensemble_answer = server_call("/info/assembly/" + species_karyo)
            list_karyotypes.append(ensemble_answer["karyotype"])
            contents = read_html_file("html/karyotype.html").render(context={"karyotype_list": ensemble_answer["karyotype"]})
        elif path == "/chromosomeLength":
            name_species = arguments["name_species"][0]
            chromosome = arguments["chromosome"][0]
            ensemble_answer = server_call("/info/assembly/" + name_species)
            print(ensemble_answer)
            length = 0
            for d in ensemble_answer["top_level_region"]:
                if d["coord_system"] == "chromosome" and d["name"] == chromosome:
                    length = d["length"]
            contents = read_html_file("html/chromosome.html").render(context={"length":length})
        elif path == "/favicon.ico":
            contents = read_html_file("html/index.html").render()
        else:
            filename = routes[1:]
            contents = pathlib.Path("html/" + filename + ".html").read_text()
        #except Exception as e:
            #contents = pathlib.Path("html/error.html").read_text()
            #print(e)

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        # IN this simple server version:
        # We are NOT processing the client's request
        # We are NOT generating any response message
        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()
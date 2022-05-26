import http.server
import socketserver
import termcolor
from pathlib import Path
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
    return data1  # el diccionario con los valores cogidos de ensemble





def read_html_file(filename):
    contents = Path(filename).read_text()
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
        genes_dict = {"FRAT1": "ENSG00000165879", "ADA": "ENSG00000196839",
                      "FXN": "ENSG00000165060", "RNU6_269P": "ENSG00000212379", "MIR633": "ENSG00000207588",
                      "TTTY4C": "ENSG00000226906", "RBMY2YP": "ENSG00000227633", "FGFR3": "ENSG00000068078",
                      "KDR": "ENSG00000128052", "ANK2": "ENSG00000145362"}


        #BASIC LEVEL

        if path == "/":
            contents = read_html_file("html/index.html").render(context={"genes_dict": genes_dict})
        elif path == "/listSpecies":
            list_species = []
            ensemble_answer = server_call("/info/species")
            try:
                if "n_species" in arguments and int(arguments["n_species"][0]) <= len(ensemble_answer["species"]) :
                    n_species = int(arguments["n_species"][0])
                else:
                    n_species = len(ensemble_answer["species"])
                for i in range(n_species):
                    list_species.append(ensemble_answer["species"][i]["name"])
                context = {"species":list_species}
                contents = read_html_file("html/species.html").render(context=context)
            except ValueError:
                contents = read_html_file("html/error.html").render(context={"error":"Please introduce an integer number."})
        elif path == "/karyotype":
            try:
                list_karyotypes = []
                species_karyo = arguments["species_karyo"][0]
                ensemble_answer = server_call("/info/assembly/" + species_karyo)
                list_karyotypes.append(ensemble_answer["karyotype"])
                contents = read_html_file("html/karyotype.html").render(context={"karyotype_list": ensemble_answer["karyotype"]})
            except KeyError:
                contents = read_html_file("html/error.html").render(context={"error": "Please introduce valid species."})
        elif path == "/chromosomeLength":
            try:
                name_species = arguments["name_species"][0]
                chromosome = arguments["chromosome"][0]
                ensemble_answer = server_call("/info/assembly/" + name_species)
                length = 0
                for d in ensemble_answer["top_level_region"]:
                    if d["coord_system"] == "chromosome" and d["name"] == chromosome:
                        length = d["length"]
                if length == 0:
                    contents = read_html_file("html/error.html").render(context={"error": "Please introduce a correct chromosome number."})
                else:
                    contents = read_html_file("html/chromosome.html").render(context={"length":length})
            except KeyError:
                contents = read_html_file("html/error.html").render(context={"error": "Please introduce a valid key."})



        #MEDIUM LEVEL
        elif path == "/geneSeq":
           gene_name = arguments["gene"][0]
           gene_id = genes_dict[gene_name]
           ensemble_answer = server_call("/sequence/id/" + gene_id)
           contents = read_html_file("html/geneSeq.html").render(context={"gene_name": gene_name,"gene_sequence": ensemble_answer["seq"]})
        elif path == "/geneInfo":
            gene_name = arguments["gene"][0]
            gene_id = genes_dict[gene_name]
            ensemble_answer = server_call("/sequence/id/" + gene_id)
            try:
                chromosome = ensemble_answer["desc"].split(":")
                start_chromosome = chromosome[2]
                end_chromosome = chromosome[3]
                length = int(end_chromosome) - int(start_chromosome)
                contents = read_html_file("html/geneInfo.html").render(context={"gene_name": gene_name,"gene_id": gene_id, "start_chromosome": start_chromosome, "end_chromosome":end_chromosome, "length": length })
            except:
                contents = read_html_file("html/error.html").render(context={"error": "Sorry we are not able to find the information for that gene, choose another one."})
        elif path == "/geneCalc":
            try:
                gene_name = arguments["gene"][0]
                gene_id = genes_dict[gene_name]
                ensemble_answer = server_call("/sequence/id/" + gene_id)
                gene_sequence = ensemble_answer["seq"]
                chromosome = ensemble_answer["desc"].split(":")
                start_chromosome = chromosome[2]
                end_chromosome = chromosome[3]
                bases_list = ["A", "C", "G", "T"]
                s = Seq(gene_sequence)
                gene_percentages = s.percentages()
                list_percentages = []
                list_percentages.append(gene_percentages)
                list_percentages1 = list(zip(bases_list,gene_percentages))
                if start_chromosome or end_chromosome == int:
                    length = int(end_chromosome) - int(start_chromosome)
                    contents = read_html_file("html/geneCalc.html").render(context={"gene_name": gene_name, "gene_percentages": list_percentages1, "length": length})
                else:
                    contents = read_html_file("html/error.html").render(context={"error": "Sorry we haven´t been able to find the calculations."})
            except:
                contents = read_html_file("html/error.html").render(context={"error": "Sorry we haven´t been able to find the calculations."})
        elif path == "/geneList":
            try:
                chromo = arguments["chromo"][0]
                start = arguments["start_position"][0]
                end = arguments["end_position"][0]
                ensemble_answer = server_call("/phenotype/region/homo_sapiens/" + chromo + ":" + start + "-" + end)
                gene_list =[]
                for g in ensemble_answer:
                    gene_name = g["phenotype_associations"]
                    for v in gene_name:
                        if "attributes" in v:
                            if "associated_gene" in v["attributes"]:
                                gene_list.append(v["attributes"]["associated_gene"])
                            contents = read_html_file("html/geneList.html").render(context={"gene_name": gene_list})
                        else:
                            contents = read_html_file("html/error.html").render(context={"error": "This is not within the dictionary."})
            #crear lista ( 2 for y 2 if, inicializar la lista y append los associated gene)
            except KeyError:
                contents = read_html_file("html/error.html").render(context={"error": "Please fill all the gaps and enter an integer number. Strings aren´t recognized."})
            except TypeError:
                contents = read_html_file("html/error.html").render(context={"error": "Please enter an integer number, negative numbers are not recognized."})
        elif path == "/favicon.ico":
            contents = read_html_file("html/index.html").render(context={"genes_dict": genes_dict})
        else:
            filename = routes[1:]
            contents = Path("html/" + filename + ".html").read_text()

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
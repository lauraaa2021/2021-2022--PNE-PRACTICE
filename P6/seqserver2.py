import http.server
import socketserver
import termcolor
import pathlib
from Seq1 import Seq
import jinja2
from urllib.parse import urlparse, parse_qs



def read_html_file(filename):
    contents = pathlib.Path(filename).read_text()
    contents = jinja2.Template(contents)          # funcionalidad igual que con .format en string / es un objeto de clase template
    return contents                         #.format para strings y para jinja2 usamos render.

# se puede representar lo mismo con jinja2 que con .format. .render nos deja escribir código dentro de las plantillas mientras que .format no
# format no deja mandar variables juntas sino que hay que mandarlas separadas


# Define the Server's port
PORT = 8080
seq_list = ["ACGACTCGACTCGA", "CAGTCATCTCA", "CAGACTAAGCGCGGG", "CGACGACAGCAGCAT", "AGACGACAGAT"]
gene_list = ["ADA", "FRAT1", "FXN", "RNU6_269P", "U5"]#constante


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # We just print a message
        print("GET received! Request line:")

        # Print the request line
        termcolor.cprint("  " + self.requestline, 'green')

        # Print the command received (should be GET)
        print("  Command: " + self.command)

        # Print the resource requested (the path)
        print("  Path: " + self.path)

        routes = self.requestline.split(" ")[1]
        # Message to send back to the clinet

        url_parse = urlparse(self.path)
        arguments = parse_qs(url_parse.query)
        path = url_parse.path    # el módulo url_parse coge la ruta sin la interrogación
        print("path: ", path)
        print("arguments", arguments)
        try:
            if path == "/":
                context = {"n_sequences": len(seq_list), "gene_names": gene_list}
                contents = read_html_file("html/form-1.html").render(context=context)
            elif path == "/ping":
                contents = read_html_file("html/ping.html").render()
            # remember : sending strings, you can send whatever but then be transformed into a string
            # devuelve un objeto de clase template, aunque no pasemos variable necesitamos implementarlo porque transforma el objeto template en un string y daría un error
            elif path == "/get":
                context = {"seq": arguments["operation"][0], "seq_1": seq_list[int(arguments["operation"][0])]}   # al final estamos accediendo a un diccionario y necesitamos acceder al valor de la clave que has definidio en el form
                contents = read_html_file("html/get.html").render(context=context)   #context manda un diccionario a través de render
            elif path == "/gene":
                sequence = Seq()
                sequence.read_fasta(arguments["operation"][0])
                context = {"seq": arguments["operation"][0], "seq_1": sequence.strbases}
                contents = read_html_file("html/gene.html").render(context=context)
            elif path == "/operation":
                sequence = arguments["msg"][0]
                operation = arguments["operation"][0]
                sequence_1 = Seq(sequence)
                if operation == "Rev":
                    contents = read_html_file("html/operation.html").render(context={"operation":operation, "result": sequence_1.reverse()})
                elif operation == "Info":
                    contents = read_html_file("html/operation.html").render(context={"operation":operation,"result": sequence_1.count_base()})
                elif operation == "Comp":
                    contents = read_html_file("html/operation.html").render(context={"operation":operation,"result": sequence_1.complement()})
            else:
                filename = routes[1:]
                contents = pathlib.Path("html/" + filename + ".html").read_text()
        except:
            contents = pathlib.Path("html/error.html").read_text()

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
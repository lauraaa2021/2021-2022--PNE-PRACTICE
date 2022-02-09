from pathlib import Path

def print_ok():
    print("ok")

def valid_filename():
    exit = False
    while not exit:
        filename = input("Enter a filename please:")
        try:
            f = open(filename, "r")
            exit = True
            return filename
        except FileNotFoundError:
            print("The file does not exist.")

def seq_read_fasta(filename):
    seq = open(filename, "r").read()
    seq = seq[seq.find("\n"):].replace("\n" ,"")
    return seq

def seq_len():
    list_genes = ["U5", "FRAT1", "ADA", "RNU6_269P", "FXN"]
    FOLDER = "./sequences/"
    for l in list_genes:
        print(len(seq0.seq_read_fasta(FOLDER + l + ".txt")))


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
            print(f)
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
    new_seq = []
    for l in list_genes:
        new_seq.append(len(seq_read_fasta(FOLDER + l + ".txt")))
    both_lists = list(zip(list_genes, new_seq))
    return both_lists


def seq_count_base():
    list_genes = ["U5", "FRAT1", "ADA", "RNU6_269P", "FXN"]
    FOLDER = "./sequences/"
    a = []
    c = []
    g = []
    t = []
    for l in list_genes:
         a.append(seq_read_fasta(FOLDER + l + ".txt").count("A"))
         c.append(seq_read_fasta(FOLDER + l + ".txt").count("C"))
         g.append(seq_read_fasta(FOLDER + l + ".txt").count("G"))
         t.append(seq_read_fasta(FOLDER + l + ".txt").count("T"))
    return a, c, g, t , list_genes

def seq_count():
    new_seq = []
    list_genes = ["U5", "FRAT1", "ADA", "RNU6_269P", "FXN"]
    FOLDER = "./sequences/"
    for e in list_genes:
        d = {"A": 0, "C": 0, "G": 0, "T": 0}
        for keys in d.keys():
            d[keys] = (seq_read_fasta(FOLDER+ e + ".txt")).count(keys)
        new_seq.append(d)
    return new_seq, list_genes

def seq_reverse():
    FOLDER = "./sequences/"
    u_5 = seq_read_fasta(FOLDER + "U5.txt")
    reverse = seq_read_fasta(FOLDER + "U5.txt")[::-1]
    return u_5[:20],  reverse[:20]

def seq_complement():
    FOLDER = "./sequences/"
    seq_1 = seq_read_fasta(FOLDER + "U5.txt")
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    bases = list(seq_1)
    bases = [complement[base] for base in bases]
    return  seq_1[:20],''.join(bases)[:20]


def seq_process():
    new_seq = []
    list_genes = ["U5", "FRAT1", "ADA", "RNU6_269P", "FXN"]
    FOLDER = "./sequences/"
    for e in list_genes:
        d = {"A": 0, "C": 0, "G": 0, "T": 0}
        for keys in d.keys():
            d[keys] = (seq_read_fasta(FOLDER+ e + ".txt")).count(keys)
        new_seq.append(max(d))
    return new_seq , list_genes

























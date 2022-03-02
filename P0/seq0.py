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
    list_genes_aux = list(zip(list_genes, a,c,g,t))
    return list_genes_aux

def seq_count():
    new_seq = []
    list_genes = ["U5", "FRAT1", "ADA", "RNU6_269P", "FXN"]
    FOLDER = "./sequences/"
    for e in list_genes:
        d = {"A": 0, "C": 0, "G": 0, "T": 0}
        for keys in d.keys():
            d[keys] = (seq_read_fasta(FOLDER+ e + ".txt")).count(keys)
        new_seq.append(d)
    list_genes_aux_1 = list(zip(list_genes, new_seq))
    return list_genes_aux_1

def seq_reverse():
    list_names = ["Frag", "Rev"]
    FOLDER = "./sequences/"
    u_5 = seq_read_fasta(FOLDER + "U5.txt")
    u_5_20 = u_5[:20]
    reverse = u_5_20[::-1]
    list_aux = []
    list_aux_1 = list_aux.append(u_5_20)
    list_aux_2 = list_aux.append(reverse)
    list_names_aux = list(zip(list_names, list_aux))
    return list_names_aux

def seq_complement():
    FOLDER = "./sequences/"
    seq_1 = seq_read_fasta(FOLDER + "U5.txt")
    seq_1_20 = seq_1[:20]
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    bases = list(seq_1_20)
    for element in bases:
        com = [complement[base] for base in seq_1_20]
    com_list = "".join(com)
    list_names_1 = ["Frag", "Comp"]
    list_com = []
    list_com_1 = list_com.append(seq_1_20)
    list_com_2 = list_com.append(com_list)
    list_names_com = list(zip(list_names_1, list_com))
    return list_names_com


def seq_process():
    new_seq = []
    list_genes = ["U5", "FRAT1", "ADA", "RNU6_269P", "FXN"]
    FOLDER = "./sequences/"
    for e in list_genes:
        d = {"A": 0, "C": 0, "G": 0, "T": 0}
        for keys in d.keys():
            d[keys] = (seq_read_fasta(FOLDER+ e + ".txt")).count(keys)
        maxValue = max(d.values())
        index_max = d.values().index(maxValue)
        new_seq.append(maxValue)
    list_process = list(zip(list_genes, new_seq))
    return list_process, index_max

























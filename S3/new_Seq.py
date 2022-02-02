
def count_bases(seq):
    d = {"A" : 0, "C":0, "G": 0, "T": 0}
    for b in seq:
        d[b] += 1
    return d



with open ("sequences", "r") as f:
    sequences = f.readlines()  #when using readlines we obtain the ending line character
    for seq in sequences:
        new_seq = seq.replace("\n", "")   #we need to create another sequence removing the end of line character
        print("Total length: ", len(new_seq)) # len is to calculate the length of the dna
        for k, v in count_bases(new_seq).items():
            print(k + ":", v)
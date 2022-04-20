class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases ="NULL"):#no se retorna nada en la init function

        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases
        if strbases == "NULL":
                print("Null sequence created!")
        elif not self.validate_sequence():
            self.strbases = "Error"
            print("Invalid Seq!!")
        else:
            print("New sequence created!")



    @staticmethod
    def validate_sequence2(sequence):
        valid = True
        i = 0
        while i < len(sequence) and valid:
            c = sequence[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid


    def validate_sequence(self):
        valid = True
        i = 0
        while i < len(self.strbases) and valid:
            c = self.strbases[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        if self.validate_sequence():
            return len(self.strbases)
        else:
            return 0


    def count_base(self):
        a = 0
        c = 0
        g = 0
        t = 0
        for e in self.strbases:
            if e == "A":
                a += 1
            elif e == "C":
                c += 1
            elif e == "G":
                g += 1
            elif e == "T":
                t += 1
        return a,c,g,t


    def count(self):
        d = {"A": 0, "C": 0, "G": 0, "T": 0}
        for b in self.strbases:
            if self.strbases == "Null" or "Error":
                return d
            else:
                d[b] += 1
                return d

    def reverse(self):
        if self.strbases == "NULL":
            return "NULL"
        elif self.strbases == "Error":
            return "Error"
        else:
            return self.strbases[::-1]


    def complement(self):
        if self.strbases == "NULL":
            return "NULL"
        elif self.strbases == "Error":
            return "Error"
        else:
            complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
            bases = list(self.strbases)
            bases = [complement[base] for base in bases]
            return ''.join(bases)

    '''def seq_read_fasta(self, filename):
        f = open("../sequences/" + filename + ".txt", "r").read()
        self.strbases = f[f.find("\n"):].replace("\n", "")'''

    def read_fasta(self, filename):
        filename = "../S4/"+ filename + ".txt"
        seq = open(filename, "r").read()
        seq = seq[seq.find("\n"):].replace("\n", "")
        self.strbases = seq

    def percentages(self):
        a, c, g, t = self.count_base()

        try:

            per_a = round((a * 100 / (a + c + g + t)), 3)
            per_c = round((c * 100 / (a + c + g + t)), 3)
            per_g = round((g * 100 / (a + c + g + t)), 3)
            per_t = round((t * 100 / (a + c + g + t)), 3)

        except ZeroDivisionError:
            print("Zero division error is not supported by python.")

        return per_a, per_c, per_t, per_g


    def add(self):
        d = {"A": 3, "C": -2, "G": 4, "T": 6}
        total = 0
        for b in self.strbases:
            total += d[b]
        return total



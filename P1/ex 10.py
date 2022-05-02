from Seq1 import Seq

list_genes = ["U5", "FRAT1", "ADA", "RNU6_269P", "FXN"]


s2 = Seq("ACGTCTCGATT")
print(s2.count())
print(s2.count_base())
print(s2.seq_process(s2.count()))
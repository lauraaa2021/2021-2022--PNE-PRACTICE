from Seq1 import Seq

s1 = Seq()

s2 = Seq("ACTGA")

s3 = Seq("Invalid sequence")


print("-----| Practice 1, Exercise 8 |------")

print(f"Sequence 1: {s1}", f"  Length: {s1.len()}")
print( "The bases are ", s1.payaso())
print("The reverse is ", s1.reverse())
print("The complement seq is", s1.complement())

print(f"Sequence 2: {s2}", f"  Length: {s2.len()}")
print("The bases are ", s2.payaso())
print("The reverse is" , s2.reverse())
print("The complement seq is", s2.complement())

print(f"Sequence 3: {s3}",f"  Length: {s3.len()}")
print("The bases are", s3.payaso())
print("The reverse is", s3.reverse())
print("The complement seq is", s3.complement())


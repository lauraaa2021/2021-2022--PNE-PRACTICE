from Seq1 import Seq

s1 = Seq()

s2 = Seq("ACTGA")

s3 = Seq("Invalid sequence")


print("-----| Practice 1, Exercise 5 |------")
print(f"Sequence 1: {s1}")
print(f"  Length: {s1.len()}")
print(s1.payaso())
print(f"Sequence 2: {s2}")
print(f"  Length: {s2.len()}")
print(s2.payaso())
print(f"Sequence 1: {s3}")
print(s3)
print(f"  Length: {s3.len()}")
print(s3.payaso())







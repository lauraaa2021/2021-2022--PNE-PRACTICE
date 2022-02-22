from Seq1 import Seq

s1 = Seq()

# -- Create a valid sequence
s2 = Seq("ACTGA")

# -- Create an invalid sequence
s3 = Seq("Invalid sequence")

print("-----| Practice 1, Exercise 5 |------")
print(f"Sequence 1: {s1}")
print(f"  Length: {s1.len()}", s1.count_1())   # give the length of name of object.len
print(f"Sequence 2: {s2}")
print(f"  Length: {s2.len()}",s2.count_1())
print(f"Sequence 1: {s3}")
print(f"  Length: {s3.len()}",s3.count_1())   # give the length of name of object.len







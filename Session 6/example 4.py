class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases, number):
        self.strbases = strbases
        self.number = number

        print("New sequence created!")

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def __str__2(self):
        return self.number

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)


# --- Main program
s1 = Seq("AGTACACTGGT", "je")
s2 = Seq("CGTAAC")

# -- Printing the objects
print(f"Sequence 1: {s1}")
print(f"Sequence 1: {s1}")
print(f"  Length: {s1.len()}")   # give the length of name of object.len
print(f"Sequence 2: {s2}")
print(f"  Length: {s2.len()}")


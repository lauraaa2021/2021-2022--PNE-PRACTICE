class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases, number):

        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases
        self.number = number
        print(number)
        print("New sequence created!")


# Main program
# Create objects of the class Seq
s1 = Seq("AGTACACTGGT", 100)   #when calling s1 when instantiating them we pass something which is passes to strbases
s2 = Seq("CGTAAC", 20)

#we don´t have the sequences printed because we haven´t printed them,
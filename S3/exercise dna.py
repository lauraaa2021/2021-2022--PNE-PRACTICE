# ask user for the dna sequence and count the number of letters

def count_bases(seq):
    d = {"A" : 0, "C":0, "G": 0, "T": 0} #we are creating a dictionary initialized to 0 and we add the values
    #we iterate through the whole sequence we use for
    for b in seq:
        d[b] += d[b] + 1 #b takes all the values of the sequence without considering if the dna sequence is wrong
    return d
# We return d and not b because we have instead of creating 4 different values for a, t, g and c
#we have created a single variable in the form of a dictionary that allows us to store the 4 variables and
#initialized it to 0 value, then with the for loop we just have to iterate and add those values to the variables
# so we return the values but just stored in a dictionary

dna_seq = input("Enter a Dna sequence please: ")
print("Total length: ", len(dna_seq)) #len is to calculate the length of the dna
print(count_bases(dna_seq))
for k,v in count_bases(dna_seq).items():
    print(k + ":", v)

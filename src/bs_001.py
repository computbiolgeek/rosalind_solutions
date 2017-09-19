# read dna string from the given file
dna_file = open('rosalind_dna.txt', 'rt')
dna_string = dna_file.read()
dna_file.close()

# count the frequencies for each base
bases = 'ACGT'
base_counts = [dna_string.count(base) for base in bases]

# print the counts
print(base_counts)
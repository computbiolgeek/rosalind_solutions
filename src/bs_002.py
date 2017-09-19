# read dna string from the given file
dna_file = open('rosalind_rna.txt', 'rt')
dna_string = dna_file.read()
dna_file.close()

# substitute each occurrence of 'T' for 'U'
rna_string = dna_string.replace('T', 'U')

# print the rna string
print(rna_string)
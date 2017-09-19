# read dna string from the given file
dna_file = open('rosalind_revc.txt', 'rt')
dna_string = dna_file.read()
dna_file.close()

# compute the reverse of dna_string
dna_reverse = dna_string[::-1]

# compute the reverse complement of dna_string
dna_reverse_complement = []
for base in dna_reverse:
    if base == 'A':
        dna_reverse_complement.append('T')
    elif base == 'C':
        dna_reverse_complement.append('G')
    elif base == 'G':
        dna_reverse_complement.append('C')
    elif base == 'T':
        dna_reverse_complement.append('A')

# cast the list into a string
separator = ''
dna_reverse_complement = separator.join(dna_reverse_complement)

# print the reverse complement of dna_string
print(dna_reverse_complement)
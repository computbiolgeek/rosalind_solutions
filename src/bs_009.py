"""
    @summary: Translating RNA into Protein
    @param param: 
    @return: 
    @author: Bian Li
    @contact: bian.li@vanderbilt.edu
    @change: June 27, 2016
"""

# read in the rna codon table and convert it into a dictionary
# that maps codons to their encoded amino acid labels
rna_codons_table = open('../examples/rna_codon_table.txt', 'rt')
rna_colons_list = rna_codons_table.read().split()
rna_codons = {rna_colons_list[i]: rna_colons_list[i + 1]
              for i in range(0, len(rna_colons_list), 2)}
rna_codons_table.close()

# read in the rna Sequence
rna_sequence_file = open('../examples/rosalind_prot.txt', 'rt')
rna_sequence = rna_sequence_file.read().rstrip()
rna_sequence_file.close()

# do the translation
protein_sequence = [rna_codons[rna_sequence[i:i+3]] 
                    for i in range(0, len(rna_sequence), 3)]

print(''.join(protein_sequence))
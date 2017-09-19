"""
    @summary: Computing GC Content
    @param param: At most 10 DNA strings in FASTA format 
    (of length at most 1 kbp each).
    @return: The ID of the string having the highest GC-content, 
    followed by the GC-content of that string. 
    @author: Bian Li
    @contact: bian.li@vanderbilt.edu
    @change: June 26th, 2016
"""

# read in the given rosalind fasta file
fasta_file = open('../examples/rosalind_gc.txt', 'rt')
chunks = fasta_file.read().split('>')
fasta_file.close()

# iterate over all lines in the fasta file
# create a dictionary containing seqid:sequence as key:value pairs
del chunks[0] # the first chunk is empty
seqid_sequence = {}
for chunk in chunks:
    rows = chunk.split('\n')
    seqid = rows[0]
    sequence = ''.join(rows[1:])
    seqid_sequence[seqid] = sequence

# compute GC-content for each sequence
max_gc_id = ''
max_gc_content = 0
for seqid, sequence in seqid_sequence.items():
    gc_content = (sequence.count('G') + sequence.count('C')) / len(sequence)
    if gc_content > max_gc_content:
        max_gc_id = seqid
        max_gc_content = gc_content

# print seqid of the sequence that has the maximum GC-content
print(max_gc_id)
print(max_gc_content)
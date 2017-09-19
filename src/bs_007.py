# read in the given two sequences
seq_file = open('../examples/rosalind_hamm.txt', 'rt')
sequences = seq_file.read().split('\n')
seq_file.close()

# a function to compute the Hamming distance between two strings
def hamming_distance(s1, s2):
    assert len(s1) == len(s2)
    hamming_dist = 0
    for char1, char2 in zip(s1, s2):
        if char1 != char2:
            hamming_dist += 1
    return hamming_dist

# compute the Hamming distance between the two DNA sequences
print(hamming_distance(sequences[0], sequences[1]))
"""
    @summary: Mendel's First Law
    @author: Bian LI
    @contact: bian.li@vanderbilt.edu
    @change: June 26th, 2016
"""

# read in the population
population = open('../examples/rosalind_iprob.txt', 'rt')
k, m, n = [int(i) for i in population.readline().split()]

# compute the probability of homozygous dominant, homozygous recessive
# and heterozygous
number_organisms = k + m + n
prob_homo_dominant = k / number_organisms
prob_hetero = m / number_organisms
prob_homo_recessive = n / number_organisms

# compute the probability that the produced organism is recessive
prob_recessive = (prob_homo_recessive * ((n - 1) / (number_organisms - 1)) +
    prob_homo_recessive * (m / (number_organisms - 1)) * 1 / 2 +
    prob_hetero * (n / (number_organisms - 1)) * 1 / 2 +
    prob_hetero * ((m - 1) / (number_organisms - 1)) * 1 / 4)

prob_dominant = 1 - prob_recessive
print(prob_dominant)
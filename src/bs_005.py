# this problem has not been solved yet
# read in n and m
nm_file = open('rosalind_fib.txt', 'rt')
nm = nm_file.readline().split()
nm_file.close()

# implement a function to compute the Fibonacci number
def fibonacci(n, m):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1, m)
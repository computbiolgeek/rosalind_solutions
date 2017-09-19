# read in month and rabit pairs each reproduction-age rabit produces
nk_file = open('rosalind_fib.txt', 'rt')
nk = nk_file.readline().split()
nk_file.close()

# define a function to compute the Fibonacci number
def fibonacci(n, k):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1, k) + k * fibonacci(n - 2, k)

# get n and k
n = int(nk[0])
k = int(nk[1])

# print the result
print(fibonacci(n, k))
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.
import time
start = time.time()

upper_limit = 2000000
answer = 0

def sieve_eratosthenes(n):
    primes = []
    sieve = [True] * n
    for p in range(2, n):
        if sieve[p]:
            primes.append(p)
            for i in range(p*p, n, p):
                sieve[i] = False
    return primes

primes = sieve_eratosthenes(upper_limit)

for k in primes:
    answer += k

print(answer)

stop = time.time()
print('Time: ', stop - start)
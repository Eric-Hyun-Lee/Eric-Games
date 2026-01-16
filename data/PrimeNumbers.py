def is_multiple(x, y):
    '''is_multiple(x, y) -> bool
    returns True if x is a multiple of y, False otherwise
    x, y: int
    '''
    # check if y divides evenly into x
    return (x % y == 0)

def is_prime(n):
    '''is_prime(n) -> bool
    returns True if n is prime, False if n is not prime
    n: int
    '''
    isPrime = True  # initialize the isPrime variable

    # check every divisor from 2 up to sqrt(n)
    for div in range(2, int(n**0.5) + 1):
        if is_multiple(n, div):
            isPrime = False  # n isn't prime!
    

    return isPrime
#Change 500 to any whole number greater than 2
numPrimes = 0
for num in range(2, 450000):
    if is_prime(num):
        numPrimes+=1
print("The number of primes was: " + str(numPrimes))
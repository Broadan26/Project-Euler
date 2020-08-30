def Euler10Optimized(prime_target): #Sieve of Erasthenes Solution like Euler 7
    prime = [True for i in range(prime_target + 1)] #Create array for Primes
    p = 2
    while (p * p <= prime_target): #If p is unchanged then it is prime
        if prime[p] == True:
            for i in range (p * 2, prime_target + 1, p): #If p is a prime update multiples
                prime[i] = False
        p = p + 1
    prime[0] = False #0 and 1 are not primes
    prime[1] = False

    i = 0
    sum = 0
    for p in range(prime_target):
        if prime[p]:
            sum = sum + p
    print('Sum of Primes:', sum)

if __name__ == "__main__": #Driver
    prime_target = 2000000
    Euler10Optimized(prime_target) #Only variations on this concept really
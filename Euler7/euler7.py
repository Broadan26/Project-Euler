import numpy as np

def upper_bound_for_p_n(size): #Calculates the upper bound for prime sieve
    if size > 6:
        result = int(size * (np.log(size) + np.log(np.log(size)))) + 1 #Formula and account for error
        return result
    else:
        return 20

def Euler7Optimized(size): #Sieve of Erasthenes Solution
    bound = upper_bound_for_p_n(size) #Get Sieve Bound

    prime = [True for i in range(bound + 1)] #Create array for primes
    p = 2
    while (p * p <= bound): #If p is unchanged it is a prime
        if prime[p] == True:
            for i in range (p * 2, bound + 1, p): #If p is a prime update its multiples
                prime[i] = False
        p = p + 1
    prime[0] = False #0 and 1 are not primes
    prime[1] = False

    i = 0
    for p in range(bound + 1): #Iterate to find expected prime
        if prime[p]:
            i = i + 1
        if prime[p] and (i == size):
            print(p)

if __name__ == "__main__": #Driver
    size = 10001 #Nth prime
    Euler7Optimized(size)
import math

def Euler3BruteForce1(size): #Horribly inefficient brute force
    largest_factor = -1
    i = 2
    while (i < size):       #Check all values below the number
        if (size % i) == 0: #Found a divisor
            is_prime = True 
            j = 2
            while (j < i):
                if (i % j) == 0:    #Not a prime
                    isPrime = False
                    j = i #Break
                j = j + 1
            if is_prime:    #Found new largest factor
                largest_factor = i
        i = i + 1
    print('Largest Factor:', largest_factor)

def Euler3BruteForce2(size): #Less horribly inefficient brute force
    largest_factor = -1
    i = 2
    while (i * i) < size:       #Only need to check up to sqrt(num)
        if (size % i) == 0:     #Check for factor
            factors = [i, (size/i)]
            k = 0
            while (k < 2):      #Check both factors
                is_prime = True
                j = 2
                while (j * j) < factors[k]:   #Check for prime
                    if (factors[k] % j) == 0: #Not a prime
                        is_prime = False
                        j = factors[k] #Break
                    j = j + 1
                if is_prime and (factors[k] > largest_factor):  #Found new largest factor
                    largest_factor = factors[k]
                k = k + 1
        i = i + 1
    print('Largest Factor:', largest_factor)

def Euler3Optimized1(size): #Optimized Factorization
    while(size % 2 == 0): #Remove all multiples of 2
        size = (size / 2)
    i = 3                         #First prime after 2
    while( i <= math.sqrt(size)): #Only need to check up to sqrt(num) for primes
        while(size % i == 0):     #Remove other factors
            size = (size / i)
        i = i + 2   #Skip evens
    if size > 2: #Last prime factor is solution
        print('Largest Factor:', int(size))

def Euler3Optimized2(size): #More Optimized Factorization
    largest_factor = -1
    i = 2
    while (i * i) <= size:      #Only need to check up to sqrt(num)
        if (size % i) == 0:     #Check for factor
            size = size / i
            largest_factor = i  #Save it
        else:
            i = i + 1
    if size > largest_factor:   #Check which remainder is largest prime
        print('Largest Factor:', int(size))
    else:
        print('Largest Factor:', int(largest_factor))

if __name__ == "__main__": #Driver
    size = 600851475143
    #Euler3BruteForce1(size) #Don't run this, it's awful
    Euler3BruteForce2(size)
    Euler3Optimized1(size)
    Euler3Optimized2(size)
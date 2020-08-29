import numpy as np

def Euler5BruteForce1(): #Horribly ineffient brute force
    i = 20
    while (((i % 2) != 0) or ((i % 3) != 0) or ((i % 4) != 0) or ((i % 5) != 0) or ((i % 6) != 0) 
           or ((i % 7) != 0) or ((i % 8) != 0) or ((i % 9) != 0) or ((i % 10) != 0) or ((i % 11) != 0) 
           or ((i % 12) != 0) or ((i % 13) != 0) or ((i % 14) != 0) or ((i % 15) != 0) or ((i % 16) != 0) 
           or ((i % 17) != 0) or ((i % 18) != 0) or ((i % 19) != 0) or ((i % 20) != 0)):
        i = i + 1
    print('Smallest Number is:', i)

def Euler5BruteForce2(): #Less horribly inefficient brute force
    i = 20
    while (((i % 2) != 0) or ((i % 3) != 0) or ((i % 4) != 0) or ((i % 5) != 0) or ((i % 6) != 0) 
           or ((i % 7) != 0) or ((i % 8) != 0) or ((i % 9) != 0) or ((i % 10) != 0) or ((i % 11) != 0) 
           or ((i % 12) != 0) or ((i % 13) != 0) or ((i % 14) != 0) or ((i % 15) != 0) or ((i % 16) != 0) 
           or ((i % 17) != 0) or ((i % 18) != 0) or ((i % 19) != 0) or ((i % 20) != 0)):
        i = i + 20
    print('Smallest Number is:', i)

def Euler5BruteForce3(): #Horribly inefficient brute force, but more iterative
    end = 20
    breakout = 0
    smallest_value = 0
    while end < math.factorial(20): #Go until a for sure factor of 1-20
        i = 1
        while i < 21: #Check for 1-20
            if(end % i) == 0: #Passes, keep going
                breakout = breakout + 1
                i = i + 1
            else: #Fails, skip the rest
                i = 21
        if breakout == 20: #Check for passing all divisors
            smallest_value = end
            end = math.factorial(20)
        breakout = 0
        end = end + 20
    print('Smallest Number is:', smallest_value)

def Euler5Optimized1(): #Much faster way to calculate
    result = 1
    i = 2
    while i <= 20: #Check the LCM of each value 2 to 20
        result = np.lcm(result, i) #Update result if LCM changes
        i = i + 1
    print('Smallest Number is:', result)

def Euler5Optimized2(): #Fastest way to calculate
    num = 20
    is_prime = np.empty(20); is_prime.fill(False)

    product = 1
    i = 2
    while i <= num: #Check every number
        if (not is_prime[i-1]):
            product = product * i #Only multiplies prime factors after 2
            j = i * i
            while j <= num: #Check multiples of future numbers for primes
                is_prime[j-1] = True
                if (np.log(j) / np.log(i) - int(np.log(j) / np.log(i))) == 0: #Check for prime factor
                    product = product * i
                j = j + i
        i = i + 1
    print('Smallest Number is:', product)

if __name__ == "__main__": #Driver
    #Euler5BruteForce1() #Don't use, not worth it
    #Euler5BruteForce2() #Don't use, also bad
    #Euler5BruteForce3() #Don't use, still very very bad
    Euler5Optimized1()
    Euler5Optimized2()
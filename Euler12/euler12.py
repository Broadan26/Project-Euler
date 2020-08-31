import numpy as np
import time

start = time.time()

#-----------------------
#Solution 1 - Very Slow
#-----------------------
def create_triangular_number(size): #Creates triangular numbers with Euler's Sum
    return (size * (size + 1) / 2)

def Euler12BruteForce(): #Drives the Triangle Creation and Testing
    triangle = 1
    triangle_size = 1
    while number_of_divisors(triangle) < 500:
        triangle_size = triangle_size + 1
        triangle = int(create_triangular_number(triangle_size))

    print(triangle)
        
def number_of_divisors(triangle): #Counts the number of divisors
    num = 0 #Holds number of divisors
    num_sqrt = int(np.sqrt(triangle)) #Sets max check
    for i in range(1,num_sqrt): #Check for divisors below max
        if triangle % i == 0: #Count both divisor pairs
            num = num + 2
    if (num_sqrt * num_sqrt) == triangle: #Remove perfect squares
        num = num - 1
    return num

if __name__ == "__main__": #Driver
    Euler12BruteForce() #Don't use, takes about 40 seconds
    print(time.time() - start)
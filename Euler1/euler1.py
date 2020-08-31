import time

start = time.time()

def Euler1BruteForce1(): #Brute Force Solution
    sum = 0
    for i in range(1000): #Runs 1000 times
        if((i % 3) == 0):
            sum = sum + i
        elif((i % 5) == 0):
            sum = sum + i
    print('Sum is:', sum) #Solution = 233168

def Euler1BruteForce2(): #A Lighter Brute Force Solution
    sum = 0
    multiple = 3
    for i in range(0,1000,3): #Runs 333 times
        sum = sum + i
    for i in range(0,1000,5): #Runs ~200 times
        sum = sum + i
    for i in range(0,1000,15): #Runs ~66 times
        sum = sum - i
    print('Sum is:', sum)

def Euler1BruteForce3(): #A code space saving optimization to previous solution
    sum_of_threes = int(sum(range(0,1000,3)))
    sum_of_fives = int(sum(range(0,1000,5)))
    sum_of_fifteens = int(sum(range(0,1000,15)))
    current_sum = sum_of_threes + sum_of_fives - sum_of_fifteens
    print('Sum is:', current_sum)

def Euler1Optimized(): #A space saving and O(1) optimized solution
    sum_of_threes = 3 * (999/3) * ((999/3)+1)/2
    sum_of_fives = 5 * (995/5) * ((995/5)+1)/2
    sum_of_fifteens = 15 * (990/15) * ((990/15)+1)/2
    current_sum = int(sum_of_threes + sum_of_fives - sum_of_fifteens)
    print('Sum is:', current_sum)

if __name__ == "__main__": #Driver
    Euler1BruteForce1()
    Euler1BruteForce2()
    Euler1BruteForce3()
    Euler1Optimized()
    print(time.time() - start)
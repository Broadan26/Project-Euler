def Euler2Iterate1(size):  #Brute Force Iteration of Terms
    a = 0                               #Set fib 1
    b = 1                               #Set fib 2
    curr_sum = 0                        #Hold sum of values
    while ((a < size) or (b < size)):
        c = (a + b)                     #Set next fib number
        if (c % 2) == 0:                #Find if even
            curr_sum = curr_sum + c     
        a = b                           #Swap
        b = c
    print(curr_sum)

def Euler2Iterate2(size):
    a = 2                               #Set fib2
    b = 0                               #Set fib1
    result = 2                          #Next even fib
    curr_sum = 0                        #Hold sum of values
    while (result < size):
        curr_sum = curr_sum + result    #Update sum
        result = 4*a + b                #Next even fib
        b = a                           #Swap
        a = result
    print(curr_sum)

if __name__ == "__main__": #Driver
    size = 4000000
    Euler2Iterate1(size)
    Euler2Iterate2(size)
def Euler9BruteForce(sum): #Simply brute force using Pythag rules
    c = 0
    found = False
    a = 1
    while a < int(sum/3): #A cannot be more than 1/3 of sum
        b = a
        while b < int(sum/2): #B cannot be more than 1/2 of sum
            c = sum - a - b

            if ((a * a) + (b * b)) == (c * c): #Check for Pythag Triple
                found = True
                break
            b = b + 1
        if found:
            break
        a = a + 1
    print('A is:', a)
    print('B is:', b)
    print('C is:', c)
    print('Product is:', (a*b*c))

def Euler9Optimized(sum): #Optimized using Pythagorean Identity
    a = b = c = 0
    m = 2
    current_sum = 0

    while current_sum < sum: #Go until Pythag triple has sum of 1000
        for n in range(1, m): #Utilize identity of Pythag triple to generate values
            a = (m * m) - (n * n)
            b = 2 * m * n
            c = (m * m) + (n * n)

            if (a + b + c) == sum: #If found, break out
                current_sum = sum
                break
        m = m + 1
    print('A is:', a)
    print('B is:', b)
    print('C is:', c)
    print('Product is:', (a*b*c))

if __name__ == "__main__": #Driver
    sum = 1000
    Euler9BruteForce(sum)
    Euler9Optimized(sum)
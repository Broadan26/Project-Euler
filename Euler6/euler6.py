def Euler6BruteForce(size): #Pretty efficient brute force method O(n)
    sum_of_squares = 0
    square_of_sum = 0
    i = 1
    while (i <= size): #Iterate from 1 to 100
        sum_of_squares = sum_of_squares + (i * i) #Perform the sum of squares
        square_of_sum = square_of_sum + i #Perform square of sums
        i = i + 1
    square_of_sum = (square_of_sum * square_of_sum)
    result = square_of_sum - sum_of_squares #Collect result
    print('Difference is:', result)

def Euler6Optimized(size): #As optimized as the problem can be O(1)
    sum_of_squares = 0
    square_of_sum = 0
    sum_of_squares = (size * (size + 1)/2)
    square_of_sum = (size * (size + 1) * (2 * size + 1)) / 6
    sum_of_squares = sum_of_squares * sum_of_squares
    result = int(sum_of_squares - square_of_sum)
    print(result)

if __name__ == "__main__": #Driver
    size = 100
    Euler6BruteForce(size)
    Euler6Optimized(size)
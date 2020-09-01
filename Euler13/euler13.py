import time

start = time.time()

def Euler13EasySolution(): #Finds the sum of all the numbers and returns the first 10 digits
    with open('euler13.txt') as fl:
        numbers = [[int(x) for x in line.split()] for line in fl]
    sum = 0
    for i in numbers:
        sum = sum + i[0]
    print(sum)

if __name__ == "__main__": #Driver
    Euler13EasySolution()
    print(time.time() - start)
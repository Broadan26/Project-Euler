import time

def sum_of_power_of_two(n: int) -> int:
    sum_of_power = 0
    power_of_two = 2 ** n
    while power_of_two > 0:
        sum_of_power += (power_of_two % 10)
        power_of_two //= 10
    return sum_of_power

def main():
    n = 1000

    start = time.time()
    sum_of_two = sum_of_power_of_two(n) # 1366
    print(f'Sum of digits of 2^1000 is: {sum_of_two}')
    end = time.time()
    print('Time Elapsed:', end - start)

if __name__ == "__main__":
    main()

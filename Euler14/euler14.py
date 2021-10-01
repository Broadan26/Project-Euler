import time
'''
LONGEST COLLATZ SEQUENCE BELOW 1,000,000
'''

def even_num(num: int):
    return (num // 2)

def odd_num(num: int):
    return ((3 * num) + 1)

def longest_collatz(limit: int = 10):
    # Setup Tuple (length, num)
    longest = (1, 1)

    # Direct Approach
    for i in range(2, limit):
        curr_length = 1
        num = i

        # Perform Collatz calculations
        while num != 1:
            if num % 2 == 0:
                num = even_num(num)
            else:
                num = odd_num(num)
            curr_length += 1

        # Check for longest
        if curr_length > longest[0]:
            longest = (curr_length, i)
    return longest

def longest_collatz_caching(limit: int = 10):
    # Setup cache
    length_cache = [-1] * limit
    length_cache[1] = 1

    # Setup tuple (length, num)
    longest = (1, 1)

    # Loop and update cache
    for i in range(2, limit):
        curr_length = 0
        num = i

        # Perform Collatz calculations
        while num != 1 and num >= i:
            curr_length += 1
            if num % 2 == 0:
                num = even_num(num)
            else:
                num = odd_num(num)

        # Update Cache
        length_cache[i] = curr_length + length_cache[num]

        # Check for longest
        if length_cache[i] > longest[0]:
            longest = (length_cache[i], i)
    
    return longest

def main():
    limit = 1_000_000

    start = time.time()
    longest = longest_collatz(limit) # (525, 837799) Length: 525, Number: 837799
    print(f'Length: {longest[0]} Number: {longest[1]}')
    end = time.time()
    print('Time Elapsed:', end - start)

    start = time.time()
    longest = longest_collatz_caching(limit) # (525, 837799) Length: 525, Number: 837799
    print(f'Length: {longest[0]} Number: {longest[1]}')
    end = time.time()
    print('Time Elapsed:', end - start)

if __name__ == "__main__":
    main()

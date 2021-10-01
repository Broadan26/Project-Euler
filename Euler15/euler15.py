from functools import reduce
from math import comb
import operator as op
import time


def ncf(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom

def lattice_paths(rows: int, cols: int) -> int:
    # Number of lattice paths follows a binomial coefficient
    return ncf(cols+rows, cols)

def lattice_paths_builtin(rows: int, cols: int) -> int:
    return comb(cols+rows, cols)

def main():
    rows = 20
    cols = 20

    start = time.time()
    num_of_paths = lattice_paths(rows, cols) # 137,846,528,820 paths
    print(f'Number of lattice paths is {num_of_paths} paths') 
    end = time.time()
    print('Time Elapsed:', end - start)

    start = time.time()
    num_of_paths = lattice_paths_builtin(rows, cols) # 137,846,528,820 paths
    print(f'Number of lattice paths is {num_of_paths} paths')
    end = time.time()
    print('Time Elapsed:', end - start)

if __name__ == "__main__":
    main()

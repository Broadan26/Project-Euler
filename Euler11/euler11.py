import numpy as np

def open_grid(): #Collects the grid
    with open('grid2020.txt') as fl:
        grid = [[int(x) for x in line.split()] for line in fl]
    return grid

def check_vertical(grid, loc_x, loc_y): #Checks the vertical product
    product = grid[loc_y][loc_x]
    for i in range(1,4):
        product = product * grid[loc_y + i][loc_x]
    return product

def check_horizontal(grid, loc_x, loc_y): #Checks the horizontal product
    product = grid[loc_y][loc_x]
    for i in range(1,4):
        product = product * grid[loc_y][loc_x + i]
    return product

def check_diagonal_right(grid, loc_x, loc_y): #Checks the diagonal right product
    product = grid[loc_y][loc_x]
    for i in range(1,4):
        product = product * grid[loc_y + i][loc_x + i]
    return product

def check_diagonal_left(grid,loc_x,loc_y): #Checks the diagonal left product
    product = grid[loc_y][loc_x]
    for i in range(1,4):
        product = product * grid[loc_y - i][loc_x + i]
    return product

def iterate_grid(grid):
    largest = 0
    loc_x = 0
    loc_y = 0
    direction = "none"
    for i in range(len(grid)): 
        for j in range(len(grid[0])): 
            if i < (len(grid) - 3): #Horizontal Check
                temp = check_horizontal(grid,i,j)
                if temp > largest:
                    largest = temp
                    loc_x = j
                    loc_y = i
                    direction = "Horizontal"
            if j < (len(grid[0]) - 3): #Vertical Check
                temp = check_vertical(grid,i,j)
                if temp > largest:
                    largest = temp
                    loc_x = j
                    loc_y = i
                    direction = "Vertical"
            if (i < (len(grid) - 3)) and (j < (len(grid[0]) - 3)): #Diagonal Right Check
                temp = check_diagonal_right(grid,i,j)
                if temp > largest:
                    largest = temp
                    loc_x = j
                    loc_y = i
                    direction = "Diagonal Right"
            if (j > 2) and (i < (len(grid[0]) - 3)): #Diagonal Left Check
                temp = check_diagonal_left(grid,i,j)
                if temp > largest:
                    largest = temp
                    loc_x = j
                    loc_y = i
                    direction = "Diagonal Left"
    print('Largest Value:', largest, 'at(', loc_y,',', loc_x,')' )
    print('Direction:', direction)

if __name__ == "__main__": #Driver
    grid = open_grid()
    print(np.matrix(grid))
    iterate_grid(grid)
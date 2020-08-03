# Module containing functions for manipulating 2-dimensional arrays of size 4x4
# Lonwabo Mvovo
# 27/05/2020

def create_grid(grid):
    '''create a 4x4 array of zeroes within grid'''
    # Updates 'grid' to a nested list with 4 lists of 0's for a range of 4
    for _ in range(4):
        grid.append([0 for _ in range(4)])

def print_grid(grid):
    '''print out a 4x4 grid in 5-width columns within a box'''
    # Prints sections of the box line by line
    print(' ----- ----- ----- -----\n' + '\n ----- ----- ----- -----\n'.join(['|' + '|'.join([f'{col:^5}' for col in row]) + '|' for row in grid]) + '\n ----- ----- ----- -----\n')

def check_lost(grid):
    '''return True if there are no 0 values and there are no
    adjacent values that are equal; otherwise False'''
    # Start a for loop where x is a number from 0 to 3 representing row/column indices of the grid
    for x in range(4):
    # Start a for loop where y is a number from 0 to 3 representing column/row indices of the grid
        for y in range(4):
            # Return 'False' if either the square's value is zero or if the square is not in the last row or last column and the square to the right or the square underneath is not the same
            if grid[x][y] == 0 or y + 1 < len(grid) and (grid[x][y] == grid[x][y+1] or grid[y][x] == grid[y+1][x]): return False
    # Since the game is not lost yet return 'True'
    return True


def check_won(grid):
    '''return True if a value>=32 is found in the grid; otherwise False'''
    # Start a for loop where row is a row of the grid
    for row in grid:
        # Start a for loop where col is a value in the row
        for col in row:
            # Return 'True' if the value of a square is greater than or equal to 32
            if col >= 32: return True
    # Since the player has not won yet return 'False'
    return False


def copy_grid(grid):
    '''return a copy of the given grid'''
    # Return a nested list with lists that are copies of grid's rows
    return [row.copy() for row in grid]


def grid_equal(grid1, grid2):
    '''check if 2 grids are equal - return a boolean value'''
    # Return 'True' if the two grids are equal otherwiser return 'False'
    return grid1 == grid2
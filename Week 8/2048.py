"""2048 game
hussein suleman
25 april 2014"""

# random number generator
import random
# grid utility routines
import util
# grid value merging routines
import push
# Import the os library which will be used to clear terminal after each move
import os

def add_block (grid):
    """add a random number to a random location on the grid"""
    # set distributon of number possibilities
    options = [2,2,2,2,2,4]
    # get random number
    chosen = options[random.randint(0,len(options)-1)]
    # initially set 'found' to False. 'found' is a boolean used to determine if an empty block to place a random number has been found
    found = False
    # start while loop that breaks when an empty block to place a random number has been found
    while (not found):
        # get random location
        x = random.randint (0, 3)
        y = random.randint (0, 3)
        # check and insert number
        if (grid[x][y] == 0):
            grid[x][y] = chosen
            found = True

def play ():
    """generate grid and play game interactively"""
    # create grid
    grid = []
    util.create_grid (grid)
    # add 2 starting random numbers
    add_block (grid)
    add_block (grid)
    # initially set 'won_message' to False. 'won_message' is used to determine if the user has been alerted that they won as to not keep printing the winning  message if they continue playing.
    won_message = False
    # start
    while (True):
        # Clear the terminal so that the game seems more interactive
        os.system('cls' if os.name == 'nt' else 'clear')
        # print the current state of the grid
        util.print_grid (grid)
        # set 'key' to a user input which represents the move they would like to do
        key = input ("Enter a direction:\n")
        # check if 'key' is one of the available options
        if (key in ['x', 'u', 'd', 'l', 'r']):
            # make a copy of the grid
            saved_grid = util.copy_grid (grid)
            if (key == 'x'):
                # quit the game
                return
            # manipulate the grid depending on input
            elif (key == 'u'):
                push.push_up (grid)
            elif (key == 'd'):
                push.push_down (grid)
            elif (key == 'r'):
                push.push_right (grid)
            elif (key == 'l'):
                push.push_left (grid)
            # check for a grid with no more gaps or legal moves
            if util.check_lost (grid):
                print ("Game Over!")
                return
            # check for a grid with the final number
            elif not won_message and util.check_won (grid):
                print ("Won!")
                won_message = True
                # Clear the terminal so that the game seems more interactive
                os.system('cls' if os.name == 'nt' else 'clear')
                # print the current state of the grid
                util.print_grid (grid)
                if input('Would you like to keep playing? (Y)es or (N)o: ').lower() == 'n':
                    print('Game Over!')
                    return
            # finally add a random block if the grid has changed    
            if not util.grid_equal (saved_grid, grid):
                add_block (grid)
            # check for a grid with no more gaps or legal moves
            if util.check_lost (grid):
                # Clear the terminal so that the game seems more interactive
                os.system('cls' if os.name == 'nt' else 'clear')
                # print last state of grid
                util.print_grid (grid)
                print ("Game Over!")
                return

# initialize the random number generator to a fixed sequence
random.seed (12)
# play the game
play ()
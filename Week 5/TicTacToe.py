# Tic-Tac-Toe game in terminal
# Lonwabo Mvovo
# 20/05/2020

# Import the os library which will be used to clear terminal after each move
import os
# Import the choice function from the random library which will be used to choose random moves for the computer to play
from random import choice

# Define 'show_board' which returns how the current game board should look in the terminal by using values in 'board' 
def show_board(): return f'''    1   2   3
   --- --- ---
1 | {board[0][0]} | {board[0][1]} | {board[0][2]} |
   --- --- ---
2 | {board[1][0]} | {board[1][1]} | {board[1][2]} |
   --- --- ---
3 | {board[2][0]} | {board[2][1]} | {board[2][2]} |
   --- --- ---'''

# Define 'row_win' which returns True if there's a possible winning move in a row otherwise returns False
def row_win():
    # Start a for loop in range of 3 for each row
    for row_i in range(3):
        # Checks if each element in a row has the same values that is equal to who's playing to see if there's a winner.
        if board[row_i][0] == board[row_i][1] == board[row_i][2] == player:
            # Return True to indicate to the computer that the player its checking can win horizontally on the spot
            return True
    # Return False to indicate to the computer that the player its checking cannot win horizontally on the spot
    return False


# Define 'col_win' which returns True if there's a possible winning move in a column otherwise returns False
def col_win():
    # Start a for loop in range of 3 for each column
    for col_i in range(3):
        # Checks if each element in a column has the same values that is equal to who's playing to see if there's a winner.
        if board[0][col_i] == board[1][col_i] == board[2][col_i] == player:
            # Return True to indicate to the computer that the player its checking can win vertically on the spot
            return True
    # Return False to indicate to the computer that the player its checking cannot win vertically on the spot
    return False


# Define 'diag_win' which returns True if there's a possible winning move in a diagonal otherwise returns False
def diag_win():
    # Start a for loop in range of 3 for each diagonal
    for diag_i in range(0, 3, 2):
        # Checks if each element in a diagonal has the same values that is equal to who's playing to see if there's a winner.
        if board[0][diag_i] == board[1][1] == board[2][2 if diag_i == 0 else 0] == player:
            # Return True to indicate to the computer that the player its checking can win diagonally on the spot
            return True
    # Return False to indicate to the computer that the player its checking cannot win diagonally on the spot
    return False


# Define 'winning_move' which returns True if the player the computer is checking can win either horizontally, vertically or diagonally by calling the respective functions otherwise returns False
def winning_move():
    return True if row_win() or col_win() or diag_win() else False


# Define 'game_over' which prints end of game message and returns True if the game is over and False if it is still ongoing
def game_over():
    # Indicate to the function that the global variables 'x_points' and 'o_points' must be used when they are refrenced
    global x_points, o_points
    # Start a for loop in range of 3 for each row
    for row_i in range(3):
        # Checks if each element in a row has the same values that is equal to who's playing to see if there's a winner.
        if board[row_i][0] == board[row_i][1] == board[row_i][2] == player:
            # Print horizontal winning message for the player that made the winning move
            print(f'\n"{player}" wins horizontally!!!')
            # Add 1 point to the player that made the winning move
            if player == 'X': x_points += 1
            else: o_points += 1
            # Return True to end game
            return True
    # Since there's no horizontal win start a for loop in range of 3 for each column
    for col_i in range(3):
        # Checks if each element in a column has the same values that is equal to who's playing to see if there's a winner.
        if board[0][col_i] == board[1][col_i] == board[2][col_i] == player:
            # Print vertical winning message for the player that made the winning move
            print(f'\n"{player}" wins vertically!!!')
            # Add 1 point to the player that made the winning move
            if player == 'X': x_points += 1
            else: o_points += 1
            # Return True to end game
            return True
    # Since there's no vertical win start a for loop in range of 3 for each diagonal
    for diag_i in range(0, 3, 2):
        # Checks if each element in a diagonal has the same values that is equal to who's playing to see if there's a winner.
        if board[0][diag_i] == board[1][1] == board[2][2 if diag_i == 0 else 0] == player:
            # Print diagonal winning message for the player that made the winning move
            print(f'\n"{player}" wins diagonally!!!')
            # Add 1 point to the player that made the winning move
            if player == 'X': x_points += 1
            else: o_points += 1
            # Return True to end game
            return True
    # Since there isn't a winner start a for loop in range of 3 for each row
    for row_j in range(3):
        # Checks each square in row to see if there is an empty spot. If there is it means the game is still ongoing so return False
        if ' ' in board[row_j]: return False
    # Since there isn't a winner and there are no empty squares left, the game ends in a draw so print draw message
    print('\nDraw!!!')
    # Return True to end game
    return True


# Define 'valid_move' that accepts a move as a parameter and returns True if the move is valid and False if it isn't
def valid_move(mv):
    # Check if the move has a length of 2 (two coordinates), both coordinates fit in board and that there is an empty spot to play
    if (len(mv) == 2 and mv[0] in range(3) and mv[1] in range(3) and board[mv[0]][mv[1]] == ' '
        or
        # Check if the move is 'quit'
        mv == ['quit']):
        # If either of these conditions are true, return True to indicate that the move is valid
        return True
    # Since the move is not valid return False
    return False


# Define 'computer_move' which returns a move the computer will play if the user decides to play with the computer depending on the mode the user has chosen
def computer_move():
    # Indicate to the function that the global variable 'player' must be used when it is refrenced
    global player
    # Set 'winning_moves_for_o' initially to an empty list which will represent all the possible winning moves O can make
    winning_moves_for_o = []
    # Set 'winning_moves_for_x' initially to an empty list which will represent all the possible winning moves X can make
    winning_moves_for_x = []
    # Set 'other_moves' initially to an empty list whcih will represent all the other moves that are not winning moves
    other_moves = []
    # Start a for loop for each row on the board
    for comp_row in range(3):
        # Start a for loop for each column on the board
        for comp_col in range(3):
            # Set 'comp_move_coords' to the index of the row and column
            comp_move_coords = [comp_row, comp_col]
            # Check if the move is valid by calling the 'valid_move' function and if it is run this code
            if valid_move(comp_move_coords):
                # Mark 'O' on the current coordinates
                board[comp_move_coords[0]][comp_move_coords[1]] = 'O'
                # Check if that move was a winning move by calling the 'winning_move' function and if it is run this code
                if winning_move():
                    # Add the move coordinates to the list of winning moves for 'O'
                    winning_moves_for_o.append(comp_move_coords)
                # Change player to 'X' to see if the move can be winning for them
                player = 'X'
                # Mark 'X' on the current coordinates
                board[comp_move_coords[0]][comp_move_coords[1]] = 'X'
                # Check if that move was a winning move by calling the 'winning_move' function and if it is run this code
                if winning_move():
                    # Add the move coordinates to the list of winning moves for 'X
                    winning_moves_for_x.append(comp_move_coords)
                # Change player back to 'O' because the checks are finished and it was player 'O's turn to begin with
                player = 'O'
                # Remove the mark made for the checks
                board[comp_move_coords[0]][comp_move_coords[1]] = ' '
                # Add the move to the list of other moves if it is not a winning move for 'O' or 'X'
                if comp_move_coords not in winning_moves_for_o and comp_move_coords not in winning_moves_for_x:
                    other_moves.append(comp_move_coords)
    # Check if the user decided to play easy mode
    if mode == 'e':
        # First try to return a move that is not winning if there are any
        if len(other_moves) > 0:
            return choice(other_moves)
        # Otherwise try to return a move that stops the user's winning move
        if len(winning_moves_for_x) > 0:
            for comp_move in winning_moves_for_x:
                if comp_move not in winning_moves_for_o:
                    return comp_move
        # Otherwise as a last resort return a winning move
        return choice(winning_moves_for_o)
    # Otherwise check if the user decided to play medium mode
    elif mode == 'm':
        # Set 'medium_comp_moves' initially to an empty list which will represent possible moves the computer can make
        medium_comp_moves = []
        # Check if there are non-winning or non-blocking moves and if there are randomly choose one and add it to the list of medium computer moves
        if len(other_moves) > 0:
            medium_comp_moves.append(choice(other_moves))
        # Check if there are winning moves for the computer and if there are randomly choose one and add it to the list of medium computer moves
        if len(winning_moves_for_o) > 0:
            medium_comp_moves.append(choice(winning_moves_for_o))
        # Check if there are blocking moves for the computer and if there are randomly choose one and add it to the list of medium computer moves
        if len(winning_moves_for_x) > 0:
            medium_comp_moves.append(choice(winning_moves_for_x))
        # Randomly choose a move from the list of medium moves and return that move
        return choice(medium_comp_moves)
    # Otherwise this means the user decided to play hard mode
    else:
        # Check if there are any winning moves for the computer and if there are randomly choose one and return it
        if len(winning_moves_for_o) > 0:
            return choice(winning_moves_for_o)
        # Otherwise check if there are any blocking moves for the computer and if there are randomly choose one and return it
        if len(winning_moves_for_x) > 0:
            return choice(winning_moves_for_x)
        # Otherwise as a last resort check if there are any moves that are non-winning or non-blocking for the computer and if there are randomly choose one and return it
        return choice(other_moves)


# Define 'play_game' which does not return anything but uses recursion to keep playing the game until it's over
def play_game():
    # Use the global variable 'player' to determine who's turn it is
    global player
    # If the user is playing with a friend or if it is their turn run this code
    if opponent == 'f' or player == 'X':
        # Start infinite while loop that breaks when user inputs a valid move
        while True:
            # Enter a try block
            try:
                # Set 'move' to coordinates inputed by user which are converted to a list of integers if they are digits otherwise they are made lowercase
                move = [int(coord) - 1 if coord.isdigit() else coord.lower() for coord in input(f'{player}: ').split()]
                # Assert that the move is valid by calling 'valid_move' with the move as an argument
                assert valid_move(move)
                # Break the infinite loop
                break
            # Enter except block when there's an error
            except:
                # Print message explaining to the user how to input co-ordinates for where they would like to move and that they must input 'QUIT' if they want to end the game
                print(f'''
Please input the coordinates (row, col) of an empty square where you would like to make your move
e.g. "2 2" makes this move:
    1   2   3
   --- --- ---
1 |   |   |   |
   --- --- ---
2 |   | {player} |   |
   --- --- ---
3 |   |   |   |
   --- --- ---

Input "QUIT" to end game''')
    # Otherwise this means the user is playing with the computer and it is the computers turn
    else:
        # Set 'move' to a move the computer will make by calling the 'computer_move' function
        move = computer_move()
    # Check if the move is 'quit'. If it is it means that the user would like to end the game so return from this function to get out of the recursion
    if move == ['quit']: return
    # Update the board where the player wanted to move to player's mark
    board[move[0]][move[1]] = player
    # Clear the terminal so that the game seems more interactive
    os.system('cls' if os.name == 'nt' else 'clear')
    # Print the current board by calling 'show_board'
    print(show_board())
    # Check if calling 'game_over' returns True. If it does it means that the game is over so return from this function to get out of the recursion
    if game_over(): return
    # Update 'player' to 'X' if it was previously 'O' otherwise update it to 'O' because it was previously 'X'
    player = 'X' if player == 'O' else 'O'
    # Since game is not over and the user does not want to quit then call 'play_game'. This makes 'play_game' a recursive function
    play_game()


# Set 'board' to a nested list of lists with 3 empty strings which acts as rows of the board
board = [
    # 0   1   2
    [' ',' ',' '], # 0
    [' ',' ',' '], # 1
    [' ',' ',' ']] # 2

# Set the initial player to 'X'
player = 'X'
# Set the first game number to 1
game = 1

# Set player-x points initially to 0
x_points = 0
# Set player-o points initially to 0
o_points = 0

print('Tic-Tac-Toe!!!\n')

# Start infinite loop that breaks when the user chooses if they would like to play with someone else or the computer
while True:
    try:
        # Set 'opponent' to a user inputed string that has all the spaces removed and is made to be lowercase for the validation
        opponent = input('Play against (F)riend or (C)omputer: ').strip().lower()
        # Assert that the user has either inputed 'f' or 'c' which represent who they would like to play the game with
        assert opponent == 'f' or opponent == 'c'
        # Break from the infinite loop
        break
    # Error message for when the user does not input either 'f' or 'c' for who they would like to play the game with
    except:
        print('Please enter who you would like to play against. "F" for friend or "C" for computer')

# Check if the user did decide to play with the computer
if opponent == 'c':
    # Start an infinite loop that breaks when the user inputs a valid mode they would like to play
    while True:
        try:
            # Set 'mode'to a string inputed by user that has all the spaces removed and is made to be lowercase for the validation
            mode = input('(E)asy / (M)edium / (H)ard: ').strip().lower()
            # Assert that the mode inputed is one of the 3 valid modes
            assert mode == 'e' or mode == 'm' or mode == 'h'
            break
        # Error message for when the user does input a valid mode
        except:
            print('Please input either "E" for easy, "M" for medium or "H" for hard.')

# Print welcome game message explaining to the user how to input co-ordinates for where they would like to move and that they must input 'QUIT' if they want to end the game
print(f'''
Input the coordinates (row, col) of an empty square where you would like to make your move.

Input "QUIT" to end game

{show_board()}''') # Prints the initial empty board by calling 'show_board'

# Infinite loop that breaks when the players would not like to play again
while True:
    # Call 'play_game' to start playing the game
    play_game()
    # Ask the user if they would like to play again and set 'play_again' to their answer in lowercase
    play_again = input('\nWould you like to play again? (Y)es or (N)o: ').lower()
    # If 'play_again' is equal to 'n' it means the user would not like to play again so break from the loop
    if play_again == 'n': break
    # Add a new game
    game += 1
    # Clear the terminal so that the game seems more interactive
    os.system('cls' if os.name == 'nt' else 'clear')
    # Clear the board values
    board = [[' ' for _ in range(3)] for _ in range(3)]
    # Print the current board by calling 'show_board'
    print(show_board())
    # Every game a new player must start so change the starting player based on the number of games played
    player = 'O' if game % 2 == 0 else 'X'

print(f'\nScoreboard\nX: {x_points}\nO: {o_points}')

# Print cool ASCII game over message
print('''   ____ _____ _____ ___  ___     ____ _   _____  _____
  / __ `/ __ `/ __ `__ \\/ _ \\   / __ \\ | / / _ \\/ ___/
 / /_/ / /_/ / / / / / /  __/  / /_/ / |/ /  __/ /    
 \\__, /\\__,_/_/ /_/ /_/\\___/   \\____/|___/\\___/_/     
/____/''')
# Merging functions that merge adjacent equal values and eliminate gaps for the game 2024
# Lonwabo Mvovo
# 17/06/2020


# define 'push_up' which takes a 4x4 nested list as parameter 'board', merges adjacent equal values upwards and eliminates gaps upwards
def push_up(board):
    # STEP 1: Push numbers up to eliminate gaps between and above numbers

    # initially set 'check_again' to False. 'check_again' will be used to determine if the while loop should run again
    check_again = True

    # start an infinite loop which breaks once gaps and zeros have been eliminated upwards
    while check_again:
        # update 'check_again' to False
        check_again = False
        # start a for loop with indices 'col_i' for each column in 'board'
        for col_i in range(4):
            # start a for loop with indices 'num_i' for the last 3 numbers in a column
            for num_i in range(1, 4):
                # check if the number appearing above this number on the board at the current index is 0 because this means there is a gap above the number
                if board[num_i - 1][col_i] == 0:
                    # check if this number on the board at the current index is 'x' ('x' is an arbitrary placeholder that is used in this module to fill the space once numbers have been pushed in a certain direction instead of 0 because 0 can represent gaps but 'x' is only used to show that a space has been created by pushing numbers in a direction)
                    if board[num_i][col_i] == 'x':
                        # change the 0 appearing above this number on the board at the current index to an 'x'
                        board[num_i - 1][col_i] = 'x'
                    # since this number is not 'x' it means that there are other numbers that need to be pushed up in this column
                    else:
                        # start a for loop with indices 'num_j' for the numbers starting from this number at the current index until the last number in a column
                        for num_j in range(num_i, 4):
                            # move the number one position up in the column
                            board[num_j - 1][col_i] = board[num_j][col_i]
                        # set the number on the board at the last iteration of the previous for loop in the column to 'x'
                        board[num_j][col_i] = 'x'
                        # since numbers have been pushed up there still might be gaps in the columns that need to be checked for so 'check_again' is updated to True
                        check_again = True

    # STEP 2: Merge adjacent equal values upwards

    # start a for loop with indices 'col_i' for each column in 'board'
    for col_i in range(4):
        # start a for loop with indices 'num_i' for the last 3 numbers in a column
        for num_i in range(1,4):
            # check if the number appearing above this number on the board at the current index and this number are equal and do not equal 'x'
            if board[num_i - 1][col_i] == board[num_i][col_i] != 'x':
                # change the number appearing above this number on the board at the current index to the sum of it and this number
                board[num_i - 1][col_i] += board[num_i][col_i]
                # change this number to 0
                board[num_i][col_i] = 0

    # STEP 3: Push numbers up again to eliminate gaps between and above numbers created by merging numbers upwards

    # code in STEP 3 is the same as STEP 1
    check_again = True

    while check_again:
        check_again = False
        for col_i in range(4):
            for num_i in range(1, 4):
                if board[num_i - 1][col_i] == 0:
                    if board[num_i][col_i] == 'x':
                        board[num_i - 1][col_i] = 'x'
                    else:
                        for num_j in range(num_i, 4):
                            board[num_j - 1][col_i] = board[num_j][col_i]
                        board[num_j][col_i] = 'x'
                        check_again = True

    # STEP 4: replace all 'x's with zeros

    # start a for loop with indices 'row_i' for each row in 'board'
    for row_i in range(4):
        # start a for loop with indices 'num_i' for each number in a row
        for num_i in range(4):
            # check if this value on the board at the current index is an 'x'
            if board[row_i][num_i] == 'x':
                # replace it with a zero
                board[row_i][num_i] = 0


def push_down(board):
    # STEP 1: Push numbers down to eliminate gaps between and below numbers

    # initially set 'check_again' to False.
    check_again = True

    # start an infinite loop which breaks once gaps and zeros have been eliminated downwards
    while check_again:
        # update 'check_again' to False
        check_again = False
        # start a for loop with indices 'col_i' for each column in 'board'
        for col_i in range(4):
            # start a for loop with indices 'num_i' for the first 3 numbers in a column
            for num_i in range(2, -1, -1):
                # check if the number appearing below this number on the board at the current index is 0 because this means there is a gap below the number
                if board[num_i + 1][col_i] == 0:
                    # check if this number on the board at the current index is 'x'
                    if board[num_i][col_i] == 'x':
                        # change the 0 appearing below this number on the board at the current index to an 'x'
                        board[num_i + 1][col_i] = 'x'
                    # since this number is not 'x' it means that there are other numbers that need to be pushed down in this column
                    else:
                        # start a for loop with indices 'num_j' for the numbers starting from this number at the current index until the first number in a column
                        for num_j in range(num_i, -1, -1):
                            # move the number one position down in the column
                            board[num_j + 1][col_i] = board[num_j][col_i]
                        # set the number on the board at the last iteration of the previous for loop in the column to 'x'
                        board[num_j][col_i] = 'x'
                        # since numbers have been pushed down there still might be gaps in the columns that need to be checked for so 'check_again' is updated to True
                        check_again = True

    # STEP 2: Merge adjacent equal values downwards

    # start a for loop with indices 'col_i' for each column in 'board'
    for col_i in range(4):
        # start a for loop with indices 'num_i' for the first 3 numbers in a column
        for num_i in range(2, -1, -1):
            # check if the number appearing below this number on the board at the current index and this number are equal and do not equal 'x'
            if board[num_i + 1][col_i] == board[num_i][col_i] != 'x':
                # change the number appearing below this number on the board at the current index to the sum of it and this number
                board[num_i + 1][col_i] += board[num_i][col_i]
                # change this number to 0
                board[num_i][col_i] = 0

    # STEP 3: Push numbers down again to eliminate gaps between and below numbers created by merging numbers downwards

    # code in STEP 3 is the same as STEP 1
    check_again = True

    while check_again:
        check_again = False
        for col_i in range(4):
            for num_i in range(2, -1, -1):
                if board[num_i + 1][col_i] == 0:
                    if board[num_i][col_i] == 'x':
                        board[num_i + 1][col_i] = 'x'
                    else:
                        for num_j in range(num_i, -1, -1):
                            board[num_j + 1][col_i] = board[num_j][col_i]
                        board[num_j][col_i] = 'x'
                        check_again = True

    # STEP 4: replace all 'x's with zeros

    # start a for loop with indices 'row_i' for each row in 'board'
    for row_i in range(4):
        # start a for loop with indices 'num_i' for each number in a row
        for num_i in range(4):
            # check if this value on the board at the current index is an 'x'
            if board[row_i][num_i] == 'x':
                # replace it with a zero
                board[row_i][num_i] = 0


def push_right(board):
    # STEP 1: Push numbers right to eliminate gaps between and to the right of numbers

    # initially set 'check_again' to False.
    check_again = True

    # start an infinite loop which breaks once gaps and zeros have been eliminated rightwards
    while check_again:
        # update 'check_again' to False
        check_again = False
        # start a for loop with indices 'row_i' for each row in 'board'
        for row_i in range(4):
            # start a for loop with indices 'num_i' for the first 3 numbers in a row
            for num_i in range(2, -1, -1):
                # check if the number appearing to the right of this number on the board at the current index is 0 because this means there is a gap to the right of the number
                if board[row_i][num_i + 1] == 0:
                    # check if this number on the board at the current index is 'x'
                    if board[row_i][num_i] == 'x':
                        # change the 0 appearing to the right of this number on the board at the current index to an 'x'
                        board[row_i][num_i + 1] = 'x'
                    # since this number is not 'x' it means that there are other numbers that need to be pushed to the right in this row
                    else:
                        # start a for loop with indices 'num_j' for the numbers starting from this number at the current index until the first number in a row
                        for num_j in range(num_i, -1, -1):
                            # move the number one position to the right in the row
                            board[row_i][num_j + 1] = board[row_i][num_j]
                        # set the number on the board at the last iteration of the previous for loop in the row to 'x'
                        board[row_i][num_j] = 'x'
                        # since numbers have been pushed to the right there still might be gaps in the rows that need to be checked for so 'check_again' is updated to True
                        check_again = True

    # STEP 2: Merge adjacent equal values rightwards

    # start a for loop with indices 'row_i' for each row in 'board'
    for row_i in range(4):
        # start a for loop with indices 'num_i' for the first 3 numbers in a row
        for num_i in range(2, -1, -1):
            # check if the number appearing to the right of this number on the board at the current index and this number are equal and do not equal 'x'
            if board[row_i][num_i + 1] == board[row_i][num_i] != 'x':
                # change the number appearing to the right of this number on the board at the current index to the sum of it and this number
                board[row_i][num_i + 1] += board[row_i][num_i]
                # change this number to 0
                board[row_i][num_i] = 0

    # STEP 3: Push numbers right again to eliminate gaps between and to the right of numbers created by merging numbers rightwards

    # code in STEP 3 is the same as STEP 1
    check_again = True

    while check_again:
        check_again = False
        for row_i in range(4):
            for num_i in range(2, -1, -1):
                if board[row_i][num_i + 1] == 0:
                    if board[row_i][num_i] == 'x':
                        board[row_i][num_i + 1] = 'x'
                    else:
                        for num_j in range(num_i, -1, -1):
                            board[row_i][num_j + 1] = board[row_i][num_j]
                        board[row_i][num_j] = 'x'
                        check_again = True
        
    # STEP 4: replace all 'x's with zeros

    # start a for loop with indices 'row_i' for each row in 'board'
    for row_i in range(4):
        # start a for loop with indices 'num_i' for each number in a row
        for num_i in range(4):
            # check if this value on the board at the current index is an 'x'
            if board[row_i][num_i] == 'x':
                # replace it with a zero
                board[row_i][num_i] = 0


def push_left(board):
    # STEP 1: Push numbers left to eliminate gaps between and to the left of numbers

    # initially set 'check_again' to False.
    check_again = True

    # start an infinite loop which breaks once gaps and zeros have been eliminated leftwards
    while check_again:
        # update 'check_again' to False
        check_again = False
        # start a for loop with indices 'row_i' for each row in 'board'
        for row_i in range(4):
            # start a for loop with indices 'num_i' for the last 3 numbers in a row
            for num_i in range(1, 4):
                # check if the number appearing to the left of this number on the board at the current index is 0 because this means there is a gap to the left of the number
                if board[row_i][num_i - 1] == 0:
                    # check if this number on the board at the current index is 'x'
                    if board[row_i][num_i] == 'x':
                        # change the 0 appearing to the left of this number on the board at the current index to an 'x'
                        board[row_i][num_i - 1] = 'x'
                    # since this number is not 'x' it means that there are other numbers that need to be pushed to the left in this row
                    else:
                        # start a for loop with indices 'num_j' for the numbers starting from this number at the current index until the last number in a row
                        for num_j in range(num_i, 4):
                            # move the number one position to the left in the row
                            board[row_i][num_j - 1] = board[row_i][num_j]
                        # set the number on the board at the last iteration of the previous for loop in the row to 'x'
                        board[row_i][num_j] = 'x'
                        # since numbers have been pushed to the left there still might be gaps in the rows that need to be checked for so 'check_again' is updated to True
                        check_again = True

    # STEP 2: Merge adjacent equal values leftwards

    # start a for loop with indices 'row_i' for each row in 'board'
    for row_i in range(4):
        # start a for loop with indices 'num_i' for the last 3 numbers in a row
        for num_i in range(1,4):
            # check if the number appearing to the left of this number on the board at the current index and this number are equal and do not equal 'x'
            if board[row_i][num_i - 1] == board[row_i][num_i] != 'x':
                # change the number appearing to the left of this number on the board at the current index to the sum of it and this number
                board[row_i][num_i - 1] += board[row_i][num_i]
                # change this number to 0
                board[row_i][num_i] = 0

    # STEP 3: Push numbers left again to eliminate gaps between and to the left of numbers created by merging numbers leftwards

    # code in STEP 3 is the same as STEP 1
    check_again = True

    while check_again:
        check_again = False
        for row_i in range(4):
            for num_i in range(1, 4):
                if board[row_i][num_i - 1] == 0:
                    if board[row_i][num_i] == 'x':
                        board[row_i][num_i - 1] = 'x'
                    else:
                        for num_j in range(num_i, 4):
                            board[row_i][num_j - 1] = board[row_i][num_j]
                        board[row_i][num_j] = 'x'
                        check_again = True
        
    # STEP 4: replace all 'x's with zeros

    # start a for loop with indices 'row_i' for each row in 'board'
    for row_i in range(4):
        # start a for loop with indices 'num_i' for each number in a row
        for num_i in range(4):
            # check if this value on the board at the current index is an 'x'
            if board[row_i][num_i] == 'x':
                # replace it with a zero
                board[row_i][num_i] = 0
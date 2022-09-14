#######################################################################################################################
#############################################-What the Code Does-######################################################
#######################################################################################################################
# def print_board(sudoku):
# This prints the board out in 3x3 grids with lines in between each 3x3 for 1 sudoku column.
#
# def complete_failed():
# This just compares the solved sudoku with the right sudoku values. If it is equal to the solved
# table then you have won. If not, you've lost. Here it will also display the total amount of turns and how long it told
# you to solve it. It will also ask if you want to play again or just quit sudoku.
#
# def computer_play():
# This is just a solver for the computer to do.
# So, it goes through each row and looks for an empty slot. When it finds an empty slot it will fill it with numbers
# from 1 to 9.
# It will then check each row, column and the number to see if it is the same. If it is it will slowly remove those
# numbers and match them with it. It will them check the individual 3x3 grid to see if the numbers are the same.
# if they are then it'll change the numbers accordingly to each row.
# There is then a checker to see for more blank spaces. If there are not any it will loop back to the top and start
# again. However, if there aren't any it will take you to the complete_failed function. This will check against the
# the solved table and determine if the computer wins.
#
# def human_play():
# This is just a function that takes your inputs on [row] and [col] and aligns them with the table.
# Then there is also a 'num' which is the number that is inputted into the sudoku table.
# Then there is the withdraw mode. This just gets an inputted number for the row and column you want to remove from
# and removes the column at that point.
# Help mode is used when the user presses h. In help mode it will look for blank spaces and suggest what moves can be
# made. So, if you typed h you'd get a result back such as at (0,0) input number 6. This is done for each place you type
# row and col from. It isn't intergrated well and is very messy.
#
# def human_is_valid():
# This function is purely used just to see if the space you're wanting to input a number is free. If it isn't free
# it will print a message telling you that and asking for another valid input.
#
# def choose_board():
# This just asks for what board the player wants to use. So, if the person inputted 4 it will use the sudoku board
# sudoku4. If you input an invalid number such as 5 it will tell you it's an invalid choice and ask for you to choose
# again. If you input a valid one it will load up play_choose.
#
# def play_choose():
# This function is purely used to pick who you want to play. If you want the computer to play you'll just have to type
# in computer and the same works if you type human for human play. If you type an invalid player it will ask for
# another input.
# Human input will load = human_play, human_is_valid
# Computer input will load computer_play
#
#######################################################################################################################
import time, sys, random

def print_board(sudoku):
    for i in range(9):
        print(sudoku[i][0:3],'|',sudoku[i][3:6],'|',sudoku[i][6:9])
        if i==5 or i==2:
            print('-'*51)
            
if __name__ == '__main__':
    sudoku2 = [
        [' ', ' ', ' ', '3', ' ', ' ', ' ', '7', ' '],
        ['7', '3', '4', ' ', '8', ' ', '1', '6', '2'],
        ['2', ' ', ' ', ' ', ' ', ' ', ' ', '3', '8'],
        ['5', '6', '8', ' ', ' ', '4', ' ', '1', ' '],
        [' ', ' ', '2', '1', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '7', '8', ' ', ' ', '2', '5', '4'],
        [' ', '7', ' ', ' ', ' ', '2', '8', '9', ' '],
        [' ', '5', '1', '4', ' ', ' ', '7', '2', '6'],
        ['9', ' ', '6', ' ', ' ', ' ', ' ', '4', '5'],
    ]

    # make sure 'option=2' is used in your submission
    option = 2
    if option == 2:
        sudoku = sudoku2
    else:
        raise ValueError('Invalid choice!')

# Turn variable
turns = 0

# Timer for how long it takes the user and the computer.
s_time = 0
s_time = time.time()

# USE SUDOKU 2 IN THE FINAL SUBMISSION!
# The solved result to help the 'help' mechanic. This only works for Sudoku 2.
sudoku_solved = [
        ['6', '8', '5', '3', '2', '1', '4', '7', '9'],
        ['7', '3', '4', '9', '8', '5', '1', '6', '2'],
        ['2', '1', '9', '6', '4', '7', '5', '3', '8'],
        ['5', '6', '8', '2', '7', '4', '9', '1', '3'],
        ['3', '4', '2', '1', '5', '9', '6', '8', '7'],
        ['1', '9', '7', '8', '3', '6', '2', '5', '4'],
        ['4', '7', '3', '5', '6', '2', '8', '9', '1'],
        ['8', '5', '1', '4', '9', '3', '7', '2', '6'],
        ['9', '2', '6', '7', '1', '8', '3', '4', '5'],
    ]


# Introduction with rules and showing the table.
print('Rules of Sudoku:\n'
    'o Every square has to contain a single number\n'
    'o Each 3×3 box can only contain each number from 1 to 9 once\n'
    'o Each vertical/horizontal column can only contain each number from 1 to 9 once.'
     )
print('#' * 51)
print_board(sudoku)
print('#' * 51)


def complete_failed(turns, s_time):
    if sudoku == [
        ['6', '8', '5', '3', '2', '1', '4', '7', '9'],
        ['7', '3', '4', '9', '8', '5', '1', '6', '2'],
        ['2', '1', '9', '6', '4', '7', '5', '3', '8'],
        ['5', '6', '8', '2', '7', '4', '9', '1', '3'],
        ['3', '4', '2', '1', '5', '9', '6', '8', '7'],
        ['1', '9', '7', '8', '3', '6', '2', '5', '4'],
        ['4', '7', '3', '5', '6', '2', '8', '9', '1'],
        ['8', '5', '1', '4', '9', '3', '7', '2', '6'],
        ['9', '2', '6', '7', '1', '8', '3', '4', '5'],
    ]:
        print('#' * 51)
        update_board(turns, s_time)
        print("The Sudoku board has been solved successfully!\nTurns: ", turns)
        print('Session time:', int(s_time),'seconds')
        print('#' * 51)
    else:
        print('#' * 51)
        update_board(turns, s_time)
        print('The Sudoku board has been failed to solve.\nTurns: ', turns)
        print('Session time:', int(s_time),'seconds')
        print('#' * 51)

    # If you have restarted then it will go to play_choose or exit.
    restart = input('Do you want to play again? (yes or no): ')
    if restart == 'yes':
        play_choose()
    else:
        sys.exit()


def update_board(turns, s_time):
    # Prints the turns and the amount of seconds that you've done.
    print('Turns:', turns)
    print('Time:', int(s_time),'seconds')
    print('#' * 51)
    print_board(sudoku)
    print('#' * 51)


def computer_play(s_time, turns):
    s_time = (time.time() - s_time)
    # For each row and column you need to find the empty cells.
    for row in range(len(sudoku)):
        for col in range(len(sudoku[row])):
            # Fill the blank spaces in the empty cells. So, it fills empty cells thus making them 'discovered'
            if sudoku[row][col] == ' ':
                # 123456789: So, it can work through the numbers from 9 to 1 until it finds a number
                # that is compatible in the grid, row, column.
                sudoku[row][col] = '123456789'

    # When the replace is done it will stop the function.
    while not all([(len(cell) == 1) for row in sudoku for cell in row]):
        # Makes the replacement false so it doesn't break out of the loop and stop the sorting process.
        replace = False

        # When the cells have been discovered it will then check.
        # Create new rows and cols for each of new number solved.
        for row in range(len(sudoku)):
            for col in range(len(sudoku[row])):
                if len(sudoku[row][col]) != 1:
                    # If the row equals same number: change
                    for col_new in range(len(sudoku[row])):
                        if col_new != col and len(sudoku[row][col_new]) == 1:
                            if sudoku[row][col_new] in sudoku[row][col]:
                                # Replace new values in the same space.
                                replace = True
                                sudoku[row][col] = sudoku[row][col].replace(sudoku[row][col_new], "")
                                # When it replaces number add a turn.
                                turns += 1

                    # If the column equals same number: change
                    for row_new in range(len(sudoku)):
                        if row_new != row and len(sudoku[row_new][col]) == 1:
                            if sudoku[row_new][col] in sudoku[row][col]:
                                # Replace new values in the same space.
                                replace = True
                                sudoku[row][col] = sudoku[row][col].replace(sudoku[row_new][col], "")
                                # When it replaces number add a turn.
                                turns += 1

                    # Find the rows and columns of each 3x3 box.
                    corner_row = row - row % 3
                    corner_col = col - col % 3

                    # Now it will work through each box and check the cells in it.
                    # Check the new assigned rows and columns.
                    for row_new in range(corner_row, corner_row + 3):
                        for col_new in range(corner_col, corner_col + 3):
                            # If there is already a same number in the row and column then change them to new
                            if (row_new != row or col_new != col) and len(sudoku[row_new][col_new]) == 1:
                                if sudoku[row_new][col_new] in sudoku[row][col]:
                                    # When Replace = True the row, col with row2 and col2.
                                    replace = True
                                    sudoku[row][col] = sudoku[row][col].replace(sudoku[row_new][col_new], "")
                                    # When it replaces number add a turn.
                                    turns += 1

        # If not replaced happened break the loop.
        if not replace:
            break
    complete_failed(turns, s_time)


def human_play(turns, s_time):
    s_time = (time.time() - s_time)
    # Starts the timer to show how long they've been playing. Also, adds time every second.
    print('-' * 51)
    print("If you need help type: 'h'\n"
          "If you want to withdraw a move type: withdraw.\n"
          "If you want to exit type: 'leave'"
          )
    # The player chooses to play, help, or leave
    print('-' * 51)
    print_board(sudoku)
    while True:
        # Starts the timer to show how long they've been playing. Also, adds time every second.
        s_time += 1

        # Where the row should go.
        row = input('Which row do you want to change?: ')
        if row.isdigit():
            # If it is then make it an int.
            row = int(row)
            c_row = row
            # If row is more than 9 print it's an invalid number.
            if row > 9:
                print('#' * 51)
                print('That is not a valid row.')
                print('#' * 51)
                continue

        # If the row is equal to withdraw it will withdraw your last row and col position.
        elif row == 'withdraw':
            # Converts to a string so it can 'delete it.'
            num = 0
            num = str(num)
            print('Where do you want to withdraw your move?')
            c_row = int(input('Which row do you want to withdraw from?: '))
            col = int(input('Which column do you want to withdraw from?: '))
            sudoku[c_row][col] = " "
            # Prints where you withdrew things.
            print('You withdrew row:', c_row, '\nYou withdrew column:', col, '\nThe number you withdrew:', num)
            print('#' * 51)
            update_board(turns, s_time)
            continue

        # If row is H get random numbers and then retrieve the num to tell the player where they can do a move.
        elif row == 'h':
            # Get random numbers and then print what each of them are to show the human.
            row = [0, 1, 2, 3, 4, 5, 6, 7, 8]
            col = [0, 1, 2, 3, 4, 5, 6, 7, 8]
            row = random.choice(row)
            col = random.choice(col)
            num = sudoku_solved[row][col]
            # Once it gets the num convert it to an int.
            num = int(num)
            print('#' * 51)
            # Shows where the row, col and num is and the values for the player to type in.
            print('Help:\nRow: ', row, '\nColumn: ', col, '\nNumber: ', num)
            continue

        # Leaving the board.
        elif row == 'leave':
            sys.exit()

        else:
            print('#' * 51)
            print('That is not an integer.\nMake sure you are inputing integers. I.e: 1, 2, 3, 4, 5, 6, 7, 8, 9')
            print('#' * 51)
            continue
        #############################################################
        # What the column should be.
        col = input('Which column do you want to change?: ')
        # Checks if the col is a number.
        if col.isdigit():
            # If it is then make it an int.
            col = int(col)
            c_col = col
            # If row is more than 9 print it's an invalid number
            if col > 9:
                print('#' * 51)
                print('That is not a valid row.')
                print('#' * 51)
                continue

        # If the row is equal to withdraw it will withdraw your last row and col position.
        elif col == 'withdraw':
            num = 0
            num = str(num)
            print('Where do you want to withdraw your move?')
            row = int(input('Which row do you want to withdraw from?: '))
            c_col = int(input('Which column do you want to withdraw from?: '))
            sudoku[row][c_col] = " "
            print('You withdrew row:', row, '\nYou withdrew column:', c_col)
            print('#' * 51)
            update_board(turns, s_time)
            continue

        # Leaving the board.
        elif row == 'leave':
            sys.exit()

        # If the row is equal to H it will choose a random row and col and tell you what to put there.
        elif col == 'h':
            # Get random numbers and then print what each of them are to show the human.
            row = [0, 1, 2, 3, 4, 5, 6, 7, 8]
            col = [0, 1, 2, 3, 4, 5, 6, 7, 8]
            row = random.choice(row)
            col = random.choice(col)
            num = sudoku_solved[row][col]
            # Once it gets the num convert it to an int.
            num = int(num)
            print('#' * 51)
            # Shows where the row, col and num is and the values for the player to type in.
            print('Help:\nRow: ', row, '\nColumn: ', col, '\nNumber: ', num)
            continue

        # If it isn't any of these then it will say it's not an integer.
        else:
            print('#' * 51)
            print('That is not an integer. Make sure you are inputting integers. I.e: 1, 2, 3, 4, 5, 6, 7, 8, 9\n'
                  'If you are looking to withdraw, type: withdraw\n'
                  "If you need help type: 'h'"
                  )
            print('#' * 51)
            continue

        # Asks what number the user wants to input into the row and column they selected earlier.
        num = input('What number do you want to go there?: ')
        human_is_valid(row, col, num)
        # After the player finishes all it will +1 to turn.
        turns += 1
        update_board(turns, s_time)


def human_is_valid(row, col, num):

    # If the space is empty it'll put the num in the cell. If it's empty it'll say it isn't clear and not place the num.
    if sudoku[row][col] == ' ':
        sudoku[row][col] = num
    else:
        print('#' * 74)
        print("Column or Row isn't free.")
        print('#' * 74)

    if sudoku[row][col] == '':
        complete_failed()


def play_choose():
    while True:
        # Choosing player!
        Player_Type = input('Choose player type (human or computer): ')
        if Player_Type == 'human':
            human_play(turns, s_time)
            break
        if Player_Type == 'computer':
            computer_play(s_time, turns)
            break
        else:
            print('Invalid Player Type!\nPlease choose again.')


play_choose()
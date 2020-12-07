#Step 1: Write a function that can print out a board. Set up your board as a list,
# where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.

# Use for real #board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
#x
#board = ['0','X','2','3','4','5','6','7','8','9']
#board = ['X','X','O','O','X','O','X','O','X','O']

def display_board(board):
    #print('\n' * 100)
    #print('   |   |   ')
    print(' '+ board[7] + ' |' + ' '+board[8] + ' |' + ' '+ board[9])
    print('---------')
    print(' '+ board[4] + ' |' + ' '+board[5] + ' |' + ' '+ board[6])
    print('---------')
    print(' '+ board[1] + ' |' + ' '+board[2] + ' |' + ' '+ board[3])
    #print('   |   |   ')
#Test-Succeeded
#test_board = ['#','X','O','X','O','X','O','X','O','X']
#new_display_board(test_board)

#Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'.
# Think about using while loops to continually ask until you get a correct answer.

def player_input():
    marker=''
    while not (marker=='X' or marker=='O'):
        marker=input('Player 1, select your marker X or O').upper()
    if marker == 'X':
        return ('X','O')
    else:
        return('O','X')

#player_input() test succeeded - returns a tuple of ('X','O') or ('O','X') for player1 and player 2 values

def place_marker(board, marker, position):
    board[position] = marker

#place_marker(blank_board,'X',9)
#display_board(board)

#Step 4: Write a function that takes in a board and checks to see if someone has won.
#print(board[1:10:4])
#display_board(board)
#   print(board[0:9:4])

def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9]==mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[1] == mark and board[5] == mark and board[9] == mark) or
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark))
    #print(x)

#Step 5: Write a function that uses the random module to randomly decide which player goes first.
# You may want to lookup random.randint() Return a string of which player went first.
#import random
#print(random.randint(0, 1 ))

def choose_first():
    import random
    if random.randint(0,1)==0:
        return 'Player 2'
    else:
        return 'Player 1'

#print(choose_first())
# testing completed

#Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.
# So if space is empty, it returns True - if Space is filled with X or O, it returns False

def space_check(board, position):

    if board[position] == 'X' or board[position]== 'O':
        return False
    else:
        return True

#print(space_check(board,1))
# Testing completed

#Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.
#Use the space_check() function to check on this.
def full_board_check(board):
    for position in range(1,10):
        if space_check(board,position) == True:
            return False
    return True

#print (board[1:10])
#print(full_board_check(board)) - Test condition satisfied and Tested output correctly.

#Step 8: Write a function that asks for a player's next position (as a number 1-9)
# and then uses the function from step 6 to check if it's a free position.
# If it is, then return the position for later use.

def player_choice(board):
    next_position=0
    while next_position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,next_position):
        next_position = int(input('Please Select next position : (1-9)'))
    return next_position


#print(player_choice(board)) - Test completed.

#Step 9: Write a function that asks the player if they want to play again
# and returns a boolean True if they do want to play again.

def replay():
    answer = ''
    while answer not in ['y','n']:
        answer = input('Do you want to Play again? Enter Y/N : ').lower()
    return(answer == 'y')

# print(replay()) - testing completed

#Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!
##################
##################
##################

print('Welcome to Tic Tac Toe!')
# while True:
while True:
    the_board = ['']*10
    player1_marker,player2_marker= player_input()
    turn = choose_first()
    print(turn + ' will play First')

    play_game = input('Are you READY to Play TIC TAC TOE ? Y/N')
    if play_game.lower()=='y':
        game_on=True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display_board(the_board)
            position=player_choice(the_board)
            place_marker(the_board,player1_marker,position)

            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Congratulations ! Player 1, you have won the Game !')
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The Game is a Draw !')
                    break
                else:
                    turn='Player 2'

        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player2_marker,position)

            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('Congratulations ! Player 2, you have won the Game !')
                game_on = False

            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The Game is a Draw')
                    break
                else:
                    turn='Player 1'

    if not replay():
        break

# Set the game up here

# pass

# while game_on:

# Player 1 Turn


# Player2's turn.

# pass

# if not replay():

# break









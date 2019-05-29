from IPython.display import clear_output

board = [' ']*10
game_val = True
message = ''


def reset_game():
    global board,game_state
    board = [' '] * 10
    game_val = True
    

print('Board for referencing the input positions')
print('7 | 8 | 9')
print('---------')
print('4 | 5 | 6')
print('---------')
print('1 | 2 | 3\n\n')


def display_board():
   # clear_output()
    print('\n'+board[7]+' | '+board[8]+' | '+board[9])
    print('---------')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('---------')
    print(board[1]+' | '+board[2]+' | '+board[3])
    


def game_check(board, player):
    return (board[1] ==  board[2] ==  board[3] == player) or \
           (board[4] ==  board[5] ==  board[6] == player) or \
           (board[7] ==  board[8] ==  board[9] == player) or \
           (board[1] ==  board[4] ==  board[7] == player) or \
           (board[2] ==  board[5] ==  board[8] == player) or \
           (board[3] ==  board[6] ==  board[9] == player) or \
           (board[1] ==  board[5] ==  board[9] == player) or \
           (board[3] ==  board[5] ==  board[7] == player)
    

def board_check(board):
    if ' ' in board[1:]:
        return False
    else:
        return True

    
def player_input(inpt):
##choose the place where to place 'X' and 'O'    
    global board
    ask = '\nChoose where to place your {}: '.format(inpt)
    while True:
        try:
            marker = int(input(ask))
        except ValueError:
            print("Invalid Input. Please input a number between 1-9.")
            continue

        if marker not in range(1,10):
            print("Invalid Input. Please input a number between 1-9.")
            continue

        if board[marker] == " ":
            board[marker] = inpt
            break
        else:
            print ("That place is not empty!")
            continue

def player_choice(inpt):
    global board,game_val,message
    message = ''
    inpt = str(inpt)
    player_input(inpt)

    #Check for player win
    if game_check(board,inpt):
        message = inpt +" wins! Congratulations\n\n"
        game_val = False
    
    #Show board
    #clear_output()
    display_board()

    #Check for a tie 
    if board_check(board):
        message = "Tie!\n\n"
        game_val = False
        
    return game_val,message


def play_game():
    reset_game()
    global message
    
    X='X'
    O='O'
    while True:        
        # Player X 
        game_val,message = player_choice(X)
        print (message)
        if game_val == False:
            break
            
        # Player O 
        game_val,message = player_choice(O)
        print (message)
        if game_val == False:
            break
    
    # Ask player for a play again
    replay = input('Would you like to play again? y/n : ')
    if replay == 'y':
        play_game()
    else:
        print ("Thanks for playing!")


play_game()


X = "X"
O = "O"
EMPTY = " "
TIE = "Draw"
NUM_SQUARES = 9

def display_instruct():
    #displays instructions for the player
    print(
        '''
Welcome to the ring!
your brain and your processor will come together in a battle for the Board of the game "TIC-TAC-toe" 
To make a move. Enter a number from 0 to 8.
The numbers uniquely correspond to the Board fields-as shown below 
0 | 1 | 2
---------
3 | 4 | 5 
---------
6 | 7 | 8
Get ready to fight!!!
    '''
    )

def ask_yes_no(question):
    #asks a question with the answer "Yes" or " No"
    response = None
    while response not in ('y', 'n'):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    #asks you to enter a number from the range
    response = None 
    while response not in range(low, high):
        response = int(input(question))
    return response

def pieces():
    #determines the ownership of the first move
    go_first = ask_yes_no('Do you want to keep the first move? (y/n):')
    if go_first == 'y':
        print('\nI give you a head start playing with crosses')
        human = X
        computer = O
    else:
       print("\nYour generosity will ruin you! I'm walking!")
       computer = X 
       human = O
    return computer, human


#creates a new game board
def new_board():
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    #displays the game board on the screen
    print('\n\t', board[0],'|', board[1], '|', board[2])
    print('\t', '---------')
    print('\t', board[3],'|', board[4], '|', board[5])
    print('\t', '---------')
    print('\t', board[6],'|', board[7], '|', board[8], '\n')

def legal_movies(board):
    #creates a list of available moves
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def winner(board):
    #determine the winner
    WAYS_TO_WIN = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    )
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner

        if EMPTY not in board:
            return TIE
    return None

def human_move(board, human):
    legal = legal_movies(board)
    move = None 
    while move not in legal:
        move = ask_number("it's your move! select one of the fields (0-8):", 0, NUM_SQUARES)
        if move not in legal:
            print('\nThis field is occupied. Choose another!\n')
    print('ooookay')
    return move

def computer_move(board, computer, human):
    #creating a working copy of the Board
    board = board[:]
    #fields from best to worst
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("I'll choose a field...", end=' ')
    for move in legal_movies(board):
        board[move] = computer
        #if the computer can win the next move, it chooses this move
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY
    for move in legal_movies(board):
        board[move] = human
        #if the next move can win a person, then block this move
        if winner(board) == human:
            print(move)
            return move
    board[move] = EMPTY
    #since neither side can win the next move
    for move in BEST_MOVES:
        print(move)
        return move


#performs a move transition
def next_turn(turn):
    if turn == X:
        return O
    else:
        return X

#congratulate the winner
def congrat_winner(the_winner, computer, human):
    if the_winner != TIE:
        print('Three', the_winner,'in a row\n')
    else:
        print('Draw')
    
    if the_winner == computer:
        print("A man can't handle my power")
    elif the_winner == human:
        print('Whimper... Motherboard and this man insulted me')
    elif the_winner == TIE:
        print('Well a draw is a draw')

def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)

main()
input('\nPress Enter to exit')
import random


def display_board(board):
    print('\n'*100)
    print('  |   |  ')
    print(f'{board[7]} | {board[8]} | {board[9]}')
    print('  |   |  ')
    print('---------')
    print('  |   |  ')
    print(f'{board[4]} | {board[5]} | {board[6]}')
    print('  |   |  ')
    print('---------')
    print('  |   |  ')
    print(f'{board[1]} | {board[2]} | {board[3]}')
    print('  |   |  ')


def player_input():
    right_answer = False
    while not right_answer:
        player1 = input('Player 1: Do you want to be X or O?').upper()
        player2 = ''
        if player1 == 'X':
            player2 = 'O'
            right_answer = True
        elif player1 == 'O':
            player2 = 'X'
            right_answer = True
        else:
            pass
    return (player1, player2)


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):

    win = (mark, mark, mark)
    if win == (board[1], board[2], board[3]):
        return True
    elif win == (board[4], board[5], board[6]):
        return True
    elif win == (board[7], board[8], board[9]):
        return True
    elif win == (board[1], board[4], board[7]):
        return True
    elif win == (board[2], board[5], board[8]):
        return True
    elif win == (board[3], board[6], board[9]):
        return True
    elif win == (board[7], board[5], board[3]):
        return True
    elif win == (board[9], board[5], board[1]):
        return True
    else:
        return False


def choose_first():
    first_player = random.randint(1, 2)
    print(f'player {first_player} is going first')
    return first_player


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    print(f' Hey there was a Tie!')
    return True


def player_choice(board):

    next_pos = 0
    while next_pos not in range(1, 10):
        next_pos = int(input("Choose your next position: (1-9) "))

        if space_check(board, next_pos):
            return next_pos
        else:
            print("Position is not available")
            next_pos = 0


def replay():

    response = input("Wanna play again???? (Y/N)")
    if response == 'Y':
        return True
    else:
        return False


print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    game_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player1, player2 = player_input()
    start = choose_first()

    if start == 1:
        marker = player1
    else:
        marker = player2

    while not full_board_check(game_board):
        if marker == player1:
            next_pos = player_choice(game_board)
            place_marker(game_board, marker, next_pos)
            marker = player2
        else:
            next_pos = player_choice(game_board)
            place_marker(game_board, marker, next_pos)
            marker = player1
        display_board(game_board)
        if win_check(game_board, player1):
            print(f'Congratulations player 1 you won!')
            break
        elif win_check(game_board, player2):
            print(f'Congratulations player2 you won!')
            break
        else:
            pass

    if not replay():
        break
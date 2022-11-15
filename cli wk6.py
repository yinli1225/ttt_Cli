# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import Game, Human


if __name__ == '__main__':
    # board = make_empty_board()
    # winner = None
    # current_player = '0'
    # while winner == None:
    #     print("TODO: take a turn!")
    #     for row in board:
    #         print(row) # TODO: Show the board to the user.
    #     row = int(input('enter row')) # TODO: Input a move from the player.
    #     col = int(input('enter col'))

    #     #if not / continue
    #     #if board[row][col] is not None, 
    #     print(row, col)

    #     if current_player == '0':
    #         board[row][col] = 'O' 
    #     if current_player == '1':
    #         board[row][col] = 'X' 
    #     winner = get_winner(board) 
    #     if winner is not None: 
    #         print(winner)  
    #     # TODO: Update the board.
    #     current_player = other_player(current_player) # TODO: Update who's turn it is.
    
    player1 = Human()
    player2 = Human()
    game = Game(player1, player2)
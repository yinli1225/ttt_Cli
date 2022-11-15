# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.
class Board:
    def __init__(self):
        self.board = [    
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

    def get_winner(self):
        """Determines the winner of the given board.
        Returns 'X', 'O', or None."""

        if self.board[0][0] == self.board[0][1] == self.board[0][2]:
            return self.board[0][0]
        if self.board[1][0] == self.board[1][1] == self.board[1][2]:
            return self.board[1][0]                
        if self.board[2][0] == self.board[2][1] == self.board[2][2]:
            return self.board[2][0]
        if self.board[0][0] == self.board[1][0] == self.board[2][0]:
            return self.board[0][0]
        if self.board[0][1] == self.board[1][1] == self.board[2][1]:
            return self.board[0][1]
        if self.board[0][2] == self.board[1][2] == self.board[2][2]:
            return self.board[0][2]
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[0][2]

        return None


def other_player(self, player):
    """Given the character for a player, returns the other player."""
    if player == '1':
        return '0'
    if player == '0':
        return '1'

def get_bot_nextmove()

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
    
    def run(self):
        game_not_over = Board.get_winner(self.board) is None
        make_move = 
        current_player = other_player(self, player)

        while game_not_over:
            make_move(self.board, current_player)

class Human:
    def get_move(self, board):
        raise NotImplementedError

class Bot:
    def get_move(self, board):
        raise NotImplementedError


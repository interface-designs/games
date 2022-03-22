from game_interface.interface import *
from games.enums.chess import *


class ChessBoard(GameState):
    def __init__(self, rows=8, columns=8, initial_state:str=''):
        self.state_str = initial_state
        self.rows = rows
        self.columns = columns
        self.set_board()

    def set_board(self):
        if self.state_str:
            raise Exception('Need to implement setting the board from an input string functionality!')
        else:
            self.state = {
                i: {
                    chr(ord('a') + j): ChessPiece(True, i, chr(ord('a') + j)) for j in range(8)
                } for i in range(1,9)
            }

    def get_turn(self):
        return self.turn

    def update(self):
        raise NotImplemented

    def raster_scan(self):
        print(self.state)


class Chess(Game):
    def __init__(self, state: ChessBoard, players: list[Player] = []):
        self.state = state
        self.winner = None

        self.players = players
        if not self.players:
            self.players = [Player('Steve', 'NY', 'steve@wayfair.com', 7777777777), Player('Josh', 'ATX', 'josh@wayfair.com', 5125650859)]

    def get_players(self, id=None):
        if id:
            return self.players[id]
        return self.players

    def move(self):
        self.state.update(move)

    def print_state(self):
        self.state.raster_scan()

    def get_winner(self):
        if self.winner:
            return self.winner
        return "No winner yet."


class ChessPiece(GamePiece):
    start_map = {
        1: {
            'a': (
                'Rook',
                Movements.rook
            ),
            'b': (
                'Knight',
                Movements.knight
            ),
            'c': (
                'Bishop',
                Movements.bishop
            ),
            'd': (
                'Queen',
                Movements.queen
            ),
            'e': (
                'King',
                Movements.king
            ),
            'f': (
                'Bishop',
                Movements.bishop
            ),
            'g': (
                'Knight',
                Movements.knight
            ),
            'h': (
                'Rook',
                Movements.rook
            )
        },
        2: {
           'a': (
                'Pawn',
                Movements.pawn
            ),
            'b': (
                'Pawn',
                Movements.pawn
            ),
            'c': (
                'Pawn',
                Movements.pawn
            ),
            'd': (
                'Pawn',
                Movements.pawn
            ),
            'e': (
                'Pawn',
                Movements.pawn
            ),
            'f': (
                'Pawn',
                Movements.pawn
            ),
            'g': (
                'Pawn',
                Movements.pawn
            ),
            'h': (
                'Pawn',
                Movements.pawn
            ) 
        },
        3: {
            'a': (),
            'b': (),
            'c': (),
            'd': (),
            'e': (),
            'f': (),
            'g': (),
            'h': ()
        },
        4: {
            'a': (),
            'b': (),
            'c': (),
            'd': (),
            'e': (),
            'f': (),
            'g': (),
            'h': ()
        },
        5: {
            'a': (),
            'b': (),
            'c': (),
            'd': (),
            'e': (),
            'f': (),
            'g': (),
            'h': ()
        },
        6: {
            'a': (),
            'b': (),
            'c': (),
            'd': (),
            'e': (),
            'f': (),
            'g': (),
            'h': ()
        },
        7: {
           'a': (
                'Pawn',
                Movements.pawn
            ),
            'b': (
                'Pawn',
                Movements.pawn
            ),
            'c': (
                'Pawn',
                Movements.pawn
            ),
            'd': (
                'Pawn',
                Movements.pawn
            ),
            'e': (
                'Pawn',
                Movements.pawn
            ),
            'f': (
                'Pawn',
                Movements.pawn
            ),
            'g': (
                'Pawn',
                Movements.pawn
            ),
            'h': (
                'Pawn',
                Movements.pawn
            )  
        },
        8: {
           'a': (
                'Rook',
                Movements.rook
            ),
            'b': (
                'Knight',
                Movements.knight
            ),
            'c': (
                'Bishop',
                Movements.bishop
            ),
            'd': (
                'Queen',
                Movements.queen
            ),
            'e': (
                'King',
                Movements.king
            ),
            'f': (
                'Bishop',
                Movements.bishop
            ),
            'g': (
                'Knight',
                Movements.knight
            ),
            'h': (
                'Rook',
                Movements.rook
            )
        }
    }

    def __init__(self, start, row, column):
        if start:
            self.name, self.movments = 'Empty', None
            if len(self.start_map[row][column]) > 0:
                self.name, self.movments = self.start_map[row][column]

    def get_name(self):
        return self.name

    def get_movements(self):
        return self.movements

    def get_image(self, size):
        return self.image

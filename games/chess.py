from game_interface.interface import *


class ChessBoard(GameState):
    def __init__(self, rows=8, columns=8, initial_state:str=''):
        self.state = self.set_board(initial_state, rows, columns)
        print(self.state)

    def set_board(state_str, rows, columns):
        state = {}
        if state_str:
            raise Exception('Need to implement setting the board from an input string functionality!')
        else:
            state = {
                i: {
                    chr(ord('a') + j) for j in range(8)
                } for i in range(1,9)
            }

        return state
        
    # def set_piece(self, piece:Piece):
    #     pass

    # def update(self, move: Move):
    #     pass

    def get_turn(self):
        return self.turn

    def raster_scan(self):
        pass


class Chess(Game):
    def __init__(self, state: ChessBoard, players: list[Player] = []):
        self.state = state

        self.players = players
        if not self.players:
            self.players = [Player(), Player()]

    def get_player(self, id=None):
        if id:
            return self.players[id]
        return self.players

    def move(self, move: Move):
        self.state.update(move)



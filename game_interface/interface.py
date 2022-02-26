from abc import ABC, abstractmethod
from person_interface.interface import Person

class Game(ABC):
    @abstractmethod
    def get_players(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def get_winner(self):
        pass

    @abstractmethod
    def print_state(self):
        pass


class GameState(ABC):
    @abstractmethod
    def raster_scan(self):
        pass

    @abstractmethod
    def update(self):
        pass

    def get_turn(self):
        pass


class GamePiece(ABC):
    @abstractmethod
    def get_name(self):
        pass

    def get_movements(self):
        pass

    def get_image(self, size):
        pass


class Player(Person):
    def info(self):
        print(self.name)
        print(self.email)
        print(self.phone)
        print(self.address)





###########################################
def get_row(size, color=0):
    row = []
    for i in range(size*8):
        if i > 0 and i % size == 0:
            color = (color + 1) % 2
        row.append(color)
    return row


def chess_board(size=10):
    board = []
    color = 0
    for i in range(8):
        for j in range(size):
            board += get_row(size, color)
        color = (color + 1) % 2

    return board


# size = int(sys.argv[1])
# board = chess_board(size)

# start = 0
# end = size * 8
# while end <= len(board):
#     print(board[start:end])
#     start = end
#     end += size * 8

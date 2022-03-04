from enum import Enum


class Movements(Enum):
    rook = [(-1,i) for i in range(-7,8)] + [(i,0) for i in range(-7,8)]
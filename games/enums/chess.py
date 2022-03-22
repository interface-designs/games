from enum import Enum


class Movements(Enum):
    rook = [(0,i) for i in range(-8,8)] + [(i,0) for i in range(-8,8)]
    knight = [(2,3), (-2,3), (3,2), (-3,2), (2,-3), (-2,-3), (3,-2), (-3,-2)]
    bishop = [(1,1) for i in range(-8,8)] + [(1,-1) for i in range(-8,8)] + [(-1,-1) for i in range(-8,8)] + [(-1,1) for i in range(-8,8)]
    queen = rook + bishop
    king = [(1,1),(1,-1),(-1,1),(-1,-1),(1,0),(0,1),(-1,0),(0,-1)]
    pawn = [(1,0)] #special unidirectional case???????

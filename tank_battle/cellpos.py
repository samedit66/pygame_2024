from direction import Direction
from settings import Settings 

class CellPos():
    def __init__(self, col, row):
        self.col = col 
        self.row = row

    def __str__(self):
        return f'CellPos(col={self.col}, row={self.row})'

    def __eq__(self, other_pos):
        return (self.col == other_pos.col) and (self.row == other.pos.row)


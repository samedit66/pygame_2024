from direction import Direction
from settings import Settings


class CellPos():

    def __init__(self, col, row):
        self.col = col
        self.row = row

    def __str__(self):
        return f'CellPos(col={self.row})' 

    def __eq__(self, other_pos):
        return (self.col == other_pos.col) and (self.row == other_pos.row)

cell_pos1 =  CellPos(10, 10)
cell_pos2 = CellPos(13, 14)
print(cell_pos1 == cell_pos2)
print(cell_pos1)
from direction import Direcction
from settings import Settings

class CellPos():
    def __init__(self, col, row):
        self.col = col
        self.row = row

    def __str__(self) -> str:
        return f"CellPos(col={self.col}, row={self.row})"

    def __eq__(self, other_pos):
        return (self.col == other_pos.col) and (self.row == other_pos.row)
    

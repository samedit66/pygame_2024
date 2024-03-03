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
    
    @staticmethod
    def _is_valid_pos(col, row):
        return (Settings.MIN_ROW_INDEX <= row <= Settings.MAX_ROW_INDEX) and \
        (Settings.MIN_COL_INDEX <= col <= Settings.MAX_COL_INDEX)

    def get_neighbor(self, direction):
        neighbor_col = self.col
        neighbor_row = self.row

        if direction == Direcction.UP:
            neighbor_row -= 1
        elif direction == Direcction.DOWN:
            neighbor_row += 1
        elif direction == Direcction.LEFT:
            neighbor_col -= 1
        elif direction == Direcction.RIGHT:
            neighbor_col += 1
            
        # если в ходе вычислений получилась неправильная позиция, то веернуть признак, что соседа нет
        if CellPos._is_valid_pos(neighbor_col, neighbor_row):
            return None
        
        return CellPos(neighbor_col, neighbor_row)

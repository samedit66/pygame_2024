from direction import Direction
from settings import Settings


class CellPos():
    def __init__(self, col, row):
        self.col = col
        self.row = row

    def __str__(self):
        return f'CellPos(col={self.col}, row={self.row})'

    def __eq__(self, other_pos):
        return (self.col == other_pos.col) and (self.row == other_pos.row)

    @staticmethod
    def _is_valid_pos(col, row):
        return (Settings.MIN_ROW_INDEX <= row <= Settings.MAX_ROW_INDEX) and \
            (Settings.MIN_COL_INDEX <= col <= Settings.MAX_COL_INDEX)
     


    def get_neighbour(self, direction):
        neighbour_col = self.col
        neighbour_row = self.row

        if direction == Direction.UP:
            neighbour_row -= 1
        elif direction == Direction.DOWN:
            neighbour_row += 1
        elif direction == Direction.LEFT:
            neighbour_col -= 1
        elif direction == Direction.RIGHT:
            neighbour_col += 1

        # Если в ходе вычислений получислось неправильная позиция,
        # вернуть признак, что соседа в заданном направлении нет
        if not CellPos._is_valid_pos(neighbour_col, neighbour_row):
            return None
        
        return CellPos(neighbour_col, neighbour_row)
    
    @staticmethod
    def position_to_pixel(position):
        if isinstance(position, tuple):
            col = position[0]
            row = position[1]
        else:
            col = position.col 
            row = position.row
        return(col * Settings.CELL_SIZE, row * Settings.CELL_SIZE)

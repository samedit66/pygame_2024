from direction import Direction
from settings import Settings


class FieldPos():
    
    def __init__(self, field, col, row):
        self._field = field
        self._col = col
        self._row = row

    @property
    def col(self):
        return self._col

    @property
    def row(self):
        return self._row

    def get_neighbor(self, direction):
        neighbor_col = self.col 
        neighbor_row = self.row

        if direction == Direction.UP:
            neighbor_row -= 1
        elif direction == Direction.DOWN:
            neighbor_row += 1
        elif direction == Direction.LEFT:
            neighbor_col -= 1
        elif direction == Direction.RIGHT:
            neighbor_col += 1
        
        # Соседа в заданном направлении нет
        if not self._field.is_valid_pos(neighbor_col, neighbor_row):
            return None

        return FieldPos(self._field, neighbor_col, neighbor_row)

    def __eq__(self, other_position):
        return  (self.col == other_position.col) and (self.row == other_position.row)
    
    def __str__(self):
        return f'FieldPos(col={self.col}, row={self.row})'

    @staticmethod
    def position_to_pixel(position):
        if isinstance(position, tuple):
            col = position[0]
            row = position[1]
        else:
            col = position.col
            row = position.row
        return (Settings.CELL_SIZE * col, Settings.CELL_SIZE * row)
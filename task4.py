class Figure():

    def __init__(self, color, cell):
        self.color = color
        self.cell = cell
        self.cell.figure = self
        self.name = 'Figure'

    def can_move(target):
        return True
    
    def move_figure(target):
        pass


class Bishop(Figure):
    def __init__(self, color, cell):
        super().__init__(color, cell)
        self.name = 'Bishop black' if color == 'black' else 'Bishop white' 

class King(Figure):
    def __init__(self, color, cell):
        super().__init__(color, cell)
        self.name = 'King black' if color == 'black' else 'King white'

class Knight(Figure):
    def __init__(self, color, cell):
        super().__init__(color, cell)
        self.name = 'Knight black' if color == 'black' else 'Knight white'

class Pawn(Figure):
    def __init__(self, color, cell):
        super().__init__(color, cell)
        self.name = 'Pawn black' if color == 'black' else 'Pawn white'

class Queen(Figure):
    def __init__(self, color, cell):
        super().__init__(color, cell)
        self.name = 'Queen black' if color == 'black' else 'Queen white' 

class Rook(Figure):
    def __init__(self, color, cell):
        super().__init__(color, cell)
        self.name = 'Rook black' if color == 'black' else 'Rook white' 
        

class Cell():

    def __init__(self, color, x, y, figure):
        self._color = color
        self._x = x
        self._y = y
        self.figure = figure

    def get_color(self):
        return self._color
    
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y


class Board():
    cells = []

    def init_cells(self):
        for i in range(8):
            row = []
            for j in range(8):
                if (i + j) % 2 != 0:
                    row.append(Cell('black', j, i, None)) #black cells
                else:
                    row.append(Cell('white', j, i, None)) #white cells
            
            self.cells.append(row)
    
    def get_cell(self, x, y):
        return self.cells[y][x]
    
    def __add_pawns(self):
        for i in range(8):
            Pawn('black', self.get_cell(i, 1))
            Pawn('white', self.get_cell(i, 6))

    def add_figures(self):
        self.__add_pawns()



board = Board()
board.init_cells()
board.add_figures()


for row in board.cells:
    for cell in row:
        print(f"Cell's color: {cell.get_color()}. Cell's coordinates: x-{cell.get_x()} y-{cell.get_y()}. Figure on cell: {cell.figure.name if cell.figure != None else 'Figure'}")


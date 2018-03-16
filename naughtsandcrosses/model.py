from enum import Enum

class Player(Enum):
    NAUGHT = 0
    CROSS = 1


class Winner(Enum):
    NAUGHT = Player.NAUGHT.value
    CROSS = Player.CROSS.value
    NONE = 2
    TIE = 3


class CellValue(Enum):
    NAUGHT = Player.NAUGHT.value
    CROSS = Player.CROSS.value
    EMPTY = 2


class CellPosition:
    def __init__(self, row, column):
        self.row, self.column = row, column
    
    def __eq__(self, other):
        return (other != None) and (self.row == other.row) and (self.column == other.column)


class BoardCell:
    def __init__(self, position, value = CellValue.EMPTY):
        self.position = position
        self.value = value
    
    def __eq__(self, other):
        return (self.position == other.position) and (self.value == other.value)


class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [[BoardCell(CellPosition(row, column)) for column in range(size)] for row in range(size)]

    def getLines(self):
        rows = self.grid
        columns = [[self.grid[row][column] for row in range(self.size)] for column in range(self.size)]
        diagonals = [[self.grid[row][row] for row in range(self.size)], [self.grid[row][self.size - row - 1] for row in range(self.size)]]
        return rows + columns + diagonals
    
    def getWinner(self):
        for line in self.getLines():
            values_in_line = set([c.value for c in line])
            if (len(values_in_line) == 1) and ((CellValue.NAUGHT in values_in_line) or (CellValue.CROSS in values_in_line)):
                return Winner(list(values_in_line)[0].value)
        
        is_full = CellValue.EMPTY not in [cell.value for row in self.grid for cell in row]
        return Winner.TIE if is_full else Winner.NONE


class GameState:
    def __init__(self, board, player1, player2):
        self.board = board
        self.current_player = Player.NAUGHT
        self.players = [player1, player2]
        
    def getCurrentPlayer(self):
        return self.players[self.current_player.value]
        
    def applyMove(self, movePosition):
        self.board.grid[movePosition.row][movePosition.column].value = CellValue.NAUGHT if self.current_player == Player.NAUGHT else CellValue.CROSS
        self.current_player = Player.NAUGHT if self.current_player == Player.CROSS else Player.CROSS

from naughtsandcrosses.model import Player, CellValue, CellPosition
from pip._vendor.pyparsing import line

class HumanPlayer:
    def __init__(self, player, key_position_lookup):
        self.player = player
        self.key_position_lookup = key_position_lookup
    
    def getMove(self, board):
        while True:
            move = input("%s turn to move: " % ("Naught's" if self.player == Player.NAUGHT else "Cross'"))
            
            if move == "q":
                return None
            
            cellPosition = self.key_position_lookup.get(move)
            if cellPosition == None:
                print("Invalid input.")
            elif board.grid[cellPosition.row][cellPosition.column].value != CellValue.EMPTY:
                print("The specified cell is occupied.")
            else:
                return cellPosition


class AiPlayer:
    def __init__(self, player):
        self.player = player
    
    def getMove(self, board):
        if (board.size == 3) and (board.grid[1][1].value == CellValue.EMPTY):
            return CellPosition(1, 1)
        
        min_open_space_count_line = self.getMinOpenSpaceCountLine(board)
        is_line_instant_win = (min_open_space_count_line != None) and (sum([1 for _ in filter(lambda c: c.value == CellValue.EMPTY, min_open_space_count_line)]) == 1)
        if is_line_instant_win:
            return self.getEmptyCellPosition(min_open_space_count_line)
        
        board_lines = board.getLines()
        opponent_player = Player.CROSS if self.player == Player.NAUGHT else Player.NAUGHT
        opponent_win_line = next(filter(lambda l: self.isLineOpen(opponent_player, l) and self.getOpenSpaceCount(l) == 1, board_lines), None)
        
        if opponent_win_line != None:
            return self.getEmptyCellPosition(opponent_win_line)
        
        if min_open_space_count_line != None:
            return self.getEmptyCellPosition(min_open_space_count_line)
        
        return next(filter(lambda c: c.value == CellValue.EMPTY, [c for r in board.grid for c in r])).position
    
    def getMinOpenSpaceCountLine(self, board):
        board_lines = board.getLines()
        open_lines = filter(lambda l: self.isLineOpen(self.player, l), board_lines)
        min_open_space_count = board.size + 1
        min_open_space_count_line = None
        for line in open_lines:
            open_space_count = self.getOpenSpaceCount(line)
            if open_space_count < min_open_space_count:
                min_open_space_count = open_space_count
                min_open_space_count_line = line
        
        return min_open_space_count_line
            
    def isLineOpen(self, player, line):
        opponent_cell_value = CellValue.NAUGHT if player == Player.CROSS else CellValue.CROSS
        return all(map(lambda c: c.value != opponent_cell_value, line))
    
    def getOpenSpaceCount(self, line):
        return sum([1 for _ in filter(lambda c: c.value == CellValue.EMPTY, line)])
    
    def getEmptyCellPosition(self, line):
        return next(filter(lambda c: c.value == CellValue.EMPTY, line)).position
    

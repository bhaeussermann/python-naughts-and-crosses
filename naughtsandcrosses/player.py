from naughtsandcrosses.model import Player, CellValue

class HumanPlayer:
    def __init__(self, key_position_lookup):
        self.key_position_lookup = key_position_lookup
    
    def getMove(self, game_state):
        while True:
            move = input("%s turn to move: " % ("Naught's" if game_state.current_player == Player.NAUGHT else "Cross'"))
            
            if move == "q":
                return None
            
            cellPosition = self.key_position_lookup.get(move)
            if cellPosition == None:
                print("Invalid input.")
            elif game_state.board.grid[cellPosition.row][cellPosition.column].value != CellValue.EMPTY:
                print("The specified cell is occupied.")
            else:
                return cellPosition

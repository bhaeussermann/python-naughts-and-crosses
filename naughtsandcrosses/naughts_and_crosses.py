import sys, os
sys.path.append(os.path.abspath('.'))

from naughtsandcrosses.model import Board, Winner, CellValue, GameState, Player
from naughtsandcrosses.player import HumanPlayer, AiPlayer
from naughtsandcrosses.cli_helper import getPositionLookup

def printBoard(board, get_cell_character_func):
    for row in board:
        print("|".join(map(get_cell_character_func, row)))

def cellToCharacter(cell):
    if cell.value == CellValue.NAUGHT:
        return "o"
    elif cell.value == CellValue.CROSS:
        return "x"
    else:
        return " "

def run(key_position_lookup, human_player):
    board = Board(3)
    gameState = \
        GameState(board, HumanPlayer(Player.NAUGHT, key_position_lookup), AiPlayer(Player.CROSS)) if human_player == Player.NAUGHT else \
        GameState(board, AiPlayer(Player.NAUGHT), HumanPlayer(Player.CROSS, key_position_lookup))
    
    while board.getWinner() == Winner.NONE:
        print()
        printBoard(gameState.board.grid, cellToCharacter)
        move = gameState.getCurrentPlayer().getMove(gameState.board)
        if move == None:
            return
        
        gameState.applyMove(move)
    
    print()
    printBoard(gameState.board.grid, cellToCharacter)
    
    winner = board.getWinner()
    if winner == Winner.NAUGHT:
        print("Naughts is the winner!")
    elif winner == Winner.CROSS:
        print("Cross is the winner!")
    else:
        print("It's a tie.")


if __name__ == '__main__':
    print("=== Naughts & Crosses ===\r\n")
    
    piece = None
    while piece not in ['o', 'x']:
        piece = input("Choose your piece: o/x ")
        
    keys = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"]]
    key_position_lookup = getPositionLookup(keys)
    
    print("Type one of the following to place at the corresponding position ('q' to quit):\r\n")
    printBoard(keys, lambda k: k)
    
    run(key_position_lookup, Player.NAUGHT if piece == 'o' else Player.CROSS)

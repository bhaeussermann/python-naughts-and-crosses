import unittest
from naughtsandcrosses.player import AiPlayer
from naughtsandcrosses.model import Player, BoardCell, CellValue, CellPosition,\
    Board

class Test(unittest.TestCase):
    def setUp(self):
        self.player = AiPlayer(Player.NAUGHT)

    def testOpenLine(self):
        self.assertTrue(self.player.isLineOpen(Player.NAUGHT, [BoardCell(CellPosition(0, 0), CellValue.NAUGHT), BoardCell(CellPosition(0, 1), CellValue.EMPTY), BoardCell(CellPosition(0, 2), CellValue.EMPTY)]))
    
    def testNotOpenLine(self):
        self.assertFalse(self.player.isLineOpen(Player.NAUGHT, [BoardCell(CellPosition(0, 0), CellValue.NAUGHT), BoardCell(CellPosition(0, 1), CellValue.CROSS), BoardCell(CellPosition(0, 2), CellValue.EMPTY)]))
    
    def testOpenSpaceCount(self):
        self.assertEqual(
            self.player.getOpenSpaceCount([BoardCell(CellPosition(0, 0), CellValue.NAUGHT), BoardCell(CellPosition(0, 1), CellValue.EMPTY), BoardCell(CellPosition(0, 2), CellValue.NAUGHT)]), 
            1)
    
    def testFinalMove(self):
        board = Board(3)
        self.setUpBoard(board, 
                        [
                            [CellValue.NAUGHT, CellValue.NAUGHT, CellValue.CROSS],
                            [CellValue.CROSS, CellValue.CROSS, CellValue.NAUGHT],
                            [CellValue.NAUGHT, CellValue.CROSS, CellValue.EMPTY]
                        ])
        self.assertEqual(self.player.getMove(board), CellPosition(2, 2))

    
    def setUpBoard(self, board, cell_values):
        for row in range(board.size):
            for column in range(board.size):
                board.grid[row][column].value = cell_values[row][column]

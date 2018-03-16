import unittest
from naughtsandcrosses.model import Board, BoardCell, CellPosition, CellValue, Winner

class BoardTest(unittest.TestCase):
    def testInitBoard(self):
        self.assertListEqual(Board(2).grid,
                             [
                                 [BoardCell(CellPosition(0, 0)), BoardCell(CellPosition(0, 1))],
                                 [BoardCell(CellPosition(1, 0)), BoardCell(CellPosition(1, 1))]
                             ])
        
    def testGetLines(self):
        self.assertCountEqual(Board(2).getLines(),
                             [
                                 [BoardCell(CellPosition(0, 0)), BoardCell(CellPosition(0, 1))],
                                 [BoardCell(CellPosition(1, 0)), BoardCell(CellPosition(1, 1))],
                                 [BoardCell(CellPosition(0, 0)), BoardCell(CellPosition(1, 0))],
                                 [BoardCell(CellPosition(0, 1)), BoardCell(CellPosition(1, 1))],
                                 [BoardCell(CellPosition(0, 0)), BoardCell(CellPosition(1, 1))],
                                 [BoardCell(CellPosition(0, 1)), BoardCell(CellPosition(1, 0))]
                             ])
        
    def testGetWinner(self):
        board = Board(3)
        self.setUpBoard(board, 
                        [
                            [CellValue.NAUGHT, CellValue.CROSS, CellValue.EMPTY],
                            [CellValue.CROSS, CellValue.CROSS, CellValue.NAUGHT],
                            [CellValue.EMPTY, CellValue.CROSS, CellValue.NAUGHT]
                        ])
        self.assertEqual(board.getWinner(), Winner.CROSS)
        
    def testGetNoWinner(self):
        board = Board(3)
        self.setUpBoard(board, 
                        [
                            [CellValue.EMPTY, CellValue.CROSS, CellValue.EMPTY],
                            [CellValue.EMPTY, CellValue.CROSS, CellValue.NAUGHT],
                            [CellValue.EMPTY, CellValue.EMPTY, CellValue.NAUGHT]
                        ])
        self.assertEqual(board.getWinner(), Winner.NONE)
    
    def testGetTie(self):
        board = Board(3)
        self.setUpBoard(board, 
                        [
                            [CellValue.CROSS, CellValue.CROSS, CellValue.NAUGHT],
                            [CellValue.NAUGHT, CellValue.CROSS, CellValue.CROSS],
                            [CellValue.CROSS, CellValue.NAUGHT, CellValue.NAUGHT]
                        ])
        self.assertEqual(board.getWinner(), Winner.TIE)
    
    
    def setUpBoard(self, board, cell_values):
        for row in range(board.size):
            for column in range(board.size):
                board.grid[row][column].value = cell_values[row][column]

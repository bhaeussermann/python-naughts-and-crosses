import unittest
from naughtsandcrosses.cli_helper import *

class Test(unittest.TestCase):
    def testGetPositionLookup(self):
        self.assertEqual(getPositionLookup([[1, 2], [3, 4]]), { 1: CellPosition(0, 0), 2: CellPosition(0, 1), 3: CellPosition(1, 0), 4: CellPosition(1, 1) })

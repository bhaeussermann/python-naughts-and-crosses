from naughtsandcrosses.model import CellPosition

def getPositionLookup(grid):
    lookup = {}
    grid_size = len(grid)
    for row in range(grid_size):
        for column in range(grid_size):
            lookup[grid[row][column]] = CellPosition(row, column)
    
    return lookup

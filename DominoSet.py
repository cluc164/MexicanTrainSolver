import random
from Tile import Tile

class DominoSet:
    def __init__(self):
        self.set = self.constructTiles()
    
    def constructTiles(self):
        tiles = []
        for i in range(0,13):
            for j in range(i,13):
                tiles.append(Tile(i,j))
        return tiles
    
    def drawRandomTile(self):
        return self.set.pop(random.randrange(0, len(self.set)))
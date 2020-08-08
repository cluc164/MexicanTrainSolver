from Tile import Tile
from copy import copy
class Player:
    def __init__(self, _hand):
        self.hand = _hand
    
    def hasStartingTile(self, startingTile):
        return startingTile in self.hand
    
    def findLongestPath(self, startingTile, printPath):
        if self.hasStartingTile(startingTile):
            if printPath == True:
                print(f'You had the double {startingTile.a.number}, placing!')
            self.hand.remove(startingTile)
        path = [startingTile]
        tilesToPick = copy(self.hand)
        longestPath = self.__longestPath(path, tilesToPick)
        for i in range(len(longestPath)-1):
            if (longestPath[i].b.number != longestPath[i+1].a.number):
                longestPath[i+1].flip()
        if (printPath):
            print(f"You placed {len(longestPath)-1} tiles")
            print(f"You have {len(self.hand)-len(longestPath)+1} tiles remaining")
            for tile in longestPath:
                print(f'[{tile}]', end=" -> \n")
        return longestPath
        
    def __longestPath(self, path, tilesToPick):
        longestPath = path
        for tile in tilesToPick:
            tileConnection = path[-1].endsMatch(tile)
            if (tileConnection):
                tileConnection[0].connected = True
                tileConnection[1].connected = True

                pathToPass = copy(path)
                pathToPass.append(tile)

                options = copy(tilesToPick)
                options.remove(tile)

                p = self.__longestPath(pathToPass, options)
                if len(p) > len(longestPath):
                    longestPath = p
                
                tileConnection[0].connected = False
                tileConnection[1].connected = False

        return longestPath

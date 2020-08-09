from Domino import Domino
from copy import copy

class Player:
    def __init__(self, _hand):
        self.hand = _hand
    
    def hasStartingDomino(self, startingDomino):
        return startingDomino in self.hand
    
    def findLongestChain(self, startingDomino, printChain):
        """
            Finds the longest chain of dominoes given a pool of potential dominoes and a starting domino
        """
        # Place the starting tile if it's in your hand
        if self.hasStartingDomino(startingDomino):
            if printChain == True:
                print(f'You had the double {startingDomino.leftEnd.number}, placing!')
            self.hand.remove(startingDomino)
        
        # Create the initial chain with the starting domino in it, and use the player's current hand
        # as the inital pool of dominoes 
        chain = [startingDomino]
        tilesToPick = copy(self.hand)

        # Find the longest chain
        longestChain = self.__longestChain(chain, tilesToPick)

        # Flip the dominoes to show the correct ends being connected
        for i in range(len(longestChain)-1):
            if (longestChain[i].rightEnd.number != longestChain[i+1].leftEnd.number):
                longestChain[i+1].flip()

        # Print the length of the chain, and the chain in order
        if (printChain):
            print(f"You placed {len(longestChain)-1} tiles")
            print(f"You have {len(self.hand)-len(longestChain)+1} tiles remaining")
            for domino in longestChain:
                print(f'[{domino}]', end=" -> \n")
        return longestChain
        
    
    def __longestChain(self, currentChain, dominoesToPick):
        """ 
            Function that iterates over an array over potential dominoes to chain together (tilesToPick)
            starting from the current path and if a single domino is able to be connected (the numbers on an end match),
            this function is called recursively with that domino added into the path and removed from the tilesToPick
        """
        # Set the longestPath we've seen to the current path, so when the recursive call returns for each iteration,
        # we can see if it was able to create a longer chain
        longestChain = currentChain
        # Iterate over each tile in the potential tile pool
        for domino in dominoesToPick:
            # Check the unconnected end of the last domino in the current chain, and if it matches the number on either 
            # end of the current tile
            tileConnection = currentChain[-1].endsMatch(domino)
            if (tileConnection):
                # Connect the tiles on the end which they connect, so we don't accidentally check them later
                tileConnection[0].connected = True
                tileConnection[1].connected = True

                # Create copies of the current chain and pool of available dominoes
                newChain = copy(currentChain)
                newDominoesToPick = copy(dominoesToPick)
                
                # Add the current domino to the new chain, and remove it from the pool of available dominoes
                newChain.append(domino)
                newDominoesToPick.remove(domino)

                # Call the longest chain function to see if there are more available connections
                chainWithNewDomino = self.__longestChain(newChain, newDominoesToPick)

                # If the chain returned from the recursive call is longer than the current longest chain, update
                # the current longest chain
                if len(chainWithNewDomino) > len(longestChain):
                    longestChain = chainWithNewDomino
                
                # Disconnect the last domino in the current chain and the current domino so new paths can 
                # be discovered in other possible chains
                tileConnection[0].connected = False
                tileConnection[1].connected = False

        return longestChain

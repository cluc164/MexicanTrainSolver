from Domino import Domino
from DominoSet import DominoSet
from Player import Player

# Number of dominoes in
DominoCount = {
    2: 16,
    3: 15,
    4: 14,
    5: 12,
    6: 11,
    7: 10,
    8: 9
}

class MexicanTrain:
    """
        Class representing a game of Mexican Train based on a number of players
    """
    def __init__(self, numPlayers):
        self.dominoes = DominoSet()
        self.players = self.generatePlayers(numPlayers)

    def generatePlayers(self, numPlayers):
        """
            Create a list of Player objects with a number of dominoes in their hand,
            the number of dominoes drawn from the domino pool is based on the number
            of Players in the game
        """
        numToDraw = DominoCount.get(numPlayers)
        players = [Player(self.drawHand(numToDraw)) for _ in range(numPlayers)]
        return players

    def drawHand(self, numToDraw):
        hand = [self.dominoes.drawRandomDomino() for _ in range(numToDraw)]
        return hand
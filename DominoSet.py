import random
from Domino import Domino

class DominoSet:
    def __init__(self):
        self.dominoes = self.constructDominoes()
    
    def constructDominoes(self):
        dominoes = []
        for i in range(0,13):
            for j in range(i,13):
                dominoes.append(Domino(i,j))
        return dominoes
    
    def drawRandomDomino(self):
        return self.dominoes.pop(random.randrange(0, len(self.dominoes)))

    def returnDomino(self, domino):
        self.dominoes.append(domino)
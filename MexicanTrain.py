from Tile import Tile
from DominoSet import DominoSet
from Player import Player
import matplotlib.pyplot as plt 

tileCount = {
    2: 16,
    3: 15,
    4: 14,
    5: 12,
    6: 11,
    7: 10,
    8: 9
}

class MexicanTrain:
    def __init__(self, numPlayers):
        self.dominoes = DominoSet()
        self.players = self.generatePlayers(numPlayers)

    def generatePlayers(self, numPlayers):
        players = []
        for _ in range(numPlayers):
            numToDraw = tileCount.get(numPlayers)
            hand = self.drawHand(numToDraw)
            players.append(Player(hand))
        return players

    def drawHand(self, numToDraw):
        hand = []
        for _ in range(numToDraw):
            hand.append(self.dominoes.drawRandomTile())
        return hand

lengths = {i: 0 for i in range(0,17)}
for i in range(0,10000):
    game = MexicanTrain(2)
    longestPath = game.players[0].findLongestPath(Tile(12,12), False)
    length = len(longestPath)
    lengths[length-1] += 1

its = lengths.items()
lengths = sorted(its)
x = []
y = []
for v in lengths:
    x.append(v[0])
    y.append(v[1])

# plotting a bar chart 
plt.bar(x, y, tick_label = x, 
        width = 0.8, color = ['red', 'green']) 
plt.show()
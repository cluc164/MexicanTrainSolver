from MexicanTrain import MexicanTrain
from Player import Player
from Tile import Tile

game = MexicanTrain(2)
player = game.players[0]

longestPath = player.findLongestPath(Tile(12,12))
print("yo")
from MexicanTrain import MexicanTrain, DominoCount
from Player import Player
from Domino import Domino
import matplotlib.pyplot as plt 
import sys

def serializeChain(chain):
    """ Serialize a chain of dominoes as a string where each domino is separated by commas, and end numbers are separated by pipes"""
    chainAsString = ''
    for domino in chain:
        chainAsString += f'{domino.a.number}|{domino.b.number},'
    return chainAsString

# Get the number of iterations (if applicable) and the starting domino number 
ITERATIONS = None
STARTING_DOMINO = 12
NUM_PLAYERS = 4

if len(sys.argv) > 1:
    if sys.argv[1].isdigit():
        ITERATIONS = int(sys.argv[1])
    if sys.argv[2].isdigit() and int(sys.argv[2]) in range(0,13):
        STARTING_DOMINO = int(sys.argv[2])

startingDomino = Domino(STARTING_DOMINO,STARTING_DOMINO)

# Run the longestChain algorithm N times if ITERATIONS is set by the command line
if (ITERATIONS != None):
    # Generate N random paths and record their lengths
    for playerNumber in range(0, 1):
        lengths = {i: 0 for i in range(0,DominoCount.get(NUM_PLAYERS)+1)}
        for i in range(0,ITERATIONS):
            game = MexicanTrain(NUM_PLAYERS)
            longestChain = game.players[0].findLongestChain(startingDomino, False)
            length = len(longestChain)
            lengths[length-1] += 1

        # Split the dictionary of lengths into two separate lists for use in graphing
        its = lengths.items()
        lengths = sorted(its)
        x = []
        y = []
        for v in lengths:
            x.append(v[0])
            y.append(v[1])

        # Plot a bar chart 
        plt.bar(x, y, tick_label = x, width = 0.8, color = ['red', 'green']) 
        plt.show()
        
        print(f'Player {playerNumber}: Generated {ITERATIONS} chain(s) starting with the domino with double {STARTING_DOMINO}')
        print("\t", y)
else:  
    game = MexicanTrain(2)
    player = game.players[0]
    longestChain = player.findLongestChain(startingDomino, False)
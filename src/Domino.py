class Domino:
    def __init__(self, left, right):
        self.leftEnd = DominoEnd(left, False)
        self.rightEnd = DominoEnd(right, False)

    def __str__(self):
        return f'{self.leftEnd.number} | {self.rightEnd.number}'

    def __eq__(self, obj):
        return ((self.leftEnd == obj.leftEnd and self.rightEnd == obj.rightEnd)
                or (self.leftEnd == obj.rightEnd and self.rightEnd == obj.leftEnd))

    def connects(self, dominoToConnect):
        return (self.leftEnd == dominoToConnect.leftEnd
                or self.leftEnd == dominoToConnect.rightEnd
                or self.rightEnd == dominoToConnect.leftEnd 
                or self.rightEnd == dominoToConnect.rightEnd)

    # TODO: This is where improvements could be made in the algorithm: intelligently check for connection
    def endsMatch(self, otherDomino): 
        """ 
            Checks whether or not the numbers on this domino's ends match the numbers on another domino's end,
            and if they do, whether or not those ends are already 'connected' to anything else
        """
        if (self.leftEnd.number == otherDomino.leftEnd.number and not self.leftEnd.connected and not otherDomino.leftEnd.connected):
            return (self.leftEnd, otherDomino.leftEnd)
        elif (self.leftEnd.number == otherDomino.rightEnd.number and not self.leftEnd.connected and not otherDomino.rightEnd.connected):
            return (self.leftEnd, otherDomino.rightEnd)
        elif (self.rightEnd.number == otherDomino.leftEnd.number and not self.rightEnd.connected and not otherDomino.leftEnd.connected):
            return (self.rightEnd, otherDomino.leftEnd)
        elif (self.rightEnd.number == otherDomino.rightEnd.number and not self.rightEnd.connected and not otherDomino.leftEnd.connected):
            return (self.rightEnd, otherDomino.rightEnd)
        return False

    def flip(self):
        num = self.leftEnd.number
        con = self.leftEnd.connected

        self.leftEnd.number = self.rightEnd.number
        self.leftEnd.connected = self.rightEnd.connected
        
        self.rightEnd.number = num
        self.rightEnd.connected = con

class DominoEnd:
    def __init__(self, number, connected):
        self.number = number
        self.connected = connected
    
    def __str__(self):
        return f'{self.number}'

    def __eq__(self, obj):
        return (self.number == obj.number) and (self.connected == obj.connected)

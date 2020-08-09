class Domino:
    def __init__(self, _a, _b):
        self.a = DominoEnd(_a, False)
        self.b = DominoEnd(_b, False)

    def __str__(self):
        return f'{self.a.number} | {self.b.number}'

    def __eq__(self, obj):
        return ((self.a == obj.a and self.b == obj.b)
                or (self.a == obj.b and self.b == obj.a))

    def connects(self, dominoToConnect):
        return (self.a == dominoToConnect.a
                or self.a == dominoToConnect.b
                or self.b == dominoToConnect.a 
                or self.b == dominoToConnect.b)

    # TODO: This is where improvements could be made in the algorithm: intelligently check for connection
    def endsMatch(self, otherDomino): 
        """ 
            Checks whether or not the numbers on this domino's ends match the numbers on another domino's end,
            and if they do, whether or not those ends are already 'connected' to anything else
        """
        if (self.a.number == otherDomino.a.number and not self.a.connected and not otherDomino.a.connected):
            return (self.a, otherDomino.a)
        elif (self.a.number == otherDomino.b.number and not self.a.connected and not otherDomino.b.connected):
            return (self.a, otherDomino.b)
        elif (self.b.number == otherDomino.a.number and not self.b.connected and not otherDomino.a.connected):
            return (self.b, otherDomino.a)
        elif (self.b.number == otherDomino.b.number and not self.b.connected and not otherDomino.a.connected):
            return (self.b, otherDomino.b)
        return False

    def flip(self):
        num = self.a.number
        con = self.a.connected

        self.a.number = self.b.number
        self.a.connected = self.b.connected
        
        self.b.number = num
        self.b.connected = con

class DominoEnd:
    def __init__(self, number, connected):
        self.number = number
        self.connected = connected
    
    def __str__(self):
        return f'{self.number}'

    def __eq__(self, obj):
        return (self.number == obj.number) and (self.connected == obj.connected)

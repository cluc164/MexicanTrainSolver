class Tile:
    def __init__(self, _a, _b):
        self.a = TileEnd(_a, False)
        self.b = TileEnd(_b, False)

    def __str__(self):
        return f'{self.a.number} | {self.b.number}'

    def __eq__(self, obj):
        return ((self.a == obj.a and self.b == obj.b)
                or (self.a == obj.b and self.b == obj.a))

    def connects(self, tileToConnect):
        return (self.a == tileToConnect.a
                or self.a == tileToConnect.b
                or self.b == tileToConnect.a 
                or self.b == tileToConnect.b)

    def endsMatch(self, tile): 
        if (self.a.number == tile.a.number and not self.a.connected and not tile.a.connected):
            return (self.a, tile.a)
        elif (self.a.number == tile.b.number and not self.a.connected and not tile.b.connected):
            return (self.a, tile.b)
        elif (self.b.number == tile.a.number and not self.b.connected and not tile.a.connected):
            return (self.b, tile.a)
        elif (self.b.number == tile.b.number and not self.b.connected and not tile.a.connected):
            return (self.b, tile.b)
        return False

    def flip(self):
        num = self.a.number
        con = self.a.connected

        self.a.number = self.b.number
        self.a.connected = self.b.connected
        
        self.b.number = num
        self.b.connected = con

class TileEnd:
    def __init__(self, number, connected):
        self.number = number
        self.connected = connected
    
    def __str__(self):
        return f'{self.number}'

    def __eq__(self, obj):
        return (self.number == obj.number) and (self.connected == obj.connected)

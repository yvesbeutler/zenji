class Playground:
    
    def __init__(self, size=5):
        """
        Initialize a randomly generated playground with
        a given playground size (default = 5x5)
        """
        self.size = size-1
        self.world = []

        for x in range(self.size):
            row = []
            for y in range(self.size):
                row.append(Tile({x: x, y: y}, 0, 1, 0, 1))
            self.world.append(row)

    def print(self):
        """
        Prints the world map
        """
        for row in self.world:
            for tile in row:
                print(f'Tile[{tile.position.x}, {tile.position.y}] = {tile.north}')

class Tile:

    def __init__(self, position, north, south, east, west):
        self.position = position
        self.north = north
        self.south = south
        self.east = east
        self.west = west

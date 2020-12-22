import collections
import math

Rotation = collections.namedtuple('Rotation', 'tile top bottom left right')

def rotate(tile):
    size = len(tile[0])
    newTile = []
    for y in range(size):
        line = ''
        for x in range(size):
            line += tile[x][size-1-y]
        newTile.append(line)
    return newTile

def flip(tile):
    return list(map(lambda x: x[::-1], tile))

class Tile():
    def __init__(self, tile):
        size = len(tile[0])
        self.rotations = []
        for _ in range(2):
            for _ in range(4):
                top = tile[0]
                bottom = tile[size-1]
                left = ''.join([t[0] for t in tile])
                right = ''.join([t[size-1] for t in tile])
                self.rotations.append(Rotation(tile, top, bottom, left, right))
                tile = rotate(tile)
            tile = flip(tile)

class Tiles():
    def __init__(self, filename):
        self.tiles = {}
        self.num = 0
        with open('20/' + filename) as f:
            lines = list(map(lambda x: x.strip(), f.readlines()))
        self.size = len(lines[1])
        i = 0
        while i < len(lines):
            id = int(lines[i][5:-1])
            self.tiles[id] = Tile(lines[i+1:i+1+self.size])
            self.num += 1
            i+= self.size + 2

Coord = collections.namedtuple('Coord', 'x y')

def diagonal(size):
    x = 0
    y = 0
    num = size**2
    while num > 0:
        if 0 <= x and x < size and 0 <= y and y < size:
            yield Coord(x,y)
            num -= 1
        x += 1
        y -= 1
        if y < 0:
            y = x
            x = 0

Placement = collections.namedtuple('Placement', 'tileId rotationNum')

class Jigsaw():
    def __init__(self, tiles):
        self.tiles = tiles
        # self.numTiles = tiles.num
        self.size = int(math.sqrt(tiles.num))

        self.order = list(diagonal(self.size))

    def aligned(self, grid, i, tileId, rotationNum):
        tileCoord = self.order[i]
        if tileCoord.x == 0 and tileCoord.y == 0:
            return True
        if tileCoord.x > 0: # there's a tile on the left
            compareTileCoord = Coord(tileCoord.x-1, tileCoord.y)
            compareTileOrder = self.order.index(compareTileCoord)
            compareTile = grid[compareTileOrder]
            if self.tiles.tiles[compareTile.tileId].rotations[compareTile.rotationNum].right != self.tiles.tiles[tileId].rotations[rotationNum].left:
                return False
        if tileCoord.y > 0: # there's a tile above
            compareTileCoord = Coord(tileCoord.x, tileCoord.y-1)
            compareTileOrder = self.order.index(compareTileCoord)
            compareTile = grid[compareTileOrder]
            if self.tiles.tiles[compareTile.tileId].rotations[compareTile.rotationNum].bottom != self.tiles.tiles[tileId].rotations[rotationNum].top:
                return False
        return True

    def search(self, i, grid, tilesRemaining):
        if tilesRemaining == []:
            # Display image
            for tiley in range(self.size):
                for j in range(1,9):
                    for tilex in range(self.size):
                        placement = grid[self.order.index(Coord(tilex,tiley))]
                        tile = self.tiles.tiles[placement.tileId]
                        rotation = tile.rotations[placement.rotationNum]
                        tile = rotation.tile
                        for i in range(1,9):
                            print(tile[j][i], end = '')
                    print()
            print()
            return
        else:
            for tileId in tilesRemaining:
                for rotationNum in range(8):
                    if self.aligned(grid, i, tileId, rotationNum):
                        newTilesRemaining = tilesRemaining.copy()
                        newTilesRemaining.remove(tileId)
                        self.search(i+1, grid + [Placement(tileId, rotationNum)], newTilesRemaining)

    def solve(self):
        self.grid = []
        tilesRemaining = list(self.tiles.tiles.keys())

        self.search(0, [], tilesRemaining)

tiles = Tiles('input.txt')
jigsaw = Jigsaw(tiles)
jigsaw.solve()
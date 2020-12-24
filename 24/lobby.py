import re
import collections

def neighbours(loc):
    return[(loc[0]+i,loc[1]+j) for i,j in [(1,0),(-1,0),(0,1),(0,-1),(1,-1),(-1,1)]]

class Floor():
    def __init__(self):
        self.tiles = collections.defaultdict(bool)

    def execute(self, i):
        for instruction in i.instructions:
            loc = location(instruction)
            self.tiles[loc] = not(self.tiles[loc])        

    def countBlack(self, locations):
        return len(list(filter(lambda k: self.tiles[k], locations)))

    def count(self):
        return self.countBlack(self.tiles.keys())

    def flip(self):
        newTiles = self.tiles.copy()

        scope = set([n for k in self.tiles.keys() if self.tiles[k] for n in neighbours(k) + [k]])

        for loc in scope:
            if self.tiles[loc]: # Black
                if self.countBlack(neighbours(loc)) not in [1,2]:
                    del newTiles[loc]
            else: # White
                if self.countBlack(neighbours(loc)) == 2:
                    newTiles[loc] = True

        self.tiles = newTiles                

    def iterate(self, n):
        for _ in range(n):
            self.flip()
        return self.count()

class Instructions():
    def __init__(self, filename):
        c = re.compile('(e|se|sw|w|nw|ne)')
        with open('24/' + filename) as f:
            self.instructions = list(map(lambda x: c.findall(x.strip()), f.readlines()))

def location(path):
    x = 0
    y = 0
    for d in path:
        if d == 'e':
            x += 1
        elif d == 'w':
            x -= 1
        elif d == 'ne':
            y += 1
        elif d == 'nw':
            x -= 1
            y += 1
        elif d == 'se':
            x += 1
            y -= 1
        elif d == 'sw':
            y -= 1
        else:
            raise Exception('Unknown direction: ' + d)
    return (x,y)
            
i = Instructions('test.txt')
f = Floor()
f.execute(i)
assert f.count() == 10
assert f.iterate(100) == 2208

i = Instructions('input.txt')
f = Floor()
f.execute(i)
print(f.count())
print(f.iterate(100))
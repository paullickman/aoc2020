import copy

class Seats():
    def __init__(self, filename):
        with open('11/' + filename) as f:
            self.masterLayout = list(map(lambda x: list(x.strip()), f.readlines()))
        self.height = len(self.masterLayout)
        self.width = len(self.masterLayout[0])

    def numNeighbours(self, x, y, extended):
        num = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if not (i==0 and j==0):
                    u = x
                    v = y
                    loop = True
                    while loop:
                        u += i
                        v += j
                        onboard = u >= 0 and u < self.width and v >=0 and v < self.height
                        if onboard and self.layout[v][u] == '#':
                            num += 1
                        loop = extended and onboard and self.layout[v][u] == '.'
        return num

    def iterate(self, extended):
        changed = False
        newLayout = copy.deepcopy(self.layout)
        neighbourLimit = 4 if not(extended) else 5
        for y in range(self.height):
            for x in range(self.width):
                if self.layout[y][x] == 'L' and self.numNeighbours(x, y, extended) == 0:
                    newLayout[y][x] = '#'
                    changed = True
                elif self.layout[y][x] == '#' and self.numNeighbours(x, y, extended) >= neighbourLimit:
                    newLayout[y][x] = 'L'
                    changed = True
        self.layout = newLayout
        return changed

    def count(self):
        return sum(c == '#' for row in self.layout for c in row)

    def numOccupied(self, extended = False):
        self.layout = copy.deepcopy(self.masterLayout)
        while self.iterate(extended):
            pass
        return self.count()

s = Seats('test.txt')
assert s.numOccupied() == 37
assert s.numOccupied(True) == 26

s = Seats('input.txt')
print(s.numOccupied())
print(s.numOccupied(True))
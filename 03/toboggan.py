import math

class Map():

    def __init__(self, filename):
        with open('03/' + filename) as f:
            self.map = list(map(lambda x: x.strip(), f.readlines()))
            self.height = len(self.map)
            self.width = len(self.map[0])

    def count(self, i, j):
        num = 0
        x, y = 0, 0
        while y < self.height:
            if self.map[y][x] == '#':
                num += 1
            x = (x + i) % self.width
            y += j
        return num

    def counts(self, slopes):
        return math.prod([self.count(s[0], s[1]) for s in slopes])

m = Map('test.txt')
assert(m.count(3,1) == 7)
slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
assert(m.counts(slopes) == 336)

m = Map('input.txt')
print(m.count(3,1))
print(m.counts(slopes))
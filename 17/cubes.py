import collections
import itertools

class Cubes():
    def __init__(self, filename, dimension):
        self.dimension = dimension

        self.cube = collections.defaultdict(bool)

        with open('17/' + filename) as f:
            y = 0
            for line in f.readlines():
                for x in range(len(line)):
                    if line[x] == '#':
                        self.cube[(x,y) + tuple([0] * (self.dimension - 2))] = True
                y += 1

        self.offsets = list(itertools.product([-1, 0, 1], repeat=self.dimension))
        self.offsets.remove(tuple([0] * self.dimension))

    def iterate(self):
        newCube = self.cube.copy()

        minRange = min(x for p in self.cube if self.cube[p] for x in p)
        maxRange = max(x for p in self.cube if self.cube[p] for x in p)

        for point in itertools.product(range(minRange-1, maxRange+2), repeat=self.dimension):
            if self.cube[point]:
                if not(self.numNeighbours(point) in [2,3]):
                    newCube[point] = False
            else:
                if self.numNeighbours(point) == 3:
                    newCube[point] = True
        self.cube = newCube

    def numNeighbours(self, point):
        return len(list(filter(lambda p: self.cube[p], [tuple(map(sum, zip(point, offset))) for offset in self.offsets])))

    def boot(self):
        # Iterate 6 times
        for _ in range(6):
            c.iterate()
        # Count number of active cells
        return len([p for p in self.cube.keys() if self.cube[p]])

c = Cubes('test.txt', 3)
assert c.boot() == 112

c = Cubes('test.txt', 4)
assert c.boot() == 848

c = Cubes('input.txt', 3)
print(c.boot())

c = Cubes('input.txt', 4)
print(c.boot())
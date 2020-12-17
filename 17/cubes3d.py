import collections
import copy

class Cubes():
    def __init__(self, filename):
        self.cube = collections.defaultdict(bool)
        self.xMin = 0
        self.xMax = 0
        self.yMin = 0
        self.yMax = 0
        self.zMin = 0
        self.zMax = 0

        with open('17/' + filename) as f:
            y = 0
            for line in f.readlines():
                for x in range(len(line)):
                    if line[x] == '#':
                        self.write(x,y,0)
                y += 1

    def write(self, x, y, z):
        self.cube[(x,y,z)] = True
        if x < self.xMin:
            self.xMin = x
        if x > self.xMax:
            self.xMax = x
        if y < self.yMin:
            self.yMin = y
        if y > self.yMax:
            self.yMax = y
        if z < self.zMin:
            self.zMin = z
        if z > self.zMax:
            self.zMax = z

    def iterate(self):
        newCube = copy.deepcopy(self.cube)
        newCells = []
        for x in range(self.xMin-1, self.xMax+2):
            for y in range(self.yMin-1, self.yMax+2):
                for z in range(self.zMin-1, self.zMax+2):
                    if self.cube[(x,y,z)]:
                        if not(self.numNeighbours(x,y,z) in [2,3]):
                            newCube[(x,y,z)] = False
                    else:
                        if self.numNeighbours(x,y,z) == 3:
                            newCells.append((x,y,z))
        self.cube = newCube
        for p in newCells:
            self.write(*p)

    def numNeighbours(self, x, y, z):
        num = 0
        for i in [-1, 0 , 1]:
            for j in [-1, 0 , 1]:
                for k in [-1, 0 , 1]:
                    if i!=0 or j!=0 or k!=0:
                        if self.cube[(x+i, y+j, z+k)]:
                            num += 1
        return num

    def count(self):
        return len([p for p in self.cube.keys() if self.cube[p]])

c = Cubes('test.txt')
for _ in range(6):
    c.iterate()
assert c.count() == 112

c = Cubes('input.txt')
for _ in range(6):
    c.iterate()
print(c.count())
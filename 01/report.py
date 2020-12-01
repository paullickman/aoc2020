import itertools
import math

class report():

    def __init__(self, filename):
        with open(filename) as f:
            self.nums = list(map(int,f.readlines()))

    def search(self, n):
        for c in itertools.combinations(self.nums, n):
            if sum(c) == 2020:
                return math.prod(c)

r = report('test.txt')
assert(r.search(2) == 514579)
assert(r.search(3) == 241861950)

r = report('input.txt')
print(r.search(2))
print(r.search(3))

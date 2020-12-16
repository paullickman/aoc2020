import re
import collections
import itertools
import math

Range = collections.namedtuple('Range', 'lower upper')

class Tickets():
    def __init__(self, filename):
        with open('16/' + filename) as f:
            lines = f.readlines()

        self.fields = []
        i = 0
        while len(lines[i]) > 1:
            z = re.match(r'[\w\s]+: (\d+)\-(\d+) or (\d+)\-(\d+)', lines[i])
            if z:
                g = z.groups()
                self.fields.append((Range(int(g[0]), int(g[1])), Range(int(g[2]), int(g[3]))))
            i += 1

        i += 2
        self.ticket = list(map(int, lines[i].split(',')))

        i += 3
        self.nearby = []
        while i < len(lines) and len(lines[i]) > 1:
            self.nearby.append(list(map(int, lines[i].split(','))))
            i += 1

    def possible(self, n):
        for f in self.fields:
            for r in f:
                if r.lower <= n and n <= r.upper:
                    return True
        return False

    def errorRate(self):
        return sum([n for t in self.nearby for n in t if not self.possible(n)])

    def search(self):
        valid = [self.ticket]
        for t in self.nearby:
            if all(map(self.possible, t)):
                valid.append(t)
        
        possible = []
        for f in self.fields:
            poss = []
            for i in range(len(self.ticket)):
                if all([(f[0].lower <= t[i] and t[i] <= f[0].upper) or (f[1].lower <= t[i] and t[i] <= f[1].upper) for t in valid]):
                    poss.append(i)
            possible.append(poss)

        enum = list(zip(itertools.count(0), possible))
        enumSorted = sorted(enum, key = lambda x: len(x[1]))
        self.scan(enumSorted, {})

    def scan(self, partition, solution):
        if partition == []:
            print(math.prod([self.ticket[solution[i]] for i in range(6)]))
        else:
            for n in partition[0][1]:
                r = remove(n, partition[1:])
                self.scan(r, {**solution, partition[0][0]:n})

def remove(n, partition):
    return list(map(lambda part: (part[0], list(filter(lambda i: i != n, part[1]))), partition))

t = Tickets('test.txt')
assert t.errorRate() == 71

# t = Tickets('test2.txt')
# t.search()

t = Tickets('input.txt')
print(t.errorRate())
t.search()
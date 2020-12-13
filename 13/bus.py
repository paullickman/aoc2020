import itertools

class Bus():
    def __init__(self, filename):
        with open('13/' + filename) as f:
            lines = f.readlines()
            self.arrival = int(lines[0])
            self.busesRaw = lines[1]
            self.buses = list(map(int, list(filter(lambda x: x != 'x', lines[1].split(',')))))

    def earliest(self):
        t = self.arrival
        while True:
            for b in self.buses:
                if t % b == 0:
                    return ((t - self.arrival) * b)
            t += 1

def subsequent(busList):
    buses = [(int(b),t) for b,t in zip(busList.split(','), itertools.count(0)) if b != 'x']
    # Algorithm to contruct a number such that it has expected modulus remainders for a list of numbers
    time = 0
    incr = 1
    for b, t in buses:
        while not(time % b == ((b - t) % b)):
            time += incr
        incr *= b # As this is the product of previous bus numbers, then it won't change the modulus remainders of subsequent times
    return time

b = Bus('test.txt')
assert b.earliest() == 295
assert subsequent(b.busesRaw) == 1068781
assert subsequent('17,x,13,19') == 3417
assert subsequent('67,7,59,61') == 754018
assert subsequent('67,x,7,59,61') ==  779210
assert subsequent('67,7,x,59,61') ==  1261476
assert subsequent('1789,37,47,1889') ==  1202161486

b = Bus('input.txt')
print(b.earliest())
print(subsequent(b.busesRaw))
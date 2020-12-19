import itertools
import functools

class Messages():
    def __init__(self, filename):
        with open('19/' + filename) as f:
            lines = f.readlines()
        
        # Read rules
        self.rules = {}

        # Parse lines like:
        # 1: 2 3 | 3 2

        i = 0
        while len(lines[i]) > 1:
            s = lines[i].split(':') # PRL Switch to re
            num = int(s[0])
            s = s[1].split('|')
            if s[0][1] == '\"':
                self.rules[num] = s[0][2]
            else:
                self.rules[num] = []
                for subrule in s:
                    subrule = subrule.strip().split(' ')
                    self.rules[num].append(list(map(int, subrule)))
            i += 1

        # Read received messages
        self.messages = list(map(lambda x: x.strip(), lines[i+1:]))

    @functools.lru_cache
    def valid(self, num):
        if type(self.rules[num]) == str:
            return self.rules[num]
        else:
            return [v for subrule in self.rules[num] for v in map(lambda x: ''.join(x), combinations(list(map(self.valid, subrule))))]

    def matches(self):
        return len([m for m in self.messages if m in self.valid(0)])

    def valid2(self, m):
        # Key observation is that rule 0 is some number of rule 42 followed by a fewer number of rule 31

        # Rule 42 and rule 31 consist of 8 chars so chunk up the string
        count = len(m) // 8
        words = [m[i*8:i*8+8] for i in range(count)]

        # Must start with a rule 42
        if words[0] not in self.valid(42):
            return False

        # Consume rule 42 - note no overlap with rule 31
        i = 1
        while words[i] in self.valid(42) and i < count-1:
            i += 1

        # Ensure more rule 42 than rule 31
        if i <= count-i:
            return False

        while i < count and words[i] in self.valid(31):
            i += 1

        # Ensure remaining all rule 31
        return i == count

    def matches2(self):
        return len(list(filter(self.valid2, self.messages)))

def prefix(n, c):
    return [[n] + s for s in c]

assert prefix(1,[[2],[3]]) == [[1,2],[1,3]]

def combinations(c):
    if c == []:
        return [[]]
    else:
        return [p for n in c[0] for p in prefix(n, combinations(c[1:]))]
        
assert combinations([[1,2],[3,4]]) == [[1,3],[1,4],[2,3],[2,4]]

m = Messages('test.txt')
assert m.matches() == 2

m = Messages('input.txt')
print(m.matches())
print(m.matches2())
import re
import collections

Password = collections.namedtuple('Password', 'lowest highest letter password')

def valid(p):
    n = len(re.findall(p.letter, p.password))
    return n >= p.lowest and n <= p.highest

def valid2(p):
    pos1 = p.password[p.lowest-1] == p.letter
    pos2 = p.password[p.highest-1] == p.letter
    return pos1 != pos2

class Passwords():

    def __init__(self, filename):
        with open(filename) as f:
            strip = map(lambda x: re.split('-| |: ', x.strip()), f.readlines())
        self.passwords = list(map(lambda x: Password(int(x[0]), int(x[1]), x[2], x[3]), strip))

    def numValid(self, v=valid):
        return len(list(filter(v, self.passwords)))

p = Passwords('test.txt')
assert(p.numValid() == 2)
assert(p.numValid(valid2) == 1)

p = Passwords('input.txt')
print(p.numValid())
print(p.numValid(valid2))

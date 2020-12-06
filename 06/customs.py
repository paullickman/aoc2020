def countSomeone(answer):
    return len(set([c for line in answer for c in line ]))

def countEveryone(answer):
    return len(set.intersection(*list(map(set, answer))))

class Answers():

    def __init__(self, filename):
        with open('06/' + filename) as f:
            self.answers = list(map(lambda x: x.splitlines(), f.read().split('\n\n')))
    
    def counts(self, count = countSomeone):
        return sum(map(count, self.answers))

a = Answers('test.txt')
assert a.counts() == 11
assert a.counts(countEveryone) == 6

a = Answers('input.txt')
print(a.counts())
print(a.counts(countEveryone))
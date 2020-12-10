import collections
import functools

def differences(nums):
    last = 0
    for num in nums:
        yield num - last
        last = num

class Jolt():
    def __init__(self, filename):
        with open('10/' + filename) as f:
            self.ratings = list(map(int, f.readlines()))
            self.ratings.sort()
            self.length = len(self.ratings)

    def chain(self):
        diffs = collections.Counter(differences(self.ratings))
        diffs[3] += 1
        return diffs[1] * diffs[3]

    @functools.lru_cache
    def count(self, last, i):
        if self.ratings[i] - last > 3:
            return 0
        if i == self.length - 1:
            return 1
        return self.count(self.ratings[i], i+1) + self.count(last, i+1)
                
    def numArrangements(self):
        return self.count(0, 0)

j = Jolt('test1.txt')
assert j.chain() == 7 * 5
assert j.numArrangements() == 8

j = Jolt('test2.txt')
assert j.chain() == 22 * 10
assert j.numArrangements() == 19208

j = Jolt('input.txt')
print(j.chain())
print(j.numArrangements())
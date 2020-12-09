def sums(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                yield nums[i] + nums[j]

class Encoding():
    def __init__(self, filename, preamble):
        with open('09/' + filename) as f:
            self.nums = list(map(int, f.readlines()))
            self.preamble = preamble

    def firstInvalid(self):
        i = self.preamble
        while i < len(self.nums):
            if not(self.nums[i] in sums(self.nums[i-self.preamble:i])):
                return self.nums[i]
            i += 1

    def search(self, n):
        for i in range(len(self.nums) - 2):
            for j in range(i + 1, len(self.nums)):
                if sum(self.nums[i:j+1]) == n:
                    return min(self.nums[i:j+1]) + max(self.nums[i:j+1])

e = Encoding('test.txt', 5)
assert e.firstInvalid() == 127
assert e.search(127) == 62

e = Encoding('input.txt', 25)
firstInvalid = e.firstInvalid()
print(firstInvalid)
print(e.search(firstInvalid))
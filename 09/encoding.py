def sums(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                yield nums[i] + nums[j]

class Encoding():
    def __init__(self, filename, preamble):
        with open('09/' + filename) as f:
            self.nums = list(map(int, f.readlines()))
            self.len = len(self.nums)
            self.preamble = preamble

    def firstInvalid(self):
        i = self.preamble
        while i < self.len:
            if not(self.nums[i] in sums(self.nums[i-self.preamble:i])):
                return self.nums[i]
            i += 1

    def search(self, target):
        for i in range(self.len - 2):
            sum = self.nums[i]
            j = i + 1
            while j < self.len and sum < target:
                sum += self.nums[j]
                if sum == target:
                    return min(self.nums[i:j+1]) + max(self.nums[i:j+1])
                j += 1

e = Encoding('test.txt', 5)
assert e.firstInvalid() == 127
assert e.search(127) == 62

e = Encoding('input.txt', 25)
firstInvalid = e.firstInvalid()
print(firstInvalid)
print(e.search(firstInvalid))
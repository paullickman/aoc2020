import collections

Content = collections.namedtuple('Content', 'bag number')

class Bags():

    def __init__(self, filename):
        self.bags = {}
        with open('07/' + filename) as f:
            for line in f.readlines():
                parts = line.split('contain')
                bagLine = parts[0].split(' ')
                bag = bagLine[0] + ' ' + bagLine[1]
                self.bags[bag] = []
                if parts[1][1:3] != 'no':
                    for contentLine in parts[1].split(','):
                        bagLine = contentLine.split(' ')
                        content = bagLine[2] + ' ' + bagLine[3]
                        self.bags[bag].append(Content(content, int(bagLine[1])))

    def contains(self, bagSearch, bagItem, top):
        if not(top): # Don't count a top level shiny gold bag
            if bagSearch == bagItem:
                return True
        return any(self.contains(bagSearch, content.bag, False) for content in self.bags[bagItem])

    def numContains(self, bag):
        return len(list(filter(lambda content: self.contains(bag, content, True), self.bags.keys())))

    def bagCount(self, bag):
        return 1 + sum(content.number * self.bagCount(content.bag) for content in self.bags[bag])

    def numBags(self, bag):
        return self.bagCount(bag) - 1 # bag doesn't contain itself

root = 'shiny gold'

b = Bags('test.txt')
assert b.numContains(root) == 4
assert b.numBags(root) == 32

b = Bags('test2.txt')
assert b.numBags(root) == 126

b = Bags('input.txt')
print(b.numContains(root))
print(b.numBags(root))
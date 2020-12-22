import collections

Contains = collections.namedtuple('Contains', 'ingredients allergens')

class Foods():
    def __init__(self, filename):
        self.ingredients = set()
        self.allergens  = set()
        self.contains = []
        with open('21/' + filename) as f:
            for line in f.readlines():
                s = line.split('(contains')
                ingredients = s[0].strip().split(' ')
                allergens = s[1].strip()[:-1].split(', ')
                self.contains.append(Contains(ingredients, allergens))
                self.ingredients.update(ingredients)
                self.allergens.update(allergens)

        self.possible = {}
        for i in self.ingredients:
            self.possible[i] = list(self.allergens)

    def reduce(self):
        # If a list of ingredients contains an allergen, then any other ingredient can't contain it
        for c in self.contains:
            for a in c.allergens:
                ingredients = [i for i in self.ingredients if i not in c.ingredients]
                for i in ingredients:
                    if a in self.possible[i]:
                        self.possible[i].remove(a)

        count = 0
        for i in self.ingredients:
            if self.possible[i] == []:
                for c in self.contains:
                    if i in c.ingredients:
                        count += 1
        return count

    def solve(self):
        # Remove ingredients that can't possible contain an allergen
        for k in list(self.possible.keys()):
            if self.possible[k] == []:
                del self.possible[k]
        
        # Simple recursive iteration is sufficient to solve
        solution = []
        while len(solution) < len(self.allergens):
            for i in list(self.possible.keys()):
                if len(self.possible[i]) == 1:
                    solution.append((i, self.possible[i][0]))
                    for otheri in list(self.possible.keys()):
                        if otheri != i:
                            if self.possible[i][0] in self.possible[otheri]:
                                self.possible[otheri].remove(self.possible[i][0])
                    del self.possible[i]
        solution.sort(key = lambda x: x[1])

        return ','.join(list(map(lambda x: x[0], solution)))

f = Foods('test.txt')
assert f.reduce() == 5
assert f.solve() == 'mxmxvkd,sqjhc,fvjkl'

f = Foods('input.txt')
print(f.reduce())
print(f.solve())
def calc(chars, region):
    num = 0
    for c in chars:
        region //= 2
        if c in ['B', 'R']:
            num += region
    return num

class Pass():

    def __init__(self, code):
        self.row = calc(code[:7], 128)
        self.column = calc(code[7:], 8)
        self.id = self.row * 8 + self.column

p = Pass('FBFBBFFRLR')
assert((p.row, p.column, p.id) == (44, 5, 357))
p = Pass('BFFFBBFRRR')
assert((p.row, p.column, p.id) == (70, 7, 567))
p = Pass('FFFBBBFRRR')
assert((p.row, p.column, p.id) == (14, 7, 119))
p = Pass('BBFFBBFRLL')
assert((p.row, p.column, p.id) == (102, 4, 820))

with open('05/input.txt') as f:
    ids = [Pass(chars).id for chars in f.readlines()]

print(max(ids))
print([x for x in range(127*8+8) if x not in ids and x-1 in ids and x+1 in ids][0])

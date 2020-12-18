import re

def calc(expr, advanced=False):
    return evaluate(re.findall(r'\d+|\+|\*|\(|\)', expr), advanced)

def evaluate(s, advanced):
    # Remove brackets
    while '(' in s:
        pos = s.index('(')
        i = pos
        depth = 1
        while depth > 0:
            i += 1
            if s[i] == '(':
                depth += 1
            elif s[i] == ')':
                depth -= 1
        c = evaluate(s[pos+1:i], advanced)
        s = s[:pos] + [str(c)] + s[i+1:]

    # Prioritise addition if doing advanced math
    if advanced:
        while '+' in s:
            pos = s.index('+')
            s = s[:pos-1] + [str(int(s[pos-1]) + int(s[pos+1]))] + s[pos+2:]

    # Left to right evaluation
    result = int(s[0])
    i = 2
    while i < len(s):
        if s[i-1] == '+':
            result += int(s[i])
        else:
            result *= int(s[i])
        i += 2

    return result

assert calc('1 + 2 * 3 + 4 * 5 + 6') == 71
assert calc('1 + (2 * 3) + (4 * (5 + 6))') == 51
assert calc('2 * 3 + (4 * 5)') == 26
assert calc('5 + (8 * 3 + 9 + 3 * 4 * 3)') == 437
assert calc('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))') == 12240
assert calc('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2') == 13632

assert calc('1 + 2 * 3 + 4 * 5 + 6', True) == 231
assert calc('1 + (2 * 3) + (4 * (5 + 6))', True) == 51
assert calc('2 * 3 + (4 * 5)', True) == 46
assert calc('5 + (8 * 3 + 9 + 3 * 4 * 3)', True) == 1445
assert calc('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', True) == 669060
assert calc('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', True) == 23340

with open('18/input.txt') as f:
    lines = f.readlines()

print(sum(map(calc, lines)))
print(sum(map(lambda x: calc(x, True), lines)))
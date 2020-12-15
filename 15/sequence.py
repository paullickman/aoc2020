import itertools

def sequence(initial):
    last = {}
    inits = list(map(int, initial.split(',')))
    turn = 1
    nextN = None
    while True:
        if inits != []:
            n = inits[0]
            inits = inits[1:]
        else:
            n = nextN
        yield n
        if n not in last.keys():
            last[n] = turn
            nextN = 0
        else:
            nextN = turn - last[n]
            last[n] = turn
        turn += 1

def pos(initial, p):
    return next(itertools.islice(sequence(initial), p-1, None))

assert pos('0,3,6', 2020) == 436
assert pos('1,3,2', 2020) ==  1
assert pos('2,1,3', 2020) ==  10
assert pos('1,2,3', 2020) ==  27
assert pos('2,3,1', 2020) ==  78
assert pos('3,2,1', 2020) ==  438
assert pos('3,1,2', 2020) == 1836

print(pos('16,1,0,18,12,14,19', 2020))

assert pos('0,3,6', 30000000) == 175594
assert pos('1,3,2', 30000000) ==  2578
assert pos('2,1,3', 30000000) ==  3544142
assert pos('1,2,3', 30000000) ==  261214
assert pos('2,3,1', 30000000) ==  6895259
assert pos('3,2,1', 30000000) ==  18
assert pos('3,1,2', 30000000) == 362

print(pos('16,1,0,18,12,14,19', 30000000))
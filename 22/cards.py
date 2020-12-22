import itertools
import operator
import copy

class Deck():
    def __init__(self, filename):
        self.players = {1: [], 2: []}
        with open('22/' + filename) as f:
            for line in f.readlines():
                line = line.strip()
                if line[0:6] == 'Player':
                    playerNo = int(line[7])
                elif line.isdigit():
                    self.players[playerNo] = [int(line)] + self.players[playerNo]

    def play(self):
        cards = copy.deepcopy(self.players)
        while len(cards[1]) > 0 and len(cards[2]) > 0:
            num1 = cards[1].pop()
            num2 = cards[2].pop()
            if num1 > num2:
                cards[1] = [num1] + cards[1]
                cards[1] = [num2] + cards[1]
            else:            
                cards[2] = [num2] + cards[2]
                cards[2] = [num1] + cards[2]

        if len(cards[1]) > 0:
            winner = 1
        else:
            winner = 2
            
        return sum(itertools.starmap(operator.mul, zip(cards[winner], itertools.count(1))))

    def play2(self, c1, c2):
        cards1 = list(c1)
        cards2 = list(c2)
        seenBefore = []
        while len(cards1) > 0 and len(cards2) > 0:
            if (cards1, cards2) in seenBefore:
                return (1, cards1, cards2) # Player 1 wins if position repeats
            seenBefore.append((cards1[:], cards2[:]))
            
            num1 = cards1.pop()
            num2 = cards2.pop()

            # Check if both players have at least as many cards remaining in their deck as the value of the card
            if num1 <= len(cards1) and num2 <= len(cards2): 
                winner, _, _ = self.play2(cards1[-num1:], cards2[-num2:])
            else:
                if num1 > num2:
                    winner = 1
                else:
                    winner = 2

            if winner == 1:
                cards1 = [num2, num1] + cards1
            else:            
                cards2 = [num1, num2] + cards2

        if len(cards1) == 0:
            return (2, cards1, cards2)
        else:
            return (1, cards1, cards2)

    def recurse(self):
        cards = {}
        winner, cards[1], cards[2] = self.play2(self.players[1], self.players[2])

        return sum(itertools.starmap(operator.mul, zip(cards[winner], itertools.count(1))))

d = Deck('test.txt')
assert d.play() == 306
assert d.recurse() == 291

d = Deck('test_infinite.txt')
# Checks non-infinite loop
_ = d.recurse()

d = Deck('input.txt')
print(d.play())        
print(d.recurse())            
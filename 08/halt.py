import collections

Instruction = collections.namedtuple('Instruction', 'operation argument')
Result = collections.namedtuple('Result', 'value halted')

class Program():
    def __init__(self, filename):
        self.program = []
        with open('08/' + filename) as f:
            for line in f.readlines():
                parse = line.split(' ')
                self.program.append(Instruction(parse[0], int(parse[1])))
        self.length = len(self.program)

    def run(self):
        acc = 0
        ip = 0
        before = [False] * self.length
        while ip < self.length and not(before[ip]):
            before[ip] = True
            op = self.program[ip].operation
            arg = self.program[ip].argument
            if op == 'acc':
                acc += arg
                ip += 1
            elif op == 'jmp':
                ip += arg
            elif op == 'nop':
                ip += 1
            else:
                raise Exception("Unknown operand: " + op)
        return Result(acc, ip == self.length)

    def search(self):
        swaps = {'jmp': 'nop', 'nop': 'jmp'}
        for i in range(self.length):
            op = self.program[i].operation
            arg = self.program[i].argument
            if op in swaps.keys():
                self.program[i] = Instruction(swaps[op], arg)
                result = self.run()
                if result.halted:
                    return result.value
                self.program[i] = Instruction(op, arg)

h = Program('test.txt')
assert h.run().value == 5
assert h.search() == 8

h = Program('input.txt')
print(h.run().value)
print(h.search())
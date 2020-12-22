import re
import collections

Command = collections.namedtuple('Command', 'mask memory value')

class Data():
    def __init__(self, filename):
        self.program = []
        with open('14/' + filename) as f:
            for line in f.readlines():
                z = re.match(r'mask = (\w+)|mem\[(\w+)\] = (\w+)', line)
                if z:
                    self.program.append(Command(*z.groups()))
                    
    def exec(self):
        self.memory = {}
        for command in self.program:
            if command.mask != None:
                andMask = int(command.mask.replace('X', '1'), 2)
                orMask  = int(command.mask.replace('X', '0'), 2)
            else:
                self.memory[int(command.memory)] = int(command.value) & andMask | orMask

    def store(self, mask, addressStr, address, value):
        if mask == "":
            self.memory[address] = value
        else:
            if mask[0] == '0':
                self.store(mask[1:], addressStr[1:], address*2+int(addressStr[0]), value)
            elif mask[0] == '1':
                self.store(mask[1:], addressStr[1:], address*2+1, value)
            elif mask[0] == 'X':
                self.store(mask[1:], addressStr[1:], address*2, value)
                self.store(mask[1:], addressStr[1:], address*2+1, value)
            else:
                raise Exception('Unknown mask char: ' + mask[0])

    def exec2(self):
        self.memory = {}
        for command in self.program:
            if command.mask != None:
                mask = command.mask
            else:
                address = ('0'*36 + bin(int(command.memory))[2:])[-36:]
                self.store(mask, address, 0, int(command.value))

    def sum(self):
        return sum(self.memory.values())

d = Data('test.txt')
d.exec()
assert d.sum() == 165
d = Data('test2.txt')
d.exec2()
assert d.sum() == 208

d = Data('input.txt')
d.exec()
print(d.sum())
d.exec2()
print(d.sum())
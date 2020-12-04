def validPair(key, value):
    if key == 'byr':
        return len(value) == 4 and int(value) >= 1920 and int(value) <= 2002
    elif key == 'iyr':
        return len(value) == 4 and int(value) >= 2010 and int(value) <= 2020
    elif key == 'eyr':
        return len(value) == 4 and int(value) >= 2020 and int(value) <= 2030
    elif key == 'hgt':
        if len(value) <= 2:
            return False
        unit = value[-2:]
        height = int(value[:-2])
        return (unit == 'cm' and height >= 150 and height <= 193) or (unit == 'in' and height >= 59 and height <= 76)
    elif key == 'hcl':
        if len(value) != 7:
            return False
        if value[0] != '#':
            return False
        return all((c >= '0' and c <= '9') or (c >= 'a' and c <= 'f') for c in value[1:])
    elif key == 'ecl':
        return value in "amb blu brn gry grn hzl oth".split(' ')
    elif key == 'pid':
        if len(value) != 9:
            return False
        return all(c >= '0' and c <= '9' for c in value)
    elif key == 'cid':
        return True

assert(validPair('byr', '2002') == True)
assert(validPair('byr', '2003') == False)
assert(validPair('hgt', '60in') == True)
assert(validPair('hgt', '190cm') == True)
assert(validPair('hgt', '190in') == False)
assert(validPair('hgt', '190') == False)
assert(validPair('hcl', '#123abc') == True)
assert(validPair('hcl', '#123abz') == False)
assert(validPair('hcl', '123abc') == False)
assert(validPair('ecl', 'brn') == True)
assert(validPair('ecl', 'wat') == False)
assert(validPair('pid', '000000001') == True)
assert(validPair('pid', '0123456789') == False)

class Passport():

    def __init__(self, filename):
        self.passports = []
        passport = {}
        with open('04/' + filename) as f:
            for line in f.readlines():
                line = line.strip()
                if line == '':
                    self.passports.append(passport)
                    passport = {}
                else:
                    fields = line.split(' ')
                    for pair in fields:
                        pair = pair.split(':')
                        key = pair[0]
                        value = pair[1]
                        passport[key] = value
            self.passports.append(passport)

    def valid(self, passport, strict):
        # Check mandatory fields present
        if any(not(m in passport.keys()) for m in ['byr','iyr','eyr','hgt','hcl','ecl','pid']):
            return False
        if not(strict):
            return True
        return all(validPair(k, passport[k]) for k in passport.keys())

    def numValid(self, strict = False):
        return len(list(filter(lambda x: self.valid(x, strict), self.passports)))

p = Passport('test.txt')
assert((p.numValid() == 2))

p = Passport('invalid.txt')
assert((p.numValid(True) == 0))

p = Passport('valid.txt')
assert((p.numValid(True) == 4))

p = Passport('input.txt')
print(p.numValid())
print(p.numValid(True))
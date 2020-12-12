import collections

Instruction = collections.namedtuple('Instruction', 'action value')

class Route():
    def __init__(self, filename):
        with open('12/' + filename) as f:
            self.route = [Instruction(line[0], int(line[1:])) for line in f.readlines()]

class Ship():
    def __init__(self):
        self.x, self.y = 0, 0
        self.dx, self.dy = 1, 0 # facing east

    def distance(self):
        return abs(self.x) + abs(self.y)

    def process(self, instr):
        if instr.action == 'N':
            self.y -= instr.value
        elif instr.action == 'S':
            self.y += instr.value
        elif instr.action == 'E':
            self.x += instr.value
        elif instr.action == 'W':
            self.x -= instr.value
        elif instr.action == 'F':
            self.x += self.dx * instr.value
            self.y += self.dy * instr.value
        elif instr.action in ['L', 'R']:
            if instr.action == 'L':
                value = instr.value
            else:
                value = 360 - instr.value # convert right to left
            while value > 0:
                self.dx, self.dy = self.dy, -self.dx # turn left 90 degrees
                value -= 90
        else:
            raise Exception('Unknown action: ' +  instr.action)

    def sail(self, route):
        for instr in route:
            self.process(instr)
        return
    
class ShipWaypoint():
    def __init__(self):
        self.shipx, self.shipy = 0, 0
        self.waypointx, self.waypointy = 10, -1
    
    def distance(self):
        return abs(self.shipx) + abs(self.shipy) # dupe?

    def process(self, instr):
        if instr.action == 'N':
            self.waypointy -= instr.value
        elif instr.action == 'S':
            self.waypointy += instr.value
        elif instr.action == 'E':
            self.waypointx += instr.value
        elif instr.action == 'W':
            self.waypointx -= instr.value
        elif instr.action == 'F':
            self.shipx += self.waypointx * instr.value
            self.shipy += self.waypointy * instr.value
        elif instr.action in ['L', 'R']:
            if instr.action == 'L':
                value = instr.value
            else:
                value = 360 - instr.value # convert right to left
            while value > 0:
                self.waypointx, self.waypointy = self.waypointy, -self.waypointx # turn left 90 degrees
                value -= 90
        else:
            raise Exception('Unknown action: ' +  instr.action)

    def sail(self, route): # dupe
        for instr in route:
            self.process(instr)
            # print(self.shipx, self.shipy, self.waypointx, self.waypointy)
        return

s = Ship()
r = Route('test.txt')
s.sail(r.route)
assert s.distance() == 25

s = ShipWaypoint()
s.sail(r.route)
assert s.distance() == 286

s = Ship()
r = Route('input.txt')
s.sail(r.route)
print(s.distance())

s = ShipWaypoint()
s.sail(r.route)
print(s.distance())
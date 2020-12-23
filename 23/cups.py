# Part 1

def move(nums):
    current = nums[0]
    search = current-1
    destination = None
    while destination == None:
        if search in nums[4:]:
            destination = nums.index(search)
        else:
            search -= 1
            if search < min(nums[4:]):
                search = max(nums[4:])
    return nums[4:destination+1] + nums[1:4] + nums[destination+1:] + [nums[0]]        

def iterate(nums, n):
    for _ in range(n):
        nums = move(nums)

    i = nums.index(1)
    return ''.join(map(str, nums[i+1:] + nums[:i]))

test = '389125467'
nums = list(map(int, test))
assert iterate(nums, 10) == '92658374'
assert iterate(nums, 100) == '67384529'

puzzle = '135468729'
nums = list(map(int, puzzle))
print(iterate(nums, 100))

# Part 2

class Node:
    def __init__(self, data):
        self.item = data
        self.nxt = None

class DoublyLinkedLoop:
    def __init__(self):
        self.start_node = None

    def insert(self, data):
        global nodes
        if self.start_node is None:
            new_node = Node(data)
            new_node.nxt = new_node
            self.start_node = new_node
            self.insert_point = new_node
            nodes[data] = new_node
            return
        new_node = Node(data)
        previous_insert_point_nxt = self.insert_point.nxt
        self.insert_point.nxt = new_node
        new_node.nxt = previous_insert_point_nxt
        self.insert_point = new_node

        nodes[data] = new_node

def move2():
    global d
    
    current_node = d.start_node
    current = current_node.item

    # Obtain the trio to pick up
    trio_start = current_node.nxt
    n = trio_start
    trio = []
    for _ in range(3):
        trio.append(n.item)
        trio_end = n
        n = n.nxt
    first_node_after_trio = n

    # Calculate the value to search for
    search = current-1
    if search == 0:
        search = totalNum
    while search in trio:
        search -= 1
        if search == 0:
            search = totalNum
    
    # Find destination
    destination_node = nodes[search]
    next_node_after_destination = destination_node.nxt

    # Insert trio at the destination node
    destination_node.nxt = trio_start
    trio_end.nxt = next_node_after_destination
    current_node.nxt = first_node_after_trio

    # Move on current node by one
    d.start_node = d.start_node.nxt
    d.insert_point = d.insert_point.nxt

def iterate2(text):
    global d, nodes

    # Set-up cards
    nodes = [None] * (totalNum+1)
    d = DoublyLinkedLoop()
    for n in list(map(int, text)) + list(range(10, totalNum+1)):
        d.insert(n)

    # Make moves
    for _ in range(totalIterations):
        move2()
        # d.print()

    # Calculate return number
    node1 = nodes[1].nxt
    node2 = node1.nxt
    return node1.item * node2.item

totalNum = 1000000
totalIterations = 10000000

assert iterate2('389125467') == 149245887792

print(iterate2('135468729'))
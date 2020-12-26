def calc_loop(key):
    n = 1
    subject = 7
    loop = 0
    while n != key:
        loop += 1
        n = (n * subject) % 20201227
    return loop

def calc_key(subject, loop):
    n = 1
    for _ in range(loop):
        n = (n * subject) % 20201227
    return n        

# Test

card_public_key = 5764801
card_loop_size = calc_loop(card_public_key)
assert card_loop_size == 8

door_public_key = 17807724
door_loop_size = calc_loop(door_public_key)
assert door_loop_size == 11

encryption_key = calc_key(card_public_key, door_loop_size)
assert encryption_key == 14897079
assert calc_key(door_public_key, card_loop_size) == encryption_key

# Input

card_public_key = 18356117
door_public_key = 5909654
card_loop_size = calc_loop(card_public_key)
door_loop_size = calc_loop(door_public_key)

print(encryption_key := calc_key(card_public_key, door_loop_size))
assert calc_key(door_public_key, card_loop_size) == encryption_key

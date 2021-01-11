import time

number = 0

target_tick = time.time() + 5
while time.time() < target_tick:
    number += 1

print("{} repetition during 5 seconds".format(number))
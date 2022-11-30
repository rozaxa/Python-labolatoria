import itertools
from itertools import cycle, repeat
import random

# A)
iter_cycle = cycle(['0', '1'])
while True:
    print(next(iter_cycle), end = " ")


# B)
mylist = ["N", "E", "S", "W"]
while True:
    print(random.choice(mylist), end=" ")

# C)
days = repeat('0,1,2,3,4,5,6')
while True:
    print(next(days))



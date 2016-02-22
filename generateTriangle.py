__author__ = 'Kelvin'

import random
import sys


NUM_OF_LEVELS = 20

with open('triangle.txt', 'w+') as f:
    for x in range(1, NUM_OF_LEVELS+1):
        for y in range(0, x):
            f.write('%02d' % (random.randint(1, 99)))
            if y+1 != x:
                f.write(" ")
        if x != NUM_OF_LEVELS:
            f.write("\n")
__author__ = 'lassevk'

import time
import sys

sys.setrecursionlimit(25000)

lines = []
for line in open("triangle100.txt").read().strip().split('\n'):
    lines.append(map(int, line.split(" ")))

def test(line, index):
    global cache
    if line > len(lines)-1:
        return 0
    key = str(line) + "|" + str(index)
    if not key in cache:
        cache[key] = lines[line][index] + max(test(line+1, index), test(line+1, index+1))
    return cache[key]

time_start = time.time()
cache = {}
print("highest path sum", test(0, 0))
time_end = time.time()
print("time taken", time_end-time_start)
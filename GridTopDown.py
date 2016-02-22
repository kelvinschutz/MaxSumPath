__author__ = 'cuongptnk'

import sys
import time

sys.setrecursionlimit(25000)

triangle = [[] for x in range(100)]
num_of_row = 0
with open("triangle100.txt", "r") as ins:
    for line in ins:
        for n in line.strip().split():
            triangle[num_of_row].append(int(n))
        num_of_row += 1
grid = [[-1 for x in range(num_of_row)] for x in range(num_of_row)]

# Since triangle is symmetric, root of the triangle can be used as an ID for the triangle
#a is the row index, b is the column index of the root of the triangle
def Sum_Max_Path(a, b):
    #base condition
    if a == num_of_row - 1:  #last row
        grid[a][b] = triangle[a][b]
        return triangle[a][b]
    #compare results between sub triangles in the left and right
    #left sub triangle : root at (a+1,b)
    if grid[a + 1][b] == -1:
        grid[a + 1][b] = Sum_Max_Path(a + 1, b)
    #right sub triangle : root at (a+1,b+1)
    if grid[a + 1][b + 1] == -1:
        grid[a + 1][b + 1] = Sum_Max_Path(a + 1, b + 1)
    #now compare
    if grid[a + 1][b] > grid[a + 1][b + 1]:
        return triangle[a][b] + grid[a + 1][b]
    else:
        return triangle[a][b] + grid[a + 1][b + 1]

time_start = time.time()
print(Sum_Max_Path(0, 0))
time_end = time.time()
print("time taken", time_end-time_start)
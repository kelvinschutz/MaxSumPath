__author__ = 'Kelvin'


import math
import time

#Returns the index of the left child of an element
def getLeftChild(index, level):
    return (index + level)

#Returns the index of the right child of an element
def getRightChild(index, level):
    return (index + level + 1)

#Opens and reads in a file into a list of integers
#The list will be stored in pathTree
def openFile(infile, tree):
    with open(infile, 'r') as f:
        read_data = f.read()

    #Split the string up into individual elements
    tree = read_data.split()

    #Convert each of the string elements into integers
    for x in range(len(tree)):
        tree[x] = int(tree[x])

    return tree

def makeRoutes(list):
    for x in range(2 ** (numOfLevels - 1)):
        string = bin(x)[2:]
        string = string.zfill(numOfLevels - 1)
        list.append(string)

def findMaxSum():
    maxSum = 0
    for x in routes:
        currentNode = 0
        currentSum = pathTree[currentNode]
        levelCounter = 1
        for y in x:
            if y == '0':
                currentNode = getLeftChild(currentNode, levelCounter)
            if y == '1':
                currentNode = getRightChild(currentNode, levelCounter)
            currentSum += pathTree[currentNode]
            levelCounter += 1
        if maxSum < currentSum:
            maxSum = currentSum
    print(maxSum)


#MAIN


pathTree = []
pathTree = openFile('triangle20.txt', pathTree)
numOfLevels = int(math.floor(math.sqrt(len(pathTree)*2)))
routes = []
makeRoutes(routes)
numberOfRoutes = len(routes)
time_start = time.time()
findMaxSum()
time_end = time.time()
print("time taken", time_end-time_start)


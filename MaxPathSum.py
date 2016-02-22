__author__ = 'Kelvin'

import time

#Returns the index of the left child of an element
def getLeftChild(index, level):
    return (index + level)

#Returns the index of the right child of an element
def getRightChild(index, level):
    return (index + level + 1)

#Returns the index of the first element of a given level
def getFirstElement(level):
    return int((level*(level-1))/2)

#Returns the index of the last element of a given level
def getLastElement(level):
    return int(getFirstElement(level)+level-1)

#Returns the number of levels in the pathTree
#If the file is of a bad format, will return -1
def initNumOfLevels(tree):
    elements_left = len(tree)
    #print("elements_left: ", elements_left)
    i = 1
    while elements_left > 0:
        elements_left -= i
        i += 1
    if(elements_left < 0):
        print("Bad File Format!")
        i = 0
    #print("Number of Levels: ", i-1)
    return i-1

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

#Prints a formatted version of the pathTree
def printTree(tree):
    #For each level, print all elements at that level
    for x in range(1,numOfLevels+1):
        print("Level ", x, ":", end="")
        #For each element between the first and last element at the current level
        # print out the element at that index
        for y in range(getFirstElement(x), getLastElement(x)+1):
            print(" ", tree[y], end="")
        #End the current line by printing without end=""
        print("")

#Print a formatted version of one level of the pathTree
def printLevelOfTree(tree, level):
    print("Level ", level, ":", end="")
    for x in range(getFirstElement(level), getLastElement(level)+1):
        print(" ", tree[x], end="")
    print("")

#Prints the child indices of a given index
def printChildren(index, level):
    print(index, "   Left: ", getLeftChild(index, level), "  Right: ", getRightChild(index,level))

#Calculate the maximum sum found in the tree
def findMaxPath(tree):
    #Iterate through each level except the last
    #The last level of elements are combined with the second to last level
    for x in range(numOfLevels-1, 0, -1):
        #For every element in a level, compare its two children
        for y in range(getFirstElement(x), getLastElement(x)+1):
            #Add the larger of the two to the current element
            if(tree[getLeftChild(y,x)] > tree[getRightChild(y,x)]):
                tree[y] += tree[getLeftChild(y,x)]
            else:
                tree[y] += tree[getRightChild(y,x)]
    return tree[0]

#Calculate the minimum sum found in the tree
def findMinPath(tree):
    #Iterate through each level except the last
    #The last level of elements are combined with the second to last level
    for x in range(numOfLevels-1, 0, -1):
        #For every element in a level, compare its two children
        for y in range(getFirstElement(x), getLastElement(x)+1):
            #Add the smaller of the two to the current element
            if(tree[getLeftChild(y,x)] < tree[getRightChild(y,x)]):
                tree[y] += tree[getLeftChild(y,x)]
            else:
                tree[y] += tree[getRightChild(y,x)]
    return tree[0]


#START MAIN
time_start = time.time()

#Start Time
pathTree = []
pathTree = openFile('triangle25.txt', pathTree)
numOfLevels = initNumOfLevels(pathTree)
print("Max Path Sum = ", findMaxPath(pathTree))
#End Time

time_end = time.time()
print("time taken", time_end-time_start)


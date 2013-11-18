

class Node:
    parent = None
    children = list()
    value = -1
    def __init__(self, v):
        self.value = v
    def __str__(self):
        return str(self.value) + " (p: " + str(self.parent) + ")"


def buildTree(line):
    print("todo")
    #build tree

def countCousins(t, value):
    print("todo")
    # find node with value in tree
    # count cousins from value node



# Read in numbers and build a tree from the text
data = input().split(" ")
treeinfo = input()
tree = buildTree(treeinfo)
# Now count the cousins from the given node 
# (check data line to see if number is correct)
countCousins(tree,data[1])

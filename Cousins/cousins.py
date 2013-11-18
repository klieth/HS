

class Node:
    def __init__(self, v):
        self.parent = None
        self.children = list()
        self.value = v
    def __str__(self):
        ret = str(self.value)
        if len(self.children) > 0:
            ret += " ("
        for c in self.children:
            ret += "[" + str(c) + "]"
        if len(self.children) > 0:
            ret += ")"
        return ret







root = None

def buildTree(line, value):
    root = None
    toFine = None
    arr = line.split(" ")
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    root = Node(arr[0])
    allNodes = list()
    allNodes.append(root)
    current = -1
    for i in range(1,len(arr)):
        n = Node(arr[i])
        if arr[i] == value:
            toFind = n
        allNodes.append(n)
        if (arr[i] != arr[i - 1] + 1):
            current += 1
        n.parent = allNodes[current]
        n.parent.children.append(n)
    return toFind


def countCousins(toFind):
    # count cousins from value node
    p = None
    gp = None
    if (toFind.parent != None):
        p = toFind.parent
    else:
        print (0)
        return
    if (p.parent != None):
        gp = p.parent
    else:
        print (0)
        return
    s = 0
    for c in gp.children:
        if c == p:
            continue
        for d in c.children:
            s += 1
    print (s)



# Read in numbers and build a tree from the text
while True:
    data = input().split(" ")
    if data[0] == "0" and data[1] == "0":
        break
    treeinfo = input()
    n = buildTree(treeinfo, int(data[1]))
    # Now count the cousins from the given node 
    countCousins(n)

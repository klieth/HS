
class Node:
    def __init__(self, name):
        self.name = name
        self.connections = list()
    def __str__(self):
        return "(" + str(self.name) + ")"
    def connect(self, node):
        self.connections.append(node)

class Graph:
    def __init__(self):
        self.allnodes = list()
    def add(self, node):
        self.allnodes.append(node)
    def has(self, name):
        for i in self.allnodes:
            if i.name == name:
                return True
        return False
    def get(self, name):
        for i in self.allnodes:
            if i.name == name:
                return i
        return False
    def adjmat(self):
        am = list()
        for i in range(len(self.allnodes)):
            am.append(list())
            for j in range(len(self.allnodes)):
                am[i].append(0)
        for n in self.allnodes:
            for m in n.connections:
                am[n.name-1][m.name-1] = 1
                am[m.name-1][n.name-1] = 1
        ret = ""
        for n in am:
            for m in n:
                ret += str(m)
            ret += "\n"
        return ret

nm = input().split()
g = Graph()

for i in range(len(nm)):
    nm[i] = int(nm[i])

for i in range(nm[1]):
    edgedata = input().split()
    for i in range(len(edgedata)):
        edgedata[i] = int(edgedata[i])
    start = None
    end = None
    if not g.has(edgedata[0]):
        start = Node(edgedata[0]);
        g.add(start)
    else:
        start = g.get(edgedata[0])
    if not g.has(edgedata[1]):
        end = Node(edgedata[1])
        g.add(end)
    else:
        end = g.get(edgedata[1]);
    start.connect(end)

print(g.adjmat())


class NodeRepresentation:
    def __init__(self, rawdata):
        if rawdata == "()":
            self.empty = True
            self.val = None
            self.path = None
            return
        values = rawdata.split(",")
        self.empty = False
        self.val = int(values[0][1:])
        self.path = values[1][:-1]
    def __str__(self):
        return "(" + str(self.val) + "," + self.path + ")"

class NodeBuffer:
    nodes = list()
    def __init__(self):
        print("made node buffer")
    def next(self):
        try:
            if len(self.nodes) == 0:
                self.nodes.extend(input().split(" "))
        except EOFError:
            return None
        return NodeRepresentation(self.nodes.pop(0))

class Node:
    def __init__(self,v):
        self.value = v
        self.left = None
        self.right = None
    def __str__(self):
        return self.value
    def completeTree(self):
        ret = self.value == None


buf = NodeBuffer()

nr = buf.next()

while nr != None:
    if nr.empty:
        print("end of tree")
        break
    print(nr)
    nr = buf.next()

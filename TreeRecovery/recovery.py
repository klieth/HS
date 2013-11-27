
class Node:
    def __init__(self,v):
        self.value = v
        self.left = None
        self.right = None
    def __str__(self):
        return self.value
    def postorder(self):
        ret = ""
        if self.left != None:
            ret += self.left.postorder()
        if self.right != None:
            ret += self.right.postorder()
        return ret + self.value



def buildTree(preorder, inorder):
    val = preorder.pop(0)
    n = Node(val)
    inIndex = inorder.index(val)
    if len(inorder[:inIndex]) > 0:
        n.left = buildTree(preorder, inorder[:inIndex])
    if len(inorder[inIndex+1:]) > 0:
        n.right = buildTree(preorder, inorder[inIndex+1:])
    return n


while True:
    try:
        line = input().split(" ")
        root = buildTree(list(line[0]), list(line[1]))
        print (root.postorder())
    except EOFError:
        break

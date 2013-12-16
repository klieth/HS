
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


# This is a recursive algorithm that continues to build subtrees
# until it is out of new values to add.
def buildTree(preorder, inorder):
    # grab the first value from the preorder list and make it
    # into a node
    val = preorder.pop(0)
    n = Node(val)

    # Find the index of the value from the inorder list. We
    # will use this to separate the the inorder list into a
    # left and right sublist for the lef and right subtrees,
    # respectively.
    inIndex = inorder.index(val)
    if len(inorder[:inIndex]) > 0:
        # This is the recursive call to built a subtree.
        # We attach it to n.left (or n.right) in order to
        # attach it correctly to the larger tree.
        n.left = buildTree(preorder, inorder[:inIndex])
    if len(inorder[inIndex+1:]) > 0:
        n.right = buildTree(preorder, inorder[inIndex+1:])

    # and when we're done, we need to return the tree we built
    return n


while True:
    try:
        line = input().split(" ")
        # the list(string) call is a shortcut to create a list of characters
        # from the string
        root = buildTree(list(line[0]), list(line[1]))
        print (root.postorder())
    except EOFError:
        # This is a trick to get the program to stop when there's no more input.
        break

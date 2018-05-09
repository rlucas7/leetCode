# code to implement fundamental tree ops for list of list
# representation of trees. 

# define functions to use list of lists as though they
# are binary trees

# function to "create" a binary tree
def BinaryTree(r):
    return [r, [], []]

# inserts a left child into the tree
def insertLeft(root,newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch, [], []])
    return root

# inserts a right child into the tre
def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[t, [], newBranch,])
    else:
        root.insert(2,[newBranch, [], []])
    return root

# now some getter and setter functions

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

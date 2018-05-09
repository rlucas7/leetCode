# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def minDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    ### basic idea is to find the lowest 
    ##depth *leaf* node and return this depth
    treeMinDepth = 0
    if root == None:
        return treeMinDepth
    else:
        myQ = [] # simulate a queue
        myQ.append(root) # prime the FIFO queue
        lListVals = [] # list of lists to store entries to return
        treeMinDepth += 1
        while myQ != []:
            tempNodeList = []
            for i in myQ:
                if i.right == None and i.left == None:
                    return treeMinDepth 
                if i.left != None:
                    tempNodeList.append(i.left)
                if i.right != None:
                    tempNodeList.append(i.right) 
            myQ = tempNodeList
            treeMinDepth += 1

# implementation for a nested list representation
def minDepth(root):
    """
    :type root: list of lists 
    :rtype: int
    """
    ### basic idea is to find the lowest 
    ##depth *leaf* node and return this depth
    treeMinDepth = 0
    if root == [] :
        return treeMinDepth
    else:
        myQ = [] # simulate a queue
        myQ.append(root) # prime the FIFO queue
        lListVals = [] # list of lists to store entries to return
        treeMinDepth += 1
        while myQ != []:
            tempNodeList = []
            for node in myQ:
                if node[2] == [] and node[1] == []:
                    return treeMinDepth 
                if node[1] != []:
                    tempNodeList.append(node[1])
                if node != []:
                    tempNodeList.append(node[2]) 
            myQ = tempNodeList
            treeMinDepth += 1

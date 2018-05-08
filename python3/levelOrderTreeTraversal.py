#levelOrder traversal, assume list of list representation
def levelOrder(tree):
    if tree[0]==[]:
        return None
    else:
        myQ = [] # simulate a Queue
        myQ.append(tree)
        while myQ != []:
            curNode = myQ.pop(0)
            print(curNode[0])
            if curNode[1] != []:
                myQ.append(curNode[1])
            if curNode[2] != []:
                myQ.append(curNode[2])

# return a list of lists, for level order traversal 
# each list within the list in the level set of values 
def levelOrderA(tree):
    if tree[0]==[]:
        return None
    else:
        myQ = [] # simulate a Queue
        myQ.append(tree)
        lListVals = []
        while myQ != []:
            tempNodeList = []
            tempEntryList = []
            for i in myQ:
                #curNode = myQ.pop(0)
                #print(curNode[0])
                if i[1] != []:
                    tempNodeList.append(i[1])
                if i[2] != []:
                    tempNodeList.append(i[2])
                tempEntryList.append(i[0])
            lListVals.append(tempEntryList)
            myQ = tempNodeList
        return lListVals 

## the problem gives a root node of a tree composed 
## of nodes with left/right links and a val in each node 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        else:
            myQ = [] # simulate a queue
            myQ.append(root) # prime the FIFO queue
            lListVals= [] # list of lists to store entries to return
            while myQ != []:
                tempNodeList = []
                tempNodeVals = []
                for i in myQ:
                    if i.left != None:
                        tempNodeList.append(i.left)
                    if i.right != None:
                        tempNodeList.append(i.right)
                    tempNodeVals.append(i.val)
                lListVals.append(tempNodeVals)    
                myQ = tempNodeList
            return lListVals

## TODO: add in some of my own unit tests here...
## to handle the reversed order problem 107. Binary
##  Tree Level Order Traversal II
## replace the return call w/`return lListVals[::-1]` to reverse slice

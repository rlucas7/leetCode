# code to calculate the mean level values in a binary tree 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        # first do a level order traversal to return lists for each level
        # then take the average of each level O(n) time, O(n) space
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
            levelMeans = []
            for i in range(0, len(lListVals)):
                levelMeans.append(sum(lListVals[i])/float(len(lListVals[i])))
            return levelMeans

##TODO:write some of my own unit tests

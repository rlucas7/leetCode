## (A)
##    2   
##   / \   
##  2   2
## /       \
##1        3   
##return true
##
##(B)
##     3
##    / \
##   2   5
##  / \   
##-1   4
##return false




# assume input is a root node, 
# all data are ints

# Node has self.left, self.right, self.val for 
# left child, right child, and stored value

# as code recurses down LHS, keep track of the max val, should be <= root, and
# as code recurses down RHS, keep track of the min val, shoulbe be >= root. 
def getRootVal(root):
    return root[0]

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

# inorder traversal return the list of values; useful for validation
# that a binary tree is a *valid* bst, list of list representation
def inorderValList(tree, inorderTrav=None):
  if inorderTrav == None:
      inorderTrav = []
  if tree != []:
      inorderValList(getLeftChild(tree), inorderTrav)
      inorderTrav.append(getRootVal(tree))
      inorderValList(getRightChild(tree),inorderTrav)
  isValidBST = True
  for i in range(0, len(inorderTrav)-1):
      if inorderTrav[i] > inorderTrav[i+1]:
           isValidBST = False
  return isValidBST 

# preorder traversal of list of list check if valid BST
def preorderValidBST(root, maxVal, minVal):
    if getLeftChild(root) != []:
        maxVal = max(maxVal, getRootVal(getLeftChild(root)))
    if getRightChild(root) != []:
        minVal = min(minVal, getRootVal(getRightChild(root)))

    if getRootVal(root) < maxVal or getRootVal(root) > minVal:
        return False
    else:
        return preorderValidBST(getLeftChild(root), maxVal, minVal) and preorderValidBST(getRightChild(root), maxVal, minVal)

        
    if tree:
        print(getRootVal(tree))
        preorder(getLeftChild(tree))
        preorder(getRightChild(tree))

# instead of list of lists let's assume node class

def inorderValList(tree, inorderTrav=None):
  if inorderTrav == None:
      inorderTrav = []
  if tree != []:
      inorderValList(getLeftChild(tree), inorderTrav)
      inorderTrav.append(getRootVal(tree))
      inorderValList(getRightChild(tree),inorderTrav)
  isValidBST = True
  for i in range(0, len(inorderTrav)-1):
      if inorderTrav[i] > inorderTrav[i+1]:
           isValidBST = False
  return isValidBST 

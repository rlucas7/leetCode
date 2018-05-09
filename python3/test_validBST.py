### add unit tests for validBST.py 
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
##... etc.
##
##
## NOTE: to run these tests, navigate to this directord and: `python -m unittest discover -v validBST`
## or you can do, `python test_validBST.py` in this directory 

import unittest
from fundamentalTreeOps import getRootVal
from fundamentalTreeOps import getLeftChild
from fundamentalTreeOps import getRightChild
from validBST import inorderValList

class TestBSTCheckerMethods(unittest.TestCase):

    def test_bstA(self):
        #A: in list of lists form, a valid BST
        bstA=[2,[2,[1, [], [] ],[] ],[2, [],[3, [],[]] ] ]
        self.assertTrue(inorderValList(bstA))

    def test_bstB(self):
        #B: in list of lists form, *not* a valid BST 
        bstB=[3,[2, [-1, [],[] ], [4,[],[]]],[5,[],[]] ]
        self.assertFalse(inorderValList(bstB))

    def test_bstC(self):
        #C: in list of list form, added another to check *not* valid
        bstC=[2, [2,[1,[],[]],[]],[2,[1,[],[]],[3,[],[]]] ]
        self.assertFalse(inorderValList(bstC))
        # check that s.split fails when the separator is not a string

    def testbstNull(self):
        #put in a null/empty bst
        bstNull=[]
        self.assertTrue(inorderValList(bstNull))

if __name__ == '__main__':
    unittest.main(verbosity=2)

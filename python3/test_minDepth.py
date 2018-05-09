#unit test cases for thei
import unittest
 
from fundamentalTreeOps import getRootVal
from fundamentalTreeOps import getLeftChild
from fundamentalTreeOps import getRightChild
from minDepth import minDepth 

class TestMinDepthMethods(unittest.TestCase):

    def test_minDepthA(self):
        #A: in list of lists form, a minDepth is 3
        bstA=[2,[2,[1, [], [] ],[] ],[2, [],[3, [],[]] ] ]
        self.assertEqual(minDepth(bstA), 3)

    def test_minDepthB(self):
        #B: in list of lists form, minDepth is 2 
        bstB=[3,[2, [-1, [],[] ], [4,[],[]]],[5,[],[]] ]
        self.assertEqual(minDepth(bstB),2)

    def test_minDepthC(self):
        #C: in list of list form, minDepth is 3
        bstC=[2, [2,[1,[],[]],[]],[2,[1,[],[]],[3,[],[]]] ]
        self.assertEqual(minDepth(bstC),3)
        # check that s.split fails when the separator is not a string

    def test_minDepthNull(self):
        #put in a null/empty tree, minDepth is 0
        bstNull=[]
        self.assertEqual(minDepth(bstNull),0)

    def test_minDepthIsOne(self):
        #put in a small tree check that right exit pattern 
        bstS=[0, [1,[],[]],[] ]
        self.assertEqual(minDepth(bstS),2)

if __name__ == '__main__':
    unittest.main(verbosity=2)

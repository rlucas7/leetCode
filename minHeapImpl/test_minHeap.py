#unit test cases for thei
import unittest
 
from minHeap import BinaryHeap 

class TestMinHeapMethods(unittest.TestCase):

    def test_minHeap(self):
        #A: in list of lists form, a minDepth is 3
        myHeap = BinaryHeap()
        myHeap.insert(1)
        self.assertEqual(myHeap.size(),1)

if __name__ == '__main__':
    unittest.main(verbosity=2)

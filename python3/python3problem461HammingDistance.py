# code to solve the hamming distance 
# bitwise/binary rep hamming distance 

## obligatory imports 
import argparse 
import os 

def get_parser():

        parser = argparse.ArgumentParser(description='Script \
                to generate solutions to hamming distance\
                for binary representation of number.')

        parser.add_argument('--inputPath', type = str, help = "filePath with\
                input data, either real or synthetic",
                required = False, default = ".")
	
        parser.add_argument('--outputPath', type = str, help = "directory path to place output",
                required = False, default = ".")
        
        return parser

class Solution:
#    def __init__(self, initData):
#        self.data = initData
#        self.next = None
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x = x ^ y
        y = 0
        while x:
            y += 1
            x = x & (x - 1)
        print(y)


def main(): 
    # here be the code 
    
    # parse cli options...
    parser = get_parser()
    args = parser.parse_args()
    inputPath = args.inputPath
    outputPath = args.outputPath

    ## branch if cli provided a non-default inputPath

    # here is the calculation 
    hDist = Solution()
    hDist.hammingDistance(1,2)


if __name__ == '__main__':
        main()

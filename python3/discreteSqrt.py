# code to implement a discrete sqrt problem, using Babylonian 
# method (Newton) for square root calculation, then force to int
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if(x==0):
            return 0
        else:
            boolFlag=True
            x_tMinus1 = float(x)/2
            S = float(x)
            x_t = 0.5*(x_tMinus1 + S/x_tMinus1)
            while boolFlag:
                if abs(x_t - x_tMinus1) < 0.7:
                    boolFlag=False
                x_tMinus1 = x_t
                x_t = 0.5*(x_tMinus1 + S/x_tMinus1)
            return int(x_t)

## TODO: add in unit tests 

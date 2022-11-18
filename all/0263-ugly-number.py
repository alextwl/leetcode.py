'''
2022/11/18 daily challenge

intuitive approach

keep dividing input n by appointed factors until n is reduced to 1.
'''

class Solution:
    def isUgly(self, n: int) -> bool:
        # exclude non-positives
        if n < 1:
            return False
        
        # just try to divide n by 2/3/5.
        for divisor in [2,3,5]:
            while 1:
                quo, rem = divmod(n, divisor)
                if rem != 0:
                    break
                n = quo
        
        return n==1

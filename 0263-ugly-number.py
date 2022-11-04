'''
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
            while n % divisor == 0:
                n //= divisor
        
        return n==1

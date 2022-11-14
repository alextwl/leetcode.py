'''
dynamic programming + two pointer approach

time=O(n**2)
'''

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[1] = 1 # base case: 1=1  (cannot break)
        
        for x in range(2, n+1):
            '''
            try max(left_product)*max(right_product)
            from 1 <= left <= right < x
            '''
            left = 1
            right = x - 1
            maxprod = 0
            while(left <= right):
                '''
                for all x there's always a minimum product 1 * x = x,
                so we maximize each left/right by max(x, dp[x]).
                '''
                maxprod = max(maxprod, max(left, dp[left]) * max(right, dp[right]))
                left += 1
                right -= 1
            dp[x] = maxprod
        
        return dp[-1]


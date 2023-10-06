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


'''
2023/10/06 daily challenge

botton-up dynamic programming approach
'''

class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n-1
        
        # dp[n] = the maximum product of n.
        dp = [0] * (n+1)
        
        # base cases (**not** for n <= 3.)
        dp[1] = 1  # impossible to split
        dp[2] = 2  # don't split because the only possible split 1*1 is smaller than 2. keep it.
        dp[3] = 3  # don't split because the only possible split 1*2 is smaller than 3. keep it.
        
        for v in range(4, n+1):
            ans = v
            for d in range(2, v):
                # try to find maximum product by splitting.
                ans = max(ans, d * dp[v - d])
            dp[v] = ans

        return dp[-1]


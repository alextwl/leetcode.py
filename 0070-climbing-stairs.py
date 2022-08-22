'''
hint: similar to fibonacci numbers
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # n > 2
        dp = [0] * (n+1)  # include 0-step
        # define initial ans
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3,n+1):
            '''
            climb(n stairs) = climb(n-1 stairs) + climb(n-2 stairs)

            e.g. the ways of n=3 stairs to climb equals to
                 way of n=1 stair + ways of n=2 stairs
                 because we can climb to n=3 stairs
                 from n=1 stair + 2 steps and
                 from n=2 stairs + 1 step.
            '''
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]

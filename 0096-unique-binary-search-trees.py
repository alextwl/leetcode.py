'''
dynamic programming approach

learnt from
https://leetcode.com/problems/unique-binary-search-trees/discuss/31706/Dp-problem.-10%2B-lines-with-comments

for all 1~n as root:

root=1, trees = 0! * (n-1)!
root=2, trees = 1! * (n-2)!
root=3, trees = 2! * (n-3)!
...
root=n, trees = (n-1)! * 0!

sum(trees) = dp[n] = (0! * (n-1)!) + (1! * (n-2)!) + (2! * (n-3)!) + ... + ((n-1)! * 0!)
'''

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1  # base case
        
        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
        
        return dp[n]


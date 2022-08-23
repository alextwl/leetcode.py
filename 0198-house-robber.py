'''
learnt from `From good to great. How to approach most of DP problems.`
https://leetcode.com/problems/house-robber/discuss/156523/From-good-to-great.-How-to-approach-most-of-DP-problems.
'''
class Solution:
    '''
    space=O(1)
    '''
    def rob(self, nums: List[int]) -> int:
        tmp = prev1 = prev2 = 0
        
        for num in nums:
            tmp = prev1
            prev1 = max(prev2+num, prev1)  # rob current house, or not to rob
            prev2 = tmp
        
        return prev1


class Solution2:
    '''
    space=O(n)
    '''
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums)+1)  # be care of house index shift.

        # temporary max profit when visited first house.
        # (might not rob if more profits earned when robbing 2nd house.)
        dp[1] = nums[0]  

        for house in range(1, len(nums)):
            dp[house+1] = max(dp[house], dp[house-1] + nums[house])
        
        return dp[-1]

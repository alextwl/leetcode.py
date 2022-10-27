'''
reduce to House Robber approach

count the appearance of each unique element
and sum up by House Robber approach due to similar constraints.
(when we pick a number of element, the neighbor numbers cannot be picked, just like house robber.)

more detailed explanation learnt from
https://leetcode.com/problems/delete-and-earn/discuss/109871/Awesome-Python-4-liner-with-explanation-Reduce-to-House-Robbers-Question
'''

import collections


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        '''
        space=O(1) pythonic ver, but the submission does not always beat intuitive ver...
        '''
        point_count = collections.Counter(nums)
        prev = curr = 0
        
        for i in range(10**4 + 1):
            prev, curr = curr, max(curr, prev + i * point_count[i])
        
        return curr

    
class Solution2:
    def deleteAndEarn(self, nums: List[int]) -> int:
        '''
        intuitive easy-to-read ver, time=O(n), space=O(n)
        '''
        # points{the value of element} = total earned points of the same element.
        points = [0] * (10**4 + 1)
        # max points robbed
        dp = [0] * (10**4 + 2)
        
        # sum up each element by the same number
        for num in nums:
            points[num] += num
        
        # house robber
        dp[2] = points[1]  # assume all points of 1 robbed
        
        for i in range(2, 10**4 + 1):
            dp[i+1] = max(dp[i], dp[i-1] + points[i])
        
        return dp[-1]

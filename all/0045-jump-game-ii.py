'''
dynamic programming approach

note that we don't discuss unreachable cases
because the description guarantees all test cases can reach the last position.

time=O(n**2), space=O(n)
'''

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            # no need to jump
            return 0
        
        '''
        count minimum times of jumps from the last position.
        '''
        dp = [float('inf')] * n
        
        '''
        initialize the last element to zero.
        (reaching last position from itself does not need to jump)
        '''
        dp[-1] = 0
        
        for i, jump in reversed(list(enumerate(nums[:-1]))):
            '''
            determine the minimum jump distance,
            if it couldn't reach the last position in one time,
            try to jump multiple times and memorize.
            '''
            jumped = min(i + jump, n-1)
            
            '''
            try to minimize jump times between i and jumped.
            '''
            for j in range(i+1, jumped+1):
                dp[i] = min(dp[i], dp[j] + 1)
        
        # the dp value of the first position is the minimum accumulated jump times.
        return dp[0]


'''
more clever 2-pointer approach

learnt from
https://leetcode.com/problems/jump-game-ii/discuss/170518/8-Lines-in-Python!-Easiest-Solution!
'''

class Solution2:
    def jump(self, nums: List[int]) -> int:
        '''
        always evaulate the furthest distance we can reach from nums[left:right+1],
        pick (jump from) the maximum right pointer,
        and we can get the minimum time of jumps.
        '''
        left = right = 0
        jumps = 0  # the number of jumps (not distance.)
        
        while right < len(nums) - 1:
            jumps += 1
            max_jump_distance = max([i + nums[i] for i in range(left, right+1)])
            left, right = right+1, max_jump_distance
        
        return jumps

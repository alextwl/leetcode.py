'''
dynamic programming approach

intuition: for any 3-number arithmetic sequences,
nums[i-1] - nums[i-2] == nums[i] - nums[i-1].
'''

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        
        '''
        initial values are all zeroes because
        it doesn't gurarantee there's at least 1 arithmetic sequence.
        '''
        dp = [0] * n
        # counter of final answer.
        ans = 0
        
        for i in range(2, n):
            # check if it's a valid arithmetic sequence
            if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]:
                '''
                it always increases the number of subarrays.
                e.g. for i=3,
                     nums[0:3] = [1,2,3]
                     nums[0:4] = [1,2,3,4]
                     are 2 valid seqs.
                '''
                dp[i] = dp[i-1] + 1
                '''
                and nums[1:4] = [2,3,4] (e.g. all cases ended at nums[3]) is also a unique seq.
                '''
                ans += dp[i]
        
        return ans


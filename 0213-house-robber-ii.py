'''
idea: reuse "198. House Robber" twice.

since houses were arranged in a circle,
let's rob it excluding the first or the last house,
and get the maximum between them.
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        def robbing(money: List[int]) -> int:
            '''
            :param money: list of money of each house
            '''
            house_total = len(money)
            # corner case: if there's no house.
            if house_total == 0:
                return 0
            
            dp = [0] * (house_total+1)
            dp[1] = money[0]  # assume 0-th house robbed.
            
            for i in range(1, house_total):
                '''
                max(i-th house not robbed, i-th house robbed)
                '''
                dp[i+1] = max(dp[i], dp[i-1] + money[i])
            
            return dp[-1]
        
        # corner case: if there's only one house.
        if len(nums) == 1:
            return nums[0]
        
        # rob except first or last house.
        return max(robbing(nums[1:]), robbing(nums[:-1]))

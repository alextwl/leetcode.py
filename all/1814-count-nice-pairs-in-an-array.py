'''
2023/11/21 daily challenge

count approach
'''

import collections


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        rev = lambda v: int(str(v)[::-1])
        
        # rearrange the equation:
        # nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])
        conds = [v - rev(v) for v in nums]
        
        ans = 0
        d = collections.defaultdict(int)  # the counter of seen conds.
        
        for v in conds:
            # we've seen d[v] numbers of v before,
            # so we can form another d[v] pairs with current v.
            ans = (ans + d[v]) % 1_000_000_007
            d[v] += 1

        return ans


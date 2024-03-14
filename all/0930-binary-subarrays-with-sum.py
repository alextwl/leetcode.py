'''
2024/03/14 daily challenge

prefix sum approach
'''

import collections


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        psum_freq = collections.defaultdict(int)

        ans = 0
        prefix_sum = 0
        for v in nums:
            prefix_sum += v
            
            if prefix_sum == goal:
                ans += 1

            if (diff := prefix_sum - goal) in psum_freq:
                ans += psum_freq[diff]

            psum_freq[prefix_sum] += 1

        return ans


'''
2024/07/23 daily challenge

counter approach
'''

import collections


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        ctr = collections.Counter(nums)
        # order by frequency ascending, order by value decreasing for the same frequency
        return sorted(nums, key=lambda x: (ctr[x], -x))


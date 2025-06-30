'''
2025/06/30 daily challenge

counter approach
'''


import collections


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        longest = 0
        ctr = collections.Counter(nums)
        for v, vcount in ctr.items():
            # find a neighbor key with difference of 1
            if ctr[v-1]:
                longest = max(longest, ctr[v-1] + vcount)
            if ctr[v+1]:
                longest = max(longest, ctr[v+1] + vcount)
        return longest


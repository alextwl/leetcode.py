'''
2024/01/02 daily challenge

counter approach
'''

import collections


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        d = collections.Counter(nums)
        ans = [[] for _ in range(max(d.values()))]

        for k, v in d.items():
            for i in range(v):
                ans[i].append(k)

        return ans


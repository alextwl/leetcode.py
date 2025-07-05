'''
2025/07/05 daily challenge

counter approach
'''


import collections


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans = -1
        for k, v in collections.Counter(arr).items():
            if k == v:
                ans = max(ans, k)
        return ans


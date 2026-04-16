'''
2026/04/16 daily challenge

hash table & binary search approach

build value-to-indices hash lists and lookup by binary search.
'''


import bisect
import collections


class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        valpos = collections.defaultdict(list)
        for i, v in enumerate(nums):
            valpos[v].append(i)

        ans = []
        for q in queries:
            v = nums[q]
            pos_list = valpos[v]
            m = len(pos_list)
            if m < 2:
                # v not exist or no other index in nums
                ans.append(-1)
                continue
            i = bisect.bisect_left(pos_list, q)
            # check nums[j] in the leftside
            j = (i - 1 + m) % m
            min_dist = min(abs(pos_list[j] - q), n - abs(pos_list[j] - q))
            # check nums[j] in the rightside
            j = (i + 1 + m) % m
            min_dist = min(min_dist, abs(pos_list[j] - q), n - abs(pos_list[j] - q))
            ans.append(min_dist)

        return ans


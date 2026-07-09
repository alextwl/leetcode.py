'''
2026/07/09 daily challenge

group consecutive nodes into a component (simplified union-find) approach

time=O(n+m)
'''


import itertools


class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        parent = [i for i in range(n)]
        curr_comp = 0  # the number of current component
        # note nums[] has been sorted,
        # we can easily group consecutive nodes in linear time.
        for i, (v0, v1) in enumerate(itertools.pairwise(nums), start=1):
            if v1 - v0 > maxDiff:
                # nums[i - 1] and nums[i] belong to different components
                curr_comp += 1
            parent[i] = curr_comp

        ans = [parent[a] == parent[b] for a, b in queries]
        return ans


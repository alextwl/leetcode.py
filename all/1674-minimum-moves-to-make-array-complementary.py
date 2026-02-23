'''
line sweep approach

time=O(N + limit)
'''


import collections


class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        nhalf = len(nums) >> 1
        arr0 = nums[:nhalf]
        arr1 = nums[-1:nhalf-1:-1]
        sline = collections.defaultdict(int)

        for a, b in zip(arr0, arr1):
            # 2 ops to modify both a & b < min(a, b) + 1
            sline[2] += 2
            # 1 op to modify the larger one
            sline[min(a, b) + 1] -= 1
            # no ops for target a + b
            sline[a + b] -= 1
            # 1 op to modify the smaller one
            sline[a + 1 + b] += 1
            # 2 ops (including the prev op) to modify both a & b
            # to make max(a, b) + limit < target <= limit * 2
            sline[max(a, b) + limit + 1] += 1
        
        ans = float('inf')
        curr = 0
        # note the problem guarantees max(nums) <= limit,
        # no worry for out-of-bound targets.
        for target in range(2, limit * 2 + 1):
            curr += sline[target]
            ans = min(ans, curr)

        return ans


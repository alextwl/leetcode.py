'''
2026/05/13 daily challenge

line sweep approach

time=O(N + limit)
'''


import collections


class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        nhalf = len(nums) >> 1
        arr0 = nums[:nhalf]
        arr1 = nums[-1:nhalf-1:-1]
        # sline[complementary value of a + b] = difference of count of operations
        sline = collections.defaultdict(int)

        for a, b in zip(arr0, arr1):
            # 2 ops to modify both a & b < min(a, b) + 1
            # e.g. modify both a & b to 1, so modified a + modified b == 2 with 2 ops.
            sline[2] += 2
            # 1 op to modify the larger one
            # e.g. modify a or b to 1,
            # since we've modified both 2 & b in the previous type of modification,
            # so deduct 1 operation from the count.
            sline[min(a, b) + 1] -= 1
            # no ops for target a + b
            # deduct 1 operation from the count
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


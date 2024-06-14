'''
min heap approach

always increment the smallest by 1.
'''

import heapq


class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        for _ in range(k):
            heapq.heappush(nums, heapq.heappop(nums) + 1)

        # shortcut: check zero multiplier
        if not nums[0]:
            return 0

        ans = 1
        for v in nums:
            ans = (ans * v) % 1_000_000_007

        return ans


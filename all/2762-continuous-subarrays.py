'''
2024/12/14 daily challenge

min & max heap approach

use heap to track min & max elements in the window of valid subarray
'''


import heapq


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        # min heap & max heap to track min & max elements in the window
        min_h = []  # (v, i)
        max_h = []  # (-v, i)

        ans = 0
        left = 0
        for right, v in enumerate(nums):
            # add v to the window
            heapq.heappush(min_h, (v, right))
            heapq.heappush(max_h, (-v, right))

            # check violation and shrink from the left
            while left < right and (-max_h[0][0] - min_h[0][0]) > 2:
                left += 1
                while min_h and min_h[0][1] < left:
                    heapq.heappop(min_h)
                while max_h and max_h[0][1] < left:
                    heapq.heappop(max_h)

            ans += right - left + 1

        return ans


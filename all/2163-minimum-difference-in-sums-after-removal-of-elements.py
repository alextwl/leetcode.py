'''
2025/07/18 daily challenge

max heap & min heap approach

learnt from official editorial:
https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/editorial/#approach-priority-queue

the goal is to minimize the 1st part & maximize the 2nd part to get a minimum difference (may be negative).
use max heap to remove big values from 1st part, min heap to remove small values from 2nd part.
'''


import heapq


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        m = len(nums)
        n = m // 3
        n1 = n - 1

        # pick elements for the first part
        total = sum(nums[:n])
        mh = [-v for v in nums[:n]]  # max heap
        heapq.heapify(mh)
        sums1 = [total]
        # shift between [n, n*2)
        for i in range(n, n * 2):
            total += nums[i]
            heapq.heappush(mh, -nums[i])
            total += heapq.heappop(mh)  # total -= original value
            sums1.append(total)

        # pick elements for the 2nd part
        h = nums[n * 2:]  # to be a min heap
        sum2 = sum(h)
        heapq.heapify(h)
        min_diff = sums1[-1] - sum2
        # shift between [n, n*2) in descending order
        for i in range(n * 2 - 1, n1, -1):
            sum2 += nums[i]
            heapq.heappush(h, nums[i])
            sum2 -= heapq.heappop(h)
            min_diff = min(min_diff, sums1[i - n] - sum2)

        return min_diff


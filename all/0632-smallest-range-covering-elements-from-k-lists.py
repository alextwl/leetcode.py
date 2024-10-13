'''
2024/10/13 daily challenge

min heap approach

learnt from official solution 2:
https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/solution/

the idea is to keep the smallest element from each list, maintain the range,
and try to shrink the difference of the range.
'''


import heapq


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        m = len(nums)

        # min heap for tracking the smallest element from nums
        h = []  # (val, the number of list, the number of element in a list)
        max_val = float('-inf')
        range_left = 0
        range_right = float('inf')

        # push the first element from each list
        for i, row in enumerate(nums):
            heapq.heappush(h, (row[0], i, 0))
            max_val = max(max_val, row[0])

        while len(h) == m:
            min_val, i, j = heapq.heappop(h)

            # shrink the range
            if max_val - min_val < range_right - range_left:
                range_left, range_right = min_val, max_val

            # push the next smallest element from the same list to the heap
            if (next_col := j + 1) < len(nums[i]):
                next_val = nums[i][next_col]
                heapq.heappush(h, (next_val, i, next_col))
                # update the current maximum value of the heap
                max_val = max(max_val, next_val)

        return [range_left, range_right]


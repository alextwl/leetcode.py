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


'''
two pointer approach

learnt from official solution 3:
https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/solution/

merge the nums to a single array and think of it as a subarray problem,
use two pointer to find the smallest range with maintaining the frequency of elements from each list.
'''


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        m = len(nums)
        all_nums = []
        for i, row in enumerate(nums):
            all_nums.extend(map(lambda x: (x, i), row))

        all_nums.sort()

        freq = {i: 0 for i in range(m)}
        count = 0  # the count of list covered with at least 1 element.

        range_left, range_right = 0, float('inf')

        left = 0
        for right in range(m - 1):
            list_idx = all_nums[right][1]
            freq[list_idx] += 1
            if freq[list_idx] == 1:
                count += 1

        for right in range(m - 1, len(all_nums)):
            list_idx = all_nums[right][1]
            freq[list_idx] += 1
            if freq[list_idx] == 1:
                count += 1

            while count == m:
                range_diff = all_nums[right][0] - all_nums[left][0]
                if range_diff < range_right - range_left:
                    range_left, range_right = all_nums[left][0], all_nums[right][0]

                # shrink the window
                freq[all_nums[left][1]] -= 1
                if freq[all_nums[left][1]] == 0:
                    count -= 1
                left += 1

        return [range_left, range_right]


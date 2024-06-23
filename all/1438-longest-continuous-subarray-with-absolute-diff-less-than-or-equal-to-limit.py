'''
2024/06/23 daily challenge

sliding window + min/max heap approach
'''

import heapq


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        h_min = []  # (v, indice of nums)
        h_max = []  # (-v, indice of nums)
        left = 0

        max_len = 0
        for right, v in enumerate(nums):
            heapq.heappush(h_min, (v, right))
            heapq.heappush(h_max, (-v, right))

            curr_min = h_min[0][0]
            curr_max = -h_max[0][0]
            diff = abs(curr_max - curr_min)
            if diff > limit:
                while (left < right and diff > limit):
                    # remove all elements prior to nums[left] (incl.) from heaps
                    while (h_min and h_min[0][1] <= left):
                        heapq.heappop(h_min)
                    while (h_max and h_max[0][1] <= left):
                        heapq.heappop(h_max)

                    # update absolute diff
                    curr_min = h_min[0][0]
                    curr_max = -h_max[0][0]
                    diff = abs(curr_max - curr_min)

                    # shrink window from left
                    left += 1
            else:
                max_len = max(max_len, right - left + 1)

        return max_len


'''
monotonic queue approach
'''

import collections


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        dq_min = collections.deque()  # order by increasing val
        dq_max = collections.deque()  # order by decreasing val

        left = 0
        max_len = 0
        for right, v in enumerate(nums):
            while dq_min and dq_min[-1] > v:
                # discard larger value from rightmost
                dq_min.pop()
            while dq_max and dq_max[-1] < v:
                # discard smaller value from rightmost
                dq_max.pop()

            dq_min.append(v)
            dq_max.append(v)

            # shrink from left if over limit
            while (dq_max[0] - dq_min[0] > limit):
                u = nums[left]
                if dq_max[0] == u:
                    dq_max.popleft()
                if dq_min[0] == u:
                    dq_min.popleft()
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len


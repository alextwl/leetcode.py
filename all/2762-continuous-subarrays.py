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


'''
two pointers + sigma summation formula approach
'''


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        ans = 0
        # window attributes
        w_min = w_max = nums[0]
        w_len = 0

        left = 0
        for right, v in enumerate(nums):
            w_min = min(w_min, v)
            w_max = max(w_max, v)

            # check violation
            if w_max - w_min > 2:
                w_len = right - left  # == (right - 1) - left + 1
                # summation formula
                ans += w_len * (w_len + 1) // 2

                # start a new window **here**
                left = right
                w_min = w_max = v

                # try to expand left boundary
                while left > 0 and abs((u := nums[left - 1]) - v) <= 2:
                    left -= 1
                    w_min = min(w_min, u)
                    w_max = max(w_max, u)
                if left < right:
                    w_len = right - left
                    # remove overlapped part expanded from left by summation formula
                    ans -= w_len * (w_len + 1) // 2

        # sum up last subarray
        w_len = right - left + 1  # nums[right] is included
        ans += w_len * (w_len + 1) // 2

        return ans


'''
monotonic stack approach
'''


import collections


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        # monotonic v-increasing/decreasing stacks: (i, v)
        q_min = collections.deque()
        q_max = collections.deque()

        ans = 0
        left = 0
        for right, v in enumerate(nums):
            while q_min and q_min[-1][1] >= v:
                q_min.pop()
            q_min.append((right, v))

            while q_max and q_max[-1][1] <= v:
                q_max.pop()
            q_max.append((right, v))

            while q_min and q_max and q_max[0][1] - q_min[0][1] > 2:
                # pop from left of either max/min element
                if q_max[0][0] < q_min[0][0]:
                    left = q_max[0][0] + 1
                    q_max.popleft()
                else:
                    left = q_min[0][0] + 1
                    q_min.popleft()
            # accumulate counts of more subarrays
            ans += right - left + 1

        return ans


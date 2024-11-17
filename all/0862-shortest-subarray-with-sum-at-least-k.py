'''
2024/11/17 daily challenge

deque (monotonic queue) approach

learnt from official solution 3:
https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/solution/
'''


import collections
import itertools


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)

        prefix = [0] + list(itertools.accumulate(nums))  # prefix sums
        q = collections.deque()  # maintain indices of the subarray window

        min_len = float('inf')  # minimum valid subarray length
        for i in range(n + 1):
            # shrink from left
            while q and prefix[i] - prefix[q[0]] >= k:
                min_len = min(min_len, i - q.popleft())
            # discard rightmost prefixes which are larger than current
            # because they would unnecessarily make subarray longer.
            # (consider any subarray starts from their position.)
            while q and prefix[i] <= prefix[q[-1]]:
                q.pop()

            q.append(i)

        return min_len if min_len != float('inf') else -1


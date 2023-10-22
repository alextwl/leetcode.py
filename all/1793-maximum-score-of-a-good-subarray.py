'''
2023/10/22 daily challenge

binary search approach

learnt from official solution 1
https://leetcode.com/problems/maximum-score-of-a-good-subarray/solution/

select the minimum from the right side of array
and search the beginning of subarray from the left side of array.
'''

import bisect


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        def solve(nums, k):
            n = len(nums)

            # build the prefix minimums (left subarray)
            left = list()
            curr_min = float('inf')
            for i in range(k-1, -1, -1):
                curr_min = min(curr_min, nums[i])
                left.append(curr_min)
            left.reverse()

            # build the suffix minimums (right subarray including nums[k])
            right = list()
            curr_min = float('inf')
            for i in range(k, n):
                curr_min = min(curr_min, nums[i])
                right.append(curr_min)

            # here we've built the prefix & suffix minimums
            # and they were also sorted respectively,
            # so we can run binary search on the left.

            max_score = 0
            # select each minimum number from the suffix (right subarray)
            # and search how lengthy we can extend the subarray in the prefix
            # to get maximum score.
            for j in range(len(right)):
                # find a nums[i:j+1] to build maximum score
                curr_min = right[j]
                i = bisect.bisect_left(left, curr_min)
                subarray_size = (k+j) - i + 1
                max_score = max(max_score, curr_min * subarray_size)

            return max_score

        # we've assumed the minimum number should be in the right side
        # so we also need to solve the array in reversed order
        # if the actual minimum was located in the left side.
        return max(solve(nums, k),
                   solve(nums[::-1], len(nums) - k - 1))


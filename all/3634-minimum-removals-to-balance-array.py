'''
2026/02/06 daily challenge

two pointers approach

learnt from official editorial:
https://leetcode.com/problems/minimum-removals-to-balance-array/editorial/#approach-sorting--two-pointers
'''


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        ans = n = len(nums)

        nums.sort()
        right = 0
        for left, lval in enumerate(nums):
            while right < n and nums[right] <= lval * k:
                # search the nearest value greater than x * k in the rightside
                right += 1
            # [left, right)
            ans = min(ans, n - right + left)
        return ans


'''
single loop ver

always grow the window size when
the condition of min_val * k <= max_val meets.

shrinking the window does not help to minimize the count of removals.
'''


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()

        left = 0
        xk = nums[0] * k
        for right, rval in enumerate(nums):
            if rval > xk:
                # window size remains
                left += 1
                xk = nums[left] * k

        # removals == elements outside of the window
        return left


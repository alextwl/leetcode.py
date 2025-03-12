'''
2025/03/12 daily challenge

binary search approach
'''


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)

        # find the beginning of positive integers
        begin_pos = n
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            v = nums[mid]
            if v > 0:
                r = mid - 1
                begin_pos = mid
            else:
                l = mid + 1

        # find the end of negative integers
        end_neg = n
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            v = nums[mid]
            if v < 0:
                l = mid + 1
            else:
                r = mid - 1
                end_neg = mid

        return max(n - begin_pos, end_neg)


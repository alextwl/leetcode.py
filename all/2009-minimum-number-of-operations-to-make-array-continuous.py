'''
2023/10/10 daily challenge

binary search approach

learnt from official solution 1
https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/solution/
'''


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def find(v, arr):
            l, r = 0, len(arr) - 1
            while (l <= r):
                mid = (l + r + 1) >> 1
                if arr[mid] <= v:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        n = len(nums)
        min_ops = n  # assume all nums replaced

        uniq_nums = sorted(set(nums))  # remove duplicates & sort it

        for i, val in enumerate(uniq_nums):
            # set the window of continuous range
            left = val
            right = left + n - 1

            # find the insertion point of 'right' val
            j = find(right, uniq_nums)

            # the number of operations if we replace the num at index-j
            ops = j - i

            min_ops = min(min_ops, n - ops)

        return min_ops


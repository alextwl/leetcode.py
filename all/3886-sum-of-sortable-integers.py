'''
2026/10/20 daily challenge

match all subarrays with cyclic rotations approach

learnt from official editorial 2:
https://leetcode.com/problems/sum-of-sortable-integers/editorial/#approach-2-case-analysis
'''


class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        # find all factors of n
        factors = []
        for div in range(1, isqrt(n) + 1):
            quo, rem = divmod(n, div)
            if rem == 0:
                factors.append(div)
                if quo != div:
                    factors.append(quo)

        target = sorted(nums)

        def validate(arr0, arr1):
            m = len(arr0)
            for i in range(m - 1):
                if arr0[i] > arr0[i + 1]:
                    return (arr0[i+1:] + arr0[:i+1]) == arr1
            return arr0 == arr1

        ans = 0
        for div in factors:
            for left in range(0, n, div):
                right = left + div - 1
                if not validate(nums[left:right+1], target[left:right+1]):
                    # k==div is not sortable
                    break
            else:
                # all slices are equivalent to the target, div is sortable
                ans += div
        return ans


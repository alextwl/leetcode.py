'''
2025/02/02 daily challenge
2026/05/23 daily challenge

linear search approach
'''


class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        double = nums + nums
        k = n
        # find the beginning
        for i in range(1, n):
            if nums[i-1] > nums[i]:
                k = i
                break
        # check if sorted
        for i in range(k + 1, k+n):
            if double[i-1] > double[i]:
                return False
        return True


'''
one-pass approach
'''


class Solution:
    def check(self, nums: List[int]) -> bool:
        # at most one decreased pair allowed if rotated
        decreased = False

        prev = 0
        for v in nums:
            if prev > v:
                if decreased:
                    return False
                decreased = True
            prev = v

        # check criteria if array wasn't rotated, no decreased pairs allowed
        if nums[0] < nums[-1]:
            return decreased == False

        return True


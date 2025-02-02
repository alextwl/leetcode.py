'''
2025/02/02 daily challenge

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


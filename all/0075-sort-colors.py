'''
2024/06/12 daily challenge

counting sort approach
'''


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ctr = [0, 0, 0]  # counter of red, wihte, and blue.
        for c in nums:
            ctr[c] += 1
        last = 0
        for c in range(3):
            for i in range(last, last + ctr[c]):
                nums[i] = c
            last += ctr[c]


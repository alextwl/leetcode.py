'''
set approach

find the minimum sum of removed pair and return its average.

similar to problem 2465.
'''


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        half = len(nums) // 2
        nums.sort()
        return min(a + b for a, b in zip(nums[:half], nums[-1:half-1:-1])) / 2


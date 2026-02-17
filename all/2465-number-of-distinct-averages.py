'''
set approach

the answer is equivalent to the number of distinct sum
between each pair of min/max.

no need to find actual averages.
'''


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        half = len(nums) // 2
        nums.sort()
        return len(set(a + b for a, b in zip(nums[:half], nums[-1:half-1:-1])))


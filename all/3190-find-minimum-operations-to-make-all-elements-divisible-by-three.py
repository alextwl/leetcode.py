'''
2025/11/22 daily challenge

we can either subtract 1 from or add 1 to a value to make it divisible.
'''


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(bool(v % 3) for v in nums)


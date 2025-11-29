'''
2025/11/29 daily challenge
'''


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k


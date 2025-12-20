SQ = [i * i for i in range(51)]


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        return sum(SQ[v] for i, v in enumerate(nums, start=1) if len(nums) % i == 0)


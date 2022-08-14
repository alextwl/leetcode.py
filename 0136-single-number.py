class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR solution
        # Hint: a XOR a = 0, a XOR a XOR b = b
        val = 0
        for n in nums:
            val ^= n
        return val

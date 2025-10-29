'''
2025/10/29 daily challenge
'''


class Solution:
    def smallestNumber(self, n: int) -> int:
        return (1 << n.bit_length()) - 1


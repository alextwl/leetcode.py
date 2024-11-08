'''
2024/11/08 daily challenge

prefix XOR approach

XOR all prefixes with an all-1's mask smaller than 2**maximumBit to get the ans.
'''


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        mask = (1 << maximumBit) - 1
        ans = []
        prefix_xor = 0

        for v in nums:
            prefix_xor ^= v
            ans.append(prefix_xor ^ mask)

        ans.reverse()
        return ans


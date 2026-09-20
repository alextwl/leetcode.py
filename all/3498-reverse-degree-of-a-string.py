'''
2026/09/20 daily challenge

enumeration approach
'''


Z_1 = ord('z') + 1


class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum((Z_1 - v) * i for i, v in enumerate(map(ord, s), start=1))


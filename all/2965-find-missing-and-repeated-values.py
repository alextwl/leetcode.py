'''
2025/03/06 daily challenge

set + xor approach
'''


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        a = b = 0

        xor = 0
        for row in grid:
            for v in row:
                if not a:
                    if v in seen:
                        a = v
                    seen.add(v)
                xor ^= v

        for v in range(1, len(grid) ** 2 + 1):
            xor ^= v

        b = xor ^ a

        return [a, b]


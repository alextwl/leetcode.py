'''
2025/09/04 daily challenge
'''


class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        dx, dy = abs(z - x), abs(z - y)
        if dx < dy:
            return 1
        if dx > dy:
            return 2
        return 0


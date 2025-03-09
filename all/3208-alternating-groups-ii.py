'''
2025/03/09 daily challenge

sliding window + double-length array approach
'''


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        n2 = n * 2
        tiles = colors * 2  # turn the circle into double-length array

        i = 0
        prev = tiles[0]
        j = 1
        groups = 0
        while i < n and j < n2:
            if prev == tiles[j]:
                i = j
            if j - i + 1 == k:
                groups += 1
                i += 1
            prev = tiles[j]
            j += 1
        return groups


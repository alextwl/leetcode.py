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


'''
one-pass (without window) approach

count the length of contiguous tiles and
calculate the number of alternating groups directly.
'''


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        seq_len = 1
        prev = colors[0]

        ans = 0

        # instead of using double-length array, we extend the iteration only (k-1) tiles.
        for i in range(1, n + k - 1):
            tile = colors[i % n]
            if prev == tile:
                # consecutive tiles of alt group broken, reset the length.
                seq_len = 0

            seq_len += 1
            # consecutive tiles of length m form (m-k+1) alt groups.
            if seq_len >= k:
                ans += 1
            prev = tile

        return ans


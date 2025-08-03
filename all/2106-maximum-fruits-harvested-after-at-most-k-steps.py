'''
2025/08/03 daily challenge

prefix sum + binary search approach
'''


import bisect


class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        prefix = [0] * (n + 1)
        i2pos = [0] * n

        for i, (j, v) in enumerate(fruits):
            prefix[i + 1] = prefix[i] + v
            i2pos[i] = j

        max_fruits = 0
        for x in range(k // 2 + 1):
            # optimal way: move in one direction and then then turn around only once
            # (1) move left x steps and then right (k - x*2) steps
            y = k - x * 2
            left, right = startPos - x, startPos + y
            # search the boundary of fruits to be collected
            start = bisect.bisect_left(i2pos, left)
            end = bisect.bisect_right(i2pos, right)
            max_fruits = max(max_fruits, prefix[end] - prefix[start])

            # (2) move right x steps and then left (k - x*2) steps
            left, right = startPos - y, startPos + x
            # search the boundary of fruits to be collected
            start = bisect.bisect_left(i2pos, left)
            end = bisect.bisect_right(i2pos, right)
            max_fruits = max(max_fruits, prefix[end] - prefix[start])

        return max_fruits


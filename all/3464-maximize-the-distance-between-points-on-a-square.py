'''
2026/04/25 daily challenge

binary search approach

learnt from official editorial:
https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/editorial/#approach-binary-search

binary search the max manhattan distance
'''


import bisect


class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        # flatten 2D coordinates to integers
        arr = []
        for x, y in points:
            if x == 0:
                # on left boundary
                arr.append(y)
            elif y == side:
                # on top boundary
                arr.append(side + x)
            elif x == side:
                # on right boundary
                arr.append(side * 3 - y)
            else:
                # on bottom boundary
                arr.append(side * 4 - x)
        arr.sort()

        def check(limit):
            perimeter = side * 4
            for start in arr:
                end = start + perimeter - limit
                cur = start
                for _ in range(k - 1):
                    i = bisect.bisect_left(arr, cur + limit)
                    if i == len(arr) or arr[i] > end:
                        cur = -1
                        break
                    cur = arr[i]
                if cur >= 0:
                    return True
            return False
        
        low, high = 1, side
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                low = mid + 1
                ans = mid
            else:
                high = mid - 1

        return ans


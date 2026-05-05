'''
binary search approach

time=O(n * log n)
'''


import bisect


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        distance = 0
        arr2.sort()

        for v in arr1:
            left = bisect.bisect_left(arr2, v - d)  # arr2[:i] < v - d, arr2[i:] >= v - d
            right = bisect.bisect_right(arr2, v + d)  # arr2[:i] <= v + d, arr2[i:] > v + d
            if left == right:
                # no elements in the range [v - d, v + d]
                distance += 1

        return distance


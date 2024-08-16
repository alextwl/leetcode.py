'''
2024/08/16 daily challenge

note we cannot pick up two integers from the same array,
so we need to ensure the largest & the smallest are picked from two different arrays.
'''


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        it = iter(arrays)
        row = next(it)
        min_val, max_val = row[0], row[-1]
        max_diff = 0
        
        for row in it:
            max_diff = max(max_diff, max_val - row[0], row[-1] - min_val)
            min_val = min(min_val, row[0])
            max_val = max(max_val, row[-1])

        return max_diff


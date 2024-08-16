'''
2024/08/16 daily challenge

find two largest & two smallest elements from arrays.

note we cannot pick up two integers from the same array,
so we need to ensure the largest & the smallest are picked from two different arrays.
'''


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min1_val = min2_val = 10000
        max1_val = max2_val = -10000
        min1_idx = min2_idx = max1_idx = max2_idx = None
        
        for i, row in enumerate(arrays):
            row_min, row_max = row[0], row[-1]
            if row_min < min1_val:
                min2_val, min2_idx = min1_val, min1_idx
                min1_val, min1_idx = row_min, i
            elif row_min <= min2_val:
                min2_val, min2_idx = row_min, i
            
            if row_max > max1_val:
                max2_val, max2_idx = max1_val, max1_idx
                max1_val, max1_idx = row_max, i
            elif row_max >= max2_val:
                max2_val, max2_idx = row_max, i
        
        if min1_idx != max1_idx:
            return max1_val - min1_val
        
        return max(max1_val - min2_val, max2_val - min1_val)


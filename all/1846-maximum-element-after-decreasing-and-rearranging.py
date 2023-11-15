'''
2023/11/15 daily challenge

greedy method + sorting approach
'''


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        max_val = 0

        for v in arr:
            max_val = min(max_val+1, v)

        return max_val


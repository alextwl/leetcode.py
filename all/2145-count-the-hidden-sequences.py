'''
2025/04/21 daily challenge

linear search approach

find the width of hidden array and calculate how can we place it into [lower, upper].
'''


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        min_diff = 0  # we do not need lower bound greater than zero
        max_diff = 0
        curr = 0
        for v in differences:
            curr += v
            min_diff = min(min_diff, curr)
            max_diff = max(max_diff, curr)

        width = max_diff - min_diff
        ans = upper - lower - width + 1
        return ans if ans > 0 else 0


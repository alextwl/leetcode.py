'''
2025/03/26 daily challenge

math approach

the median of sorted 1D array is the uni-value.

learnt from official editorial 1:
https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/editorial/#approach-1-sorting-and-median

proof:
f(i) is the total difference of array to make uni-value arr[i].

f(i) = (arr[i] - arr[0]) + ... + (arr[n] - arr[i])
f(i-1) = (arr[i-1] - arr[0]) + ... + (arr[n] - arr[i-1])

f(i) - f(i-1) = i * (arr[i] - arr[i-1]) + (n - i) * (arr[i-1] - arr[i])
              = (2 * i - n) * (arr[i] - arr[i-1])

consider the case of minimum operations occurs if we could make f(i) - f(i-1) == 0,
let i = (n // 2) and it's the index of the median.
'''


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # convert the grid to 1D array
        arr = []
        for row in grid:
            arr.extend(row)
        arr.sort()

        # find the median
        n = len(arr)
        median = arr[n // 2]
        common_remainder = median % x

        ops = 0
        for v in arr:
            if v % x != common_remainder:
                # we cannot modify v to the median
                return -1
            ops += abs(v - median) // x

        return ops


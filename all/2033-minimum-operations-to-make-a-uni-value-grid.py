'''
2025/03/26 daily challenge
2026/04/28 daily challenge

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


'''
simplified math approach

the difference between sums of two parts of sorted elements
is the total value we need to add to/subtract from.
'''


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = []
        # check whether all elements have the same remainder or not
        rem = grid[0][0] % x
        for row in grid:
            for val in row:
                if val % x != rem:
                    return -1
                arr.append(val)

        arr.sort()
        mid = len(arr) // 2
        if mid == 0:
            # there's only one cell.
            return 0
        # don't include central value if the length of arr is odd.
        # the center is already unified.
        return (sum(arr[-mid:]) - sum(arr[:mid])) // x


'''
prefix/suffix sums approach

iterate all elements by calculating total difference to it as an uni-value,
and minimize the difference.

the equation can be optimized with sorted array and prefix/suffix sums.

assume arr[i] is an uni-value, the equation of total difference is:

            arr[i] - arr[0]         arr[i] - arr[i-1]
left_diff = --------------- + ... + -----------------
                   x                       x
            arr[i] * i - (arr[0] + arr[1] + ... + arr[i-1])
          = -----------------------------------------------
                                 x
            arr[i] * i - prefix[i]
          = ----------------------
                       x

             arr[n-1] - arr[i]         arr[i+1] - arr[i]
right_diff = ----------------- + ... + -----------------
                     x                         x
             (arr[n-1] + arr[n-2] + ... + arr[i+1]) - arr[i] * (n - i - 1)
           = -------------------------------------------------------------
                                         x
             suffix[i] - arr[i] * (n - i - 1)
           = --------------------------------
                            x

the minimal number of operations = min((left_diff + right_diff) // x for each element in arr)
'''


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = []
        for row in grid:
            arr.extend(row)
        
        arr.sort()
        n = len(arr)

        # prefix & suffix sums (excluding current val for each position)
        prefix = [0] * n
        suffix = [0] * n
        curr_sum = 0
        rem = arr[0] % x
        for i, v in enumerate(arr):
            if v % x != rem:
                return -1
            prefix[i] = curr_sum
            curr_sum += v
        curr_sum = 0
        for i, v in enumerate(reversed(arr), start=1):
            suffix[-i] = curr_sum
            curr_sum += v
        
        min_diff = float('inf')
        # find the uni-value by minimizing the total difference
        for i in range(n):
            left_diff = (arr[i] * i - prefix[i])
            right_diff = (suffix[i] - arr[i] * (n - i - 1))
            min_diff = min(min_diff, left_diff + right_diff)
        
        return min_diff // x


'''
2022/08/27 daily challenge

learnt from
https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/discuss/83599/Accepted-C%2B%2B-codes-with-explanation-and-references
good explanation for 2D Kadane's algorithm

also see https://qr.ae/pvbUa0 for O(nlogn) version.
'''

import bisect

MIN_INT = -10**5


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        if not matrix:
            return 0

        row = len(matrix)
        col = len(matrix[0])
        ans = MIN_INT

        # recursive loops for left & right bounds of column.
        for left in range(0, col):
            # sums[row] = sum of selected range of column.
            sums = [0] * row
            for right in range(left, col):
                # where "left" is fixed and "right" is moved to next column each loop
                # build sums for row x left~right column. (== rectangles of each matrix[row][left:right])
                for i in range(0, row):
                    sums[i] += matrix[i][right]

                # Kadane's algorithm
                # find max subarray < k
                # just remember whether any culumative sum existed or not.
                csumlist = []
                curSum = 0
                curMax = MIN_INT  # default to minimum of integer k
                for csum in sums:
                    bisect.insort(csumlist, curSum)
                    curSum += csum
                    
                    # find maximum subarray which is < k within csumlist
                    idx = bisect.bisect_left(csumlist, curSum - k)
                    
                    if idx < len(csumlist):
                        # why curSum - csumlist[idx]:
                        # curSum consists of current sums of rectangle,
                        # and previous bisect is to find proper top bound of row of subarray
                        # that ensures the selected subarray is < k.
                        # It's the reason to remove csumlist[idx] from curSum because array might be > k.
                        curMax = max(curMax, curSum - csumlist[idx])

                ans = max(ans, curMax)
        return ans

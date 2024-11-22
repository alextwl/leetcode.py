'''
2024/11/22 daily challenge

pattern frequency counting approach

the hint about bitwise XOR is difficult to understand,
see official editorial for easier explanation.

learnt from official solution 2:
https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/solution/
'''


import collections


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        freq = collections.Counter()
        
        for row in matrix:
            head_val = row[0]
            pattern = ''.join("1" if v == head_val else "0" for v in row)
            freq[pattern] += 1
        
        return max(freq.values())


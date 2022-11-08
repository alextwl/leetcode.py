'''
dynamic programming + dfs approach

learnt from
https://leetcode.com/problems/unique-paths/discuss/1581998/C%2B%2BPython-5-Simple-Solutions-w-Explanation-or-Optimization-from-Brute-Force-to-DP-to-Math

use depth first search to the finish cell with memorization of path counts.
'''

import functools

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @functools.cache
        def dfs(i, j):
            '''
            traverse paths to the finish cell.
            '''
            if i >=m or j >= n:
                return 0
            if (i, j) == (m-1, n-1):
                # the finish cell to the finish cell is always 1.
                return 1
            return dfs(i+1, j) + dfs(i, j+1)  # go down + go right
        # traverse from the top-left corner
        return dfs(0, 0)


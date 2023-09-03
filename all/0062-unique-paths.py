'''
2022/08/01 daily challenge

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


'''
math combination approach

see the above reference for more detailed derivation.

we need to move m-1 steps (to the right edge)
and n-1 steps (to the lower edge),
total m-1 + n-1 = m+n-2 steps to reach the finish cell.

  m+n-2               (m+n-2)!
 C               = --------------
  (m-1) or (n-1)    (m-1)!(n-1)!

note we could cancel denominator's (m-1)! if m > n
(or (n-1)! if m < n) in the equation for faster calculation.
'''

from math import factorial

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return factorial(m+n-2) // factorial(m-1) // factorial(n-1)


'''
2023/09/03 daily challenge

math combination approach (simplified ver)
'''


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n > m:
            m, n = n, m
        
        ans = 1
        for i in range(m+n-2, m-1, -1):
            ans *= i

        divisor = 1
        for i in range(n-1, 1, -1):
            divisor *= i

        return ans // divisor


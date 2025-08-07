'''
2025/08/07 daily challenge

dynamic programming approach

learnt from official editorial:
https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/editorial/#approach-dynamic-programming
'''


class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)

        # the top-left child's fruits (diagonal path)
        total = sum(fruits[i][i] for i in range(n))

        # dp for other 2 children
        def get_fruits():
            prev = [float('-inf')] * n
            curr = [float('-inf')] * n
            prev[n-1] = fruits[0][n-1]
            for i in range(1, n - 1):
                for j in range(max(n - 1 - i, i + 1), n):
                    best = prev[j]
                    if j - 1 >= 0:
                        best = max(best, prev[j - 1])
                    if j + 1 < n:
                        best = max(best, prev[j + 1])
                    curr[j] = best + fruits[i][j]
                prev, curr = curr, prev
            return prev[-1]
        
        # dp from bottom-left corner
        total += get_fruits()

        # diagonally reflect the matrix for reusing the function
        for i in range(n):
            for j in range(i):
                fruits[i][j], fruits[j][i] = fruits[j][i], fruits[i][j]

        # dp from upper-right corner
        total += get_fruits()

        return total


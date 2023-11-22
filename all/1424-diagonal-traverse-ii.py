'''
2023/11/22 daily challenge
'''


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        # determine the number of diagonal lines
        n = 0
        for i, row in enumerate(nums):
            n = max(n, i + len(row))

        diags = [[] for _ in range(n)]

        # convert the matrix elements to line-reversed diagonal order
        for i, row in enumerate(nums):
            for j, v in enumerate(row):
                diags[i+j].append(v)

        # convert to the diagonal order
        ans = []
        for d in diags:
            for v in reversed(d):
                ans.append(v)

        return ans


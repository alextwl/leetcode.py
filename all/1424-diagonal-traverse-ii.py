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


'''
breadth first search approach
'''


import collections


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        height = len(nums)
        q = collections.deque()
        q.append((0, 0))

        ans = []

        # BFS
        while(q):
            row, col = q.popleft()
            ans.append(nums[row][col])

            # queue the cell under the current
            # if it's another beginning of a diagonal line.
            if col == 0 and (row + 1) < height:
                q.append((row+1, 0))

            # queue the right cell
            if (col + 1) < len(nums[row]):
                q.append((row, col+1))

        return ans


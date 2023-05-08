'''
2023/05/08 daily challenge
'''

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        left, right = 0, len(mat)-1  # note: the input is a square.

        for row in mat:
            ans += row[left]
            if left != right:
                ans += row[right]
            left += 1
            right -= 1

        return ans


'''
slightly faster ver
'''

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        ans = 0

        if n & 1:
            # a matrix with odd width
            half = n>>1  # find the index of row center
            for i, row in enumerate(mat):
                ans += row[i]
                if i != half:
                    ans += row[-i-1]
        else:
            # a matrix with even width
            for i, row in enumerate(mat):
                ans += row[i] + row[-i-1]

        return ans


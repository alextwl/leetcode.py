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


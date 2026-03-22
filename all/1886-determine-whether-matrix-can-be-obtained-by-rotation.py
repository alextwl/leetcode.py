'''
2026/03/22 daily challenge

in-place swap cells manually
'''


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            # 0 degree == 360 degrees
            return True

        n = len(mat)
        half0, half1 = n // 2, (n + 1) // 2

        for _ in range(3):
            # rotate 90 degrees
            # proceed rows from both terminals.
            for i in range(half0):
                for j in range(half1):
                    # swap cells in-place
                    mat[i][j], mat[n-1-j][i], mat[n-1-i][n-1-j], mat[j][n-1-i] = \
                        mat[n-1-j][i], mat[n-1-i][n-1-j], mat[j][n-1-i], mat[i][j]
            if mat == target:
                return True
        return False


'''
pythonic way to convert rows to columns

learnt from
https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/discuss/1266035/Python-Very-detailed-explanation-of-one-liner-solution-(for-python-beginners)
'''


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            # compare if initial input was equivalent to target or not.
            # 0 degree rotation == 360 degree rotation
            return True
        # rotate 3 times and compare with target
        for _ in range(0,3):
            # zip(*mat[::-1]) -> regroup each column of rows -> 90-degree rotated matrix
            mat = [list(x) for x in zip(*mat[::-1])]
            if mat == target:
                return True
        
        return False


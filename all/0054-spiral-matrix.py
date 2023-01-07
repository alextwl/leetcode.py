'''
leetcode 75 lv2 day 1
'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        seq = []
        x = y = 0
        while(True):
            # go right
            for j in range(y, right+1):
                seq.append(matrix[x][j])
            y = right
            top += 1
            # next: go down
            x += 1
            if x > bottom: break

            # go down
            for i in range(x, bottom+1):
                seq.append(matrix[i][y])
            x = bottom
            right -= 1
            # next: go left
            y -= 1
            if y < left: break

            # go left
            for j in range(y, left-1, -1):
                seq.append(matrix[x][j])
            y = left
            bottom -= 1
            # next: go up
            x -= 1
            if x < top: break

            # go up
            for i in range(x, top-1, -1):
                seq.append(matrix[i][y])
            x = top
            left += 1
            # next: go right
            y += 1
            if y > right: break

        return seq


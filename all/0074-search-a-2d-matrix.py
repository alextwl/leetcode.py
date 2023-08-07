'''
leetcode 75 lv2 day 8

binary search approach
'''


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1

        # search rows
        while(left <= right):
            middle = (left+right) // 2
            head, tail = matrix[middle][0], matrix[middle][-1]
            if head <= target <= tail:
                break
            if head > target:
                right = middle - 1
            else:
                # tail < target
                left = middle + 1
        else:
            # the target is not in any rows.
            return False

        # search columns in middle row
        row = matrix[middle]
        left, right = 0, len(row) - 1
        while(left <= right):
            mid = (left+right) // 2
            val = row[mid]
            if val == target:
                return True
            if val > target:
                right = mid - 1
            else:
                # val < target
                left = mid + 1

        return False


'''
2023/08/07 daily challenge

onepass binary search ver
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m*n - 1
        
        while(left <= right):
            mid = left + (right-left) // 2
            row, col = divmod(mid, n)
            val = matrix[row][col]
            
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


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


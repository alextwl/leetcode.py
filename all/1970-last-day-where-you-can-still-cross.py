'''
2023/06/30 daily challenge

binary search + breadth first search approach
'''

import collections


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        # note all the input coordinates are 1-based.
        def isCrossable(day):
            '''
            run BFS on the specific day.
            '''
            mat = [[0] * col for _ in range(row)]
            
            # mark the water on and before the day.
            for r, c in cells[:day]:
                # convert 1-based index to 0-based
                mat[r-1][c-1] = 1
            
            # queue land in the first row.
            q = collections.deque()
            for j, cell in enumerate(mat[0]):
                if cell == 0:
                    q.append((0, j))
                    # visit it in advance
                    mat[0][j] = -1
            
            # BFS
            last_row = row - 1
            while(q):
                i, j = q.popleft()
                if i == last_row:
                    # last row reached
                    return True
                
                # queue 4-direction neighbors
                for x, y in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                    x += i
                    y += j
                    if 0 <= x < row and 0 <= y < col and mat[x][y] == 0:
                        q.append((x, y))
                        # visit the cells first
                        mat[x][y] = -1
            
            # path to the last row not found.
            return False
        
        # binary search
        left, right = 1, row*col  # day 1 to the max day
        
        while(left < right):
            mid = left + (right - left + 1) // 2
            if isCrossable(mid):
                # mid day is verified crossable, but not mid + 1
                left = mid
            else:
                right = mid - 1

        return left


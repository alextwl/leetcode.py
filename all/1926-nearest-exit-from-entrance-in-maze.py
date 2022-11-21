'''
2022/11/21 daily challenge

breadth first search approach

(with input matrix modified for visited vertices)
'''

import collections


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # the bottom-right border index of the maze
        mm, nn = len(maze) - 1, len(maze[0]) - 1
        
        # init a fifo with the entrance
        q = collections.deque()
        q.append((entrance, 0))  # (coordinate, depth)
        
        while q:
            cell, depth = q.popleft()
            x, y = cell
            
            # boundary check
            if not (0 <= x <= mm and 0 <= y <= nn):
                continue
            
            if maze[x][y] != '.':
                # bypass walls or visited cells.
                continue
            
            if (depth > 0) and (x in [0, mm] or y in [0, nn]):
                '''
                exit found.
                since the entrance does not count as an exit,
                depth==0 is not valid.
                '''
                return depth
            
            # visit the cell
            maze[x][y] = 'v'
            
            # push next 4 direction cells
            depth += 1
            for i, j in [(1,0), (0,1), (-1, 0), (0, -1)]:
                q.append(([x+i, y+j], depth))

        # exit not found.
        return -1


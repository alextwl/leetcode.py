'''
2023/05/21 daily challenge

DFS + BFS approach
'''

import collections

WATER = 0
LAND = 1  # a land of an island to be identified
ISLAND_1ST = 2
ISLAND_2ND = 3


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        '''
        identify the lands of islands
        '''
        def dfs(x: int, y: int, island_no: int, shorelines: List[Tuple[int, int]]):
            '''
            :param x: the row index of grid
            :param y: the column index of grid
            :param island_no: the island number (ISLAND_1ST or ISLAND_2ND)
            :param shorelines: the shoreline coordinates of the island
            '''
            # boundary check
            if not(0 <= x < n and 0 <= y < n):
                return
            
            if grid[x][y] == 0:
                # water reached, add the coord to the shorelines
                shorelines.append((x, y))
            elif grid[x][y] == 1:
                # rewrite the land with no
                grid[x][y] = island_no
                # traverse the neighbors
                for i, j in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                    dfs(x+i, y+j, island_no, shorelines)

        # traverse the grid
        shores_dict = {ISLAND_1ST: [],
                       ISLAND_2ND: []}
        current_island = ISLAND_1ST
        for x in range(n):
            for y in range(n):
                if grid[x][y] == 1:
                    dfs(x, y, current_island, shores_dict[current_island])
                    # the 1st island traversed, go to next island
                    current_island = ISLAND_2ND
        

        # the matrix of the minimum length of shortest path to the 1st island
        mat = [[float('inf')] * n for _ in range(n)]
        
        # time to traverse from 1st island to 2nd island
        q = collections.deque([(x, y, 1) for x, y in shores_dict[ISLAND_1ST]])
        # BFS
        while(q):
            x, y, depth = q.popleft()

            # boundary check
            if not(0 <= x < n and 0 <= y < n):
                continue
            #print("x=%d, y=%d" % (x, y))
            if grid[x][y] == 0:
                # search only the current depth is lesser than previous one
                if mat[x][y] > depth:
                    #print("depth=%d updated" % depth)
                    mat[x][y] = depth
                    if (x, y) in shores_dict[ISLAND_2ND]:
                        # 2nd island shore reached, no need to search further
                        continue
                    # traverse the connected water
                    depth += 1
                    for i, j in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                        q.append((x+i, y+j, depth))
        #print("mat: " + str(mat))
        #print("2nd: " + str(shores_dict[ISLAND_2ND]))
        # minimize the depth of shorelines of the 2nd island
        return min(mat[x][y] for x, y in shores_dict[ISLAND_2ND])


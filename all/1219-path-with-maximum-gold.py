'''
2024/05/14 daily challenge

breadth first search + backtracing + bitset approach
'''

import collections


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # convert points to bitmask-based integers
        next_bit = 0
        xy2mask = dict()
        weight = dict()
        for x, row in enumerate(grid):
            for y, cell in enumerate(row):
                if cell:
                    node = 1 << next_bit
                    next_bit += 1
                    
                    xy2mask[(x, y)] = node
                    weight[node] = cell
        
        # create graph based on bitmask
        g = dict()
        for (x, y), node in xy2mask.items():
            g[node] = set()
            
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dx += x
                dy += y
                if 0 <= dx < m and 0 <= dy < n and grid[dx][dy]:
                    g[node].add(xy2mask[(dx, dy)])
        
        # bfs subroutine with backtracking
        def bfs(start_node):
            # visit the start node
            q = collections.deque([(start_node, weight[start_node], start_node)])  # (node bitmask, current gold, visited bitset)
            max_gold = 0
            
            while(q):
                node, gold, visited = q.popleft()
                max_gold = max(max_gold, gold)
                
                for next_node in g[node]:
                    if next_node & visited:
                        continue
                    q.append((next_node, gold + weight[next_node], next_node | visited))

            return max_gold

        # iterate each gold cell as start node
        ans = 0
        for start_node in weight.keys():
            ans = max(ans, bfs(start_node))

        return ans


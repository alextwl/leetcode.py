'''
2025/01/13 daily challenge

union find approach (rank ver)
'''


import collections


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        uf = dict()
        rank = collections.defaultdict(int)
        
        def find(coord):
            if uf.setdefault(coord, coord) != coord:
                uf[coord] = find(uf[coord])
            return uf[coord]
        
        def union(coord0, coord1):
            coord0, coord1 = find(coord0), find(coord1)
            if rank[coord1] > rank[coord0]:
                rank[coord1] += 1
                uf[coord0] = coord1
            else:
                rank[coord0] += 1
                uf[coord1] = coord0
        
        m, n = len(grid), len(grid[0])
        col_firsts = [None] * n
        for i, row in enumerate(grid):
            row_first = None
            for j, cell in enumerate(row):
                if cell:
                    if row_first is None:
                        row_first = (i, j)
                    else:
                        union(row_first, (i, j))
                    if col_firsts[j] is None:
                        col_firsts[j] = (i, j)
                    else:
                        union(col_firsts[j], (i, j))
        # update all coordinates' parents
        for coord in uf.keys():
            find(coord)
        # count the family size
        cnt = collections.Counter(uf.values())
        return sum(size for size in cnt.values() if size > 1)


'''
count nodes by rows & columns

time=O(2mn)
'''


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row_cnt = [0] * m
        col_cnt = [0] * n

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell:
                    row_cnt[i] += 1
                    col_cnt[j] += 1

        connected = 0
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell and (row_cnt[i] > 1 or col_cnt[j] > 1):
                    connected += 1

        return connected

